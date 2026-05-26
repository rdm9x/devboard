#!/usr/bin/env python3
"""Заменяет личные/брендовые упоминания в git-tracked файлах на generic.

См. CLAUDE.md «Правило №1»: репо публичный, в коде/документах не должно
быть имён компании-владельца, владельца лично, клиентов, доменно-специфичных
проектов.

Запуск:
    python3 scripts/sanitize_repo.py            # dry-run, печатает diff stat
    python3 scripts/sanitize_repo.py --apply    # реально пишет файлы

Исключения (не трогаем):
- vendored/ — сторонний код Anthropic, свои примеры.
- CLAUDE.md, audit_pride_refs.py, docs/audit/pride-rename-audit.md — содержат
  упоминания как часть правил/аудита, замены сломают смысл.
- LICENSE, NOTICE — стандартные файлы.
- PRIDE_* env-vars — legacy fallback, осознанная совместимость.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent

# Порядок важен: длинные паттерны идут первыми, чтобы короткие их не съели.
REPLACEMENTS: List[Tuple[re.Pattern, str]] = [
    # --- Email/контакты ---
    (re.compile(r"Rudich@priderussia\.com", re.IGNORECASE), "owner@example.com"),
    (re.compile(r"@priderussia\.com"), "@example.com"),
    (re.compile(r"priderussia\.com"), "example.com"),
    (re.compile(r"\bpriderussia\b"), "example"),

    # --- Клиенты (latin) ---
    (re.compile(r"LC\s+Waikiki", re.IGNORECASE), "Customer E"),
    (re.compile(r"\bSOKOLOV\b"), "Customer A"),
    (re.compile(r"\bSokolov\b"), "Customer A"),
    (re.compile(r"\bsokolov\b"), "Customer A"),
    (re.compile(r"\bKOTON\b"), "Customer B"),
    (re.compile(r"\bKoton\b"), "Customer B"),
    (re.compile(r"\bkoton\b"), "Customer B"),

    # --- Клиенты (cyrillic варианты) ---
    (re.compile(r"СОКОЛОВ"), "Customer A"),
    (re.compile(r"Соколов"), "Customer A"),
    (re.compile(r"КОТОН"), "Customer B"),
    (re.compile(r"Котон"), "Customer B"),
    (re.compile(r"Спортмастер[аеуом]?"), "Customer D"),
    (re.compile(r"спортмастер[аеуом]?", re.IGNORECASE), "Customer D"),
    (re.compile(r"\bМагнит[аеуом]?\b"), "Customer C"),
    (re.compile(r"\bmagnit\b", re.IGNORECASE), "Customer C"),

    # --- Доменно-специфичное (крышные конструкции = продукт владельца) ---
    (re.compile(r"крышных рекламных конструкций"), "outdoor billboards"),
    (re.compile(r"крышные рекламные конструкции"), "outdoor billboards"),
    (re.compile(r"крышных конструкций"), "outdoor billboards"),
    (re.compile(r"крышные конструкции"), "outdoor billboards"),
    (re.compile(r"крышная реклама"), "outdoor advertising"),
    (re.compile(r"крышной рекламы"), "outdoor advertising"),
    (re.compile(r"roofing-company"), "demo-project"),
    (re.compile(r"roofing-constructions"), "outdoor-billboards"),
    (re.compile(r"\broofing\b"), "outdoor"),

    # --- Имя и владелец ---
    (re.compile(r"\bДмитри[йяею]\b"), "owner"),
    (re.compile(r"\bDmitry\b"), "owner"),
    (re.compile(r"\bRudich\b"), "owner"),

    # --- Компания-владелец ---
    (re.compile(r"компани[еияю]\s+ПРАЙД"), "владельца"),
    (re.compile(r"ПРАЙД[аеуом]?"), "Acme"),
    # PRIDE/Pride: не трогаем PRIDE_xxx (env-vars legacy fallback)
    # и pride_tasks/pride-tasks (уже мигрированы там где надо).
    (re.compile(r"\bPRIDE(?![_A-Z])"), "Acme"),
    (re.compile(r"\bPride\b"), "Acme"),
]

# Файлы которые **полностью** не трогаем
SKIP_FILES = {
    "CLAUDE.md",                              # содержит примеры как часть правил
    "audit_pride_refs.py",                    # аудит-инструмент
    "docs/audit/pride-rename-audit.md",       # отчёт аудита
    "LICENSE",
    "NOTICE",
    "scripts/sanitize_repo.py",               # сам себя не редактирует
}

# Папки которые полностью не трогаем
SKIP_PREFIXES = (
    "vendored/",
    ".git/",
)


def git_tracked_files() -> List[Path]:
    out = subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True
    )
    return [ROOT / line for line in out.splitlines() if line.strip()]


def should_skip(rel_path: str) -> bool:
    if rel_path in SKIP_FILES:
        return True
    if any(rel_path.startswith(p) for p in SKIP_PREFIXES):
        return True
    return False


def process_file(path: Path) -> Tuple[int, str | None]:
    """Возвращает (count_replacements, new_text or None)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, IsADirectoryError):
        return 0, None

    original = text
    total = 0
    for pattern, repl in REPLACEMENTS:
        text, n = pattern.subn(repl, text)
        total += n

    if text == original:
        return 0, None
    return total, text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="реально записать изменения. Без флага — dry-run.")
    parser.add_argument("--limit", type=int, default=0,
                        help="ограничить число обрабатываемых файлов (для отладки).")
    args = parser.parse_args()

    files = git_tracked_files()
    changed_summary: List[Tuple[str, int]] = []
    total_replacements = 0
    files_processed = 0

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if should_skip(rel):
            continue
        if not f.is_file():
            continue

        n, new_text = process_file(f)
        if n == 0:
            continue

        files_processed += 1
        total_replacements += n
        changed_summary.append((rel, n))

        if args.apply:
            f.write_text(new_text, encoding="utf-8")

        if args.limit and files_processed >= args.limit:
            break

    print(f"Files changed: {len(changed_summary)}")
    print(f"Total replacements: {total_replacements}")
    print()
    for rel, n in sorted(changed_summary, key=lambda x: -x[1]):
        print(f"  {n:4d}  {rel}")

    if not args.apply:
        print("\n(dry-run; запусти с --apply чтобы записать изменения)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
