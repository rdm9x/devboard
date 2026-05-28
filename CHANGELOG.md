# Changelog

All notable changes to **devboard** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0](https://github.com/rdm9x/devboard/compare/v1.0.0...v1.1.0) (2026-05-28)


### Added

* **8e0f3bb869db:** add Flask calculator backend with safe eval and tests ([a51ddf2](https://github.com/rdm9x/devboard/commit/a51ddf2aad0293c007f0abe1e3e582b9ec398243))
* add Demo mode button and Clear demo UI (E3.3) ([912cab2](https://github.com/rdm9x/devboard/commit/912cab2a9311da3c154c4eafde5522edaec61e5a))
* add Demo mode button in settings (E3.3) — Try/Clear demo ([393651e](https://github.com/rdm9x/devboard/commit/393651e981e8029072f34f899a2915a89b7cc2ee))
* add LLM role config tests (E6.6) ([98aa619](https://github.com/rdm9x/devboard/commit/98aa619455dd78a5dd5d7ab50522830be7d55008))
* add llm/model frontmatter to all roles (E6.6) ([60a1e5a](https://github.com/rdm9x/devboard/commit/60a1e5a4e62673b85397dd4a6a9441f9e0c2f11d))
* add performance baseline docs (E8.6) ([04ed54c](https://github.com/rdm9x/devboard/commit/04ed54c7c15790d43a60d8d33135d092ab1eeff4))
* add POST/DELETE /api/demo endpoint for onboarding Demo mode ([687af32](https://github.com/rdm9x/devboard/commit/687af32c4a57fb8c89684ef60b48f8e0dc21fa9a))
* add Replay tour button in settings (E3.4) ([8bd2549](https://github.com/rdm9x/devboard/commit/8bd2549a7509c47d71dbee41bb542159be330f74))
* add role import endpoint tests and 6 example roles (E7.3-E7.5) ([b5a17f1](https://github.com/rdm9x/devboard/commit/b5a17f14995427fe200577ff9b98442e0a1632a7))
* **ADR-009 Phase 1:** Управляющий + долгосрочная память поверх dev ([96a5584](https://github.com/rdm9x/devboard/commit/96a558449a8a9e7f58cc8dd8b6dd4a33ad93a627))
* **ADR-009 Phase 2:** пилот marketing-отдел готов ([30d7d30](https://github.com/rdm9x/devboard/commit/30d7d30eaeefedef642d779ee355790c3d9622f4))
* **B1-1.5:** /api/team/start — параметр role + backend подбор скрипта ([d41d96d](https://github.com/rdm9x/devboard/commit/d41d96de68151e74646cd0db5f737ab89c4d60bf))
* **B1:** SQL migration — chat_threads + chat_messages.thread_id ([bd5bf8f](https://github.com/rdm9x/devboard/commit/bd5bf8f3a8f370cacf3c980262c3d3543873989f))
* **B2-1.6:** company-context onboarding — endpoint + inherits injection ([ec510a7](https://github.com/rdm9x/devboard/commit/ec510a7236ee674db854059fd3b419b843444ae3))
* **B2:** devboard-work.sh + .ps1 — парсинг --role &lt;slug&gt; ([8d7923b](https://github.com/rdm9x/devboard/commit/8d7923b5e1d4ecd89a26174c8888b6ad35bfd5ee))
* **B2:** Owner Dashboard Backend API (ADR-013) ([925cd92](https://github.com/rdm9x/devboard/commit/925cd92d891bf7c4d2c12db5bf18a03118563a5a))
* **B2:** REST endpoints — artifacts list + open-file + open-folder ([2888fec](https://github.com/rdm9x/devboard/commit/2888fec37a5e24f434716aae76126b556ee189e5))
* **B5-1.6:** model_hint per-role — инжекция PRIDE_TEAM_MODEL при старте сессии ([54bceb9](https://github.com/rdm9x/devboard/commit/54bceb9dd04e54b0b5f1b69495243fc5edb3a38f))
* **board:** чип PRJ-NNN на карточке задачи ([10a5cae](https://github.com/rdm9x/devboard/commit/10a5cae80e036c23a04aa9010c7daf7f69b2ec62))
* **chat Stage 5:** auto-reply — managing-director responds to owner messages ([04782ad](https://github.com/rdm9x/devboard/commit/04782ad2add3beb12dc552127b23b131511befcc))
* **chat:** turn /chat into a tab inside main page, monolithic dark theme ([63b8031](https://github.com/rdm9x/devboard/commit/63b80316b4ea6f347dba16a38495ac125c672cf5))
* **chat:** кнопки «В архив» / «Восстановить» на тредах ([f3f9424](https://github.com/rdm9x/devboard/commit/f3f942445fa0a3c517546fc245b6103456340b91))
* **chat:** убрать нативные alert/confirm/prompt — кастомные модалки ([b5ed179](https://github.com/rdm9x/devboard/commit/b5ed1799cf25c1f0cf972c98a360bf569c532c39))
* **db:** add task_artifacts migration ([6fbc9a9](https://github.com/rdm9x/devboard/commit/6fbc9a9ff45db235c00401b387cf9b5cd9f0069d))
* **E7.2:** replace model text input with dynamic dropdown per LLM provider ([d73bf9c](https://github.com/rdm9x/devboard/commit/d73bf9c8c90dc2cd42f4e881a461f25ac268bb85))
* **E7.2:** wire dynamic LLM model dropdown — HTML+i18n+CSS+e2e ([61177a8](https://github.com/rdm9x/devboard/commit/61177a88797a92a3b5e55c855d94b241122948e4))
* **F1-1.6:** split-button dropdown «Запустить команду» с выбором роли ([130134b](https://github.com/rdm9x/devboard/commit/130134bfeadc28c2853f87b282f23fcef7bd9dac))
* **F2-1.5:** Roles tab — collapsible department sections ([3497437](https://github.com/rdm9x/devboard/commit/3497437ccd82ae48dd199e7c8408323970c60f75))
* **F2-1.6:** Roles tab — единая таблица с colgroup и dept-group строками ([5358860](https://github.com/rdm9x/devboard/commit/5358860d320d7078c556b80ad115291a46b3c8b2))
* **F2.1:** DB migration enabled + PATCH endpoint + session filter + MCP field ([cbd3e54](https://github.com/rdm9x/devboard/commit/cbd3e54b9fc6a4c84c5e78c94708e668bd89d587))
* **F2.2:** checkbox на todo-карточках + CSS disabled + column counter + i18n ([cbd5aa3](https://github.com/rdm9x/devboard/commit/cbd5aa3f70a58904d30147a7bee2d9e799ff7937))
* **F2:** Threads list with search, sort by updated_at, and archive collapsible ([08d229d](https://github.com/rdm9x/devboard/commit/08d229dbc4721aef8d238669620c7967c9a272a8))
* **F3-1.5:** chat — dynamic placeholder and interlocutor description ([4372700](https://github.com/rdm9x/devboard/commit/437270067fa53074890d9ce90067616b9bf9cffc))
* **F3:** Implement active thread message rendering + input ([107f185](https://github.com/rdm9x/devboard/commit/107f185469b225293fb2fb4611f8a8979bdfb24d))
* **f3:** Owner Dashboard Frontend UI — implement project cards, progress, action items ([5571229](https://github.com/rdm9x/devboard/commit/557122977239678c1c52d92a18039f4ca8fa4670))
* **F5:** Sidebar chat button + remove right panel from kanban ([7a66958](https://github.com/rdm9x/devboard/commit/7a66958dcf4242acda7f7a4e3d9a7d1d72b5927e))
* **F5:** Sidebar chat button with onboarding tooltip ([a4a556b](https://github.com/rdm9x/devboard/commit/a4a556b50128dc9ae2bd58c53ff968c48c9b062e))
* **inbox:** секция «Отчёты по проектам» на столе — быстрый доступ ([d26a7ef](https://github.com/rdm9x/devboard/commit/d26a7efad03b85b56fec94c172f7fe46f84489e0))
* **memory:** curated manager memory — core knowledge tag, cascade archive ([19d5c13](https://github.com/rdm9x/devboard/commit/19d5c1382def94f36dfc0e95f8236bad050021b3))
* **Phase 3a B1+WIP:** chat_threads migration + chat UI scaffolding + safety rule ([fa7d7a3](https://github.com/rdm9x/devboard/commit/fa7d7a31a5ddb3b80a3709ad56d1d7aad2fe8b5c))
* **planning Stage 1:** live button + REST + schema for Phase 3b orchestration ([82ac546](https://github.com/rdm9x/devboard/commit/82ac546f70226e7811895edb8603a08aa699472b))
* **planning Stage 1:** UI + Flask endpoints (paired with previous commit) ([53554c3](https://github.com/rdm9x/devboard/commit/53554c38938be04883f586dfda9ff2481446fd5b))
* **planning Stage 2:** orchestrator + planning-mode prompts for leads ([f7ddf0a](https://github.com/rdm9x/devboard/commit/f7ddf0aa66305e819af68ef85a1a2e4e14cc4bd3))
* **planning Stage 3:** live banner + accept/reject/revise buttons ([f73b5cb](https://github.com/rdm9x/devboard/commit/f73b5cbd2ba55c7626ec5a358c37b7c3ff0f3645))
* **planning Stage 4a:** each planning session gets its own chat thread ([f962596](https://github.com/rdm9x/devboard/commit/f962596567113d55fa6632e3bf7eaf9ef438af1d))
* **planning Stage 4b:** «Принять» decomposes the plan into kanban tasks ([59d5adc](https://github.com/rdm9x/devboard/commit/59d5adc112ce54ba7e23f88ed6f2a02fc97f469f))
* **planning Stage 4c:** «Доработать» = managing-director resynthesizes report ([6cc22dc](https://github.com/rdm9x/devboard/commit/6cc22dc3debe2d2065164ae74cd3c1df3b6b6394))
* **planning:** жёсткий cost-tracking + настраиваемый лимит в форме ([245efeb](https://github.com/rdm9x/devboard/commit/245efebb39bc76c71558e3149b3205d86751d601))
* **planning:** профили моделей base/deep + chat-responder на haiku ([0a08b55](https://github.com/rdm9x/devboard/commit/0a08b5526c5ab54fdae202eaf8038027cf1143df))
* **projects:** PRJ-NNN structure + UI cleanup + 13 test repairs ([8685c95](https://github.com/rdm9x/devboard/commit/8685c95a9980ed8e72fa711fcd30f5c6093f634a))
* **report:** авто HTML-отчёт по проекту когда все задачи завершены ([53088a7](https://github.com/rdm9x/devboard/commit/53088a7bbab7a57b38df8e1e296c740c7356d67a))
* **rework:** «Доработать» реально заставляет переделать, а не закрыть повторно ([8980530](https://github.com/rdm9x/devboard/commit/898053055c0c9054637f71f37b9d5ec01808d088))
* **S1.1:** rename product pride-team → devboard across entire repo ([caf4e04](https://github.com/rdm9x/devboard/commit/caf4e042f2a992a09abf2034d136a201166b524d))
* **S1.2:** replace personal name «дмитрий» with neutral «пользователь»/«user» ([c7c245e](https://github.com/rdm9x/devboard/commit/c7c245e355c30c157d175eccd1882abb03fd79f0))
* **S15.2:** ADR-006 token optimization quick wins ([a94c6f7](https://github.com/rdm9x/devboard/commit/a94c6f7902748ab96a6aac3f4dd8015b97f7b864))
* **S16.3:** cmd+k global search + shortcuts tutorial page ([dddeda8](https://github.com/rdm9x/devboard/commit/dddeda89df5f612ba7802b059ccd480d53c94796))
* **S17.5:** persistence auto_mode при перезагрузке дашборда ([64c05e7](https://github.com/rdm9x/devboard/commit/64c05e75bf5460a55e31e54fd58ecc06e1e7ad4c))
* **S2.1:** complete Settings page — backend endpoint, en.json, aria fix ([9c920d6](https://github.com/rdm9x/devboard/commit/9c920d6bb0b27e5921ccf3810732f9cfd081d96f))
* **S2.1:** Settings page CSS — 6 sections (Language/Theme/Team/Backups/Usage/Danger) ([ab8fa37](https://github.com/rdm9x/devboard/commit/ab8fa37a35bd523ae1549c502bc945d2fc2c5c44))
* **S2.1:** Settings page CSS — layout, sections, rows, danger zone ([cb94ef8](https://github.com/rdm9x/devboard/commit/cb94ef87c9fce1a6c2e1aac808cba0d6f869424e))
* **S2.2:** output_locale backend — POST /api/team/start сохраняет locale, devboard-work.sh передаёт в claude ([bc79e9e](https://github.com/rdm9x/devboard/commit/bc79e9e3250617a81d6156034b98e41d23ad39c1))
* **S2.3:** Role names localized in EN locale ([cac1ce0](https://github.com/rdm9x/devboard/commit/cac1ce0d4aa92affd7bfa55c0c671e09d1da005c))
* **S2.4:** chat scroll-to-bottom on load + floating down-arrow button ([d4a7189](https://github.com/rdm9x/devboard/commit/d4a718909a2f5d7239e311fa47796e73d93398ab))
* **S5.2:** Statistics — lifetime task counters (done, created, rate, in-progress) ([c78e4bd](https://github.com/rdm9x/devboard/commit/c78e4bd95603fe616f2d3433cafbf17382f79100))
* **S5.3:** first-run wizard — language, expertise, theme steps ([a1e02b6](https://github.com/rdm9x/devboard/commit/a1e02b66cc77ecaee60bdec5b86d6f5d29f8bc15))
* **S5.4:** expand onboarding tour from 5 to 12 steps ([fed9572](https://github.com/rdm9x/devboard/commit/fed9572dafc590c71eaac1b5cd843f3e1197cdcf))
* **S5.5:** add reader-mode i18n keys + dashboard tests ([14732b0](https://github.com/rdm9x/devboard/commit/14732b0c27b16b548d12ce92d805742ed5b3d76e))
* **S5.5:** task modal reader-mode — TL;DR, steps, acceptance, option buttons ([8490b4e](https://github.com/rdm9x/devboard/commit/8490b4e56db12e3b00314acd5933c9c5bc5cb75a))
* **S6.4:** safety-net — MCP done → review с system-комментарием и чат-алертом ([401bd28](https://github.com/rdm9x/devboard/commit/401bd28e54664279a40107d66597cf56e8d06044))
* **S8.1:** реализация ADR-003 на уровне БД — таблица departments ([f79e743](https://github.com/rdm9x/devboard/commit/f79e743d6d59dacda1dcb2fc18f13284d83fe909))
* **S8.2:** department_id в MCP-tools + новые tools list/get/create_department ([fbaafc2](https://github.com/rdm9x/devboard/commit/fbaafc26f55c17bc04b458e8d3881764f9145aa1))
* **S8.3:** REST API endpoints для departments + обратная совместимость tasks/chat ([42b1b71](https://github.com/rdm9x/devboard/commit/42b1b71513a2cc6c54461dc92903fd856fbc68e1))
* **team:** status показывает все активные роли + dropdown без Управляющего ([9e77794](https://github.com/rdm9x/devboard/commit/9e77794cbb583b9bb5bb539d2c4396e42e51b3d6))
* **team:** главная кнопка запускает ВСЕ отделы, dropdown — точечно ([799356c](https://github.com/rdm9x/devboard/commit/799356ccabd1e9476a94df4ce82537fcb9f9eb2e))
* **v1.2:** Settings tab, dual-locale (UI+output), EN role names, chat UX ([02828d4](https://github.com/rdm9x/devboard/commit/02828d4cdf1e176fc116a7b2229f5074c717555a))
* **v1.3:** Statistics tab, sidebar reorder, plain-language teamlead mode ([fedf1d5](https://github.com/rdm9x/devboard/commit/fedf1d5b70cc245796c35f4a2ca725ad0db4e659))
* **v1.4:** final polish — i18n consistency, port unification, docs update ([0263ce7](https://github.com/rdm9x/devboard/commit/0263ce72387c441c2a110c06002532d4f8bca531))
* **v1.5:** first-run wizard, expanded tour, task reader-mode, stats fixes ([b768685](https://github.com/rdm9x/devboard/commit/b7686853318c6aec47cc5c7527657e472b6e9bf9))
* **v1.5:** first-run wizard, expanded tour, task reader-mode, stats fixes ([142df10](https://github.com/rdm9x/devboard/commit/142df107b7a04fccc97fc27decdce77b8349199a))
* **v1.6:** S6.6 — умные браузер-уведомления + секция Notifications в Settings ([cdba439](https://github.com/rdm9x/devboard/commit/cdba439ec25b5071d453ae77f5b6d3cf04ccbacf))
* **v2.0.1:** cross-platform install reliability ([aff038e](https://github.com/rdm9x/devboard/commit/aff038e190b19f6589e3bbdff7ecd361353c80a0))
* **v2.0.2:** tutorial — Learn tab с 5 страницами + onboarding integration ([eee2725](https://github.com/rdm9x/devboard/commit/eee2725ac90fbb602f27837b79b7cb6779e4f648))
* **v2.0:** Phase 2-4 — frontend departments + HR-pipeline + inter-department ([1f14d8c](https://github.com/rdm9x/devboard/commit/1f14d8c9ad84ac90d6085dfc1f1fa8c74c90eb2c))


### Fixed

* #modal-confirm → z-index: 250 (выше любого .modal: 100). ([f3d0d08](https://github.com/rdm9x/devboard/commit/f3d0d08ac1636d35dd24753c606272494a1e4352))
* 3 мелких хвоста (тесты + prompt лидов + alerts в app.js) ([e370a0f](https://github.com/rdm9x/devboard/commit/e370a0f490379035279b507e26e948e10a27092b))
* add repo root to sys.path and seed chat messages in demo endpoint ([42a5d89](https://github.com/rdm9x/devboard/commit/42a5d8962bee277058493099b17988696fc593fc))
* **ADR-009 Phase 1.7:** assignee dropdown + миграция тимлид→dev-lead + cleanup ([bacdca7](https://github.com/rdm9x/devboard/commit/bacdca7a86ef3b00382a49b444b0df3724ccec98))
* align router pick tests with counters key rename and label fix ([2097566](https://github.com/rdm9x/devboard/commit/20975660be840f09a094a7410406a3c6a6655930))
* **artifacts:** кнопка открытия файла зовёт /api/open-file вместо file:// ([f4db399](https://github.com/rdm9x/devboard/commit/f4db3998f0cb5c48d0258b968536cf5af3f47882))
* **auto-mode:** _has_pending_work проверяет весь отдел, не только лида ([88f06d8](https://github.com/rdm9x/devboard/commit/88f06d87d4f45c547f9e2d1f754bfe5fbc042adb))
* **auto-mode:** использовать smart-default role в _auto_monitor_loop ([f765117](https://github.com/rdm9x/devboard/commit/f765117b63493fa614e25325980140bdb430155c))
* **B3-1.5:** убрать hardcoded assignee='тимлид' — динамический lookup по dept_id ([6827373](https://github.com/rdm9x/devboard/commit/6827373eaa9878b17411a3bbe39eb4ddb83200dc))
* **card:** badge модели на карточке учитывает task.model_hint ([72feef9](https://github.com/rdm9x/devboard/commit/72feef92bd526896d670d6a839f5c841c5928afd))
* **chat:** live-refresh thread messages every 5s (no manual reload) ([49ea885](https://github.com/rdm9x/devboard/commit/49ea8857da1d7073626d3fd7a008bd5378bea9e1))
* **chat:** override legacy max-height:400px that pinned input mid-view ([abd616c](https://github.com/rdm9x/devboard/commit/abd616c4d951e97a196fbaa7bf64f9787f342359))
* **chat:** preserve dark theme on reload, fill the chat view to full height ([1d7ef69](https://github.com/rdm9x/devboard/commit/1d7ef69971adb72c9cdb89470f26bba97c6c3ae9))
* **chat:** use 'owner' as message author instead of unknown 'user' ([1234a72](https://github.com/rdm9x/devboard/commit/1234a7202181dda119b691c5a18a2251ee5d0154))
* **coordination:** зависимости задач + передача контекста смежных отделов ([c738d1b](https://github.com/rdm9x/devboard/commit/c738d1b3694e963c65ec55ba99bbdbea2655d672))
* correct Docker paths after cyrillics→latin rename; security hardening ([121c25c](https://github.com/rdm9x/devboard/commit/121c25ce67e20ea0aab94e8e9b4ad33b9d9608be))
* **critical:** _find_lead_for_department dev → dev-lead, не legacy 'тимлид' ([eabe4c0](https://github.com/rdm9x/devboard/commit/eabe4c0ae5288f8746e840a936a1e359aad394ce))
* **F1+F2 real:** assignee dropdown — реальная динамическая загрузка ролей ([3b23688](https://github.com/rdm9x/devboard/commit/3b236889e3ecd7f0c38ba332836605f5dca9b8dc))
* **F3-1.6:** default chat channel = Управляющий (__global__) по ADR-009 ([292f4f6](https://github.com/rdm9x/devboard/commit/292f4f6f34b951112604e425a4c4c90f06e44840))
* **F4-1.6:** legacy «тимлид» → нейтральные метки в i18n и канбане ([22371c3](https://github.com/rdm9x/devboard/commit/22371c35a957d0ac5711f9d7b5ee9e9e9f52c73f))
* hide '+ Department' button until HR-pipeline fix (issue [#0](https://github.com/rdm9x/devboard/issues/0)bead55b) ([e8cad46](https://github.com/rdm9x/devboard/commit/e8cad46cae075b8936e82b541f8bd27a842d3ec1))
* **HR-fix:** pipeline rewrite — stream-json reader + respawn for revise ([d02d492](https://github.com/rdm9x/devboard/commit/d02d4926703b14708d3755abfe1c18699da606ae))
* **inbox:** отчёты не рендерились — забыл container.appendChild(item) ([1f60df0](https://github.com/rdm9x/devboard/commit/1f60df076df5fa01b1776206da197bfbb853eb35))
* **Phase 1.8 leftover:** pyproject.toml + sqlite3.Row .get() crash ([369821d](https://github.com/rdm9x/devboard/commit/369821dae3a6551bfea55db03585cfee79c6e388))
* **planning:** orphan recovery on orchestrator start; shorter lead timeout ([893b3f0](https://github.com/rdm9x/devboard/commit/893b3f0b5ca9aa0d5a64e988db809d5466ed7b5a))
* **planning:** owner sees lead replies inside planning threads ([4ba283c](https://github.com/rdm9x/devboard/commit/4ba283cd76e092569245a056541d5367edc0a04b))
* **planning:** persist consolidated_proposal; chat-responder can't fake task creation ([84bf36f](https://github.com/rdm9x/devboard/commit/84bf36f50bf9e7662234e306a1c09afd1da53e62))
* **planning:** post a confirmation message into the active thread ([f34b5e7](https://github.com/rdm9x/devboard/commit/f34b5e7a7ede72708b508450447ce9cfdafe33be))
* **planning:** задачи привязываются к проекту — workspace/artifacts работают ([74e8251](https://github.com/rdm9x/devboard/commit/74e82511cda294af35d6da2a624ada35e2cf0322))
* recognize 'owner' role in add_chat_message_to_thread() ([bed2977](https://github.com/rdm9x/devboard/commit/bed297703b36a5ed706f1c61f40cedb2cf2c1333))
* remove duplicate api_open_folder route causing Flask AssertionError ([8bc66bd](https://github.com/rdm9x/devboard/commit/8bc66bdf70f75aafbfe065ccab89d767092a7a4d))
* **report:** таймаут генерации отчёта 180→420с для больших проектов ([88d845c](https://github.com/rdm9x/devboard/commit/88d845cb818bbc1817a23c802a7a4bf90a54dab2))
* **roles:** запрет тимлиду коммитить файлы сторонних проектов в Devboard ([b0e613c](https://github.com/rdm9x/devboard/commit/b0e613c76ad2b314846d1b432b70750f3c4d0a79))
* **roles:** тимлид больше не отвечает «принял оба правила» на старые admin-сообщения ([94733a2](https://github.com/rdm9x/devboard/commit/94733a2f395f09324a2b473a9582c29951a8b5c0))
* **roles:** тимлиду запрещены submit_result(new_status='done') и update_task(status='done') ([09eec5d](https://github.com/rdm9x/devboard/commit/09eec5d5371ccac950808378d90c26c44be6810e))
* **router:** B5 — model_hint пользователя переопределяет архитектурные labels ([f837e5d](https://github.com/rdm9x/devboard/commit/f837e5d78ad5ae2cbdb1ae3dcd3cf9069dd199c0))
* **router:** filter enabled=False tasks in pick_from_db() ([6820d92](https://github.com/rdm9x/devboard/commit/6820d92bc264ec50ed4825ba214e1506323a19c1))
* **router:** model_hint — latest task wins (вместо max rank) ([d0fba4c](https://github.com/rdm9x/devboard/commit/d0fba4c69743ba47b51729a03bbc472b48ca426d))
* **router:** pick selects freshest model_hint, ignores rank — latest wins ([30941d7](https://github.com/rdm9x/devboard/commit/30941d77e26b3a4d351e20d32b019582c97f8147))
* **routing:** use currentDepartment() — корректный localStorage ключ ([a3de1a4](https://github.com/rdm9x/devboard/commit/a3de1a492dfdcde57bee3847a90d1cfda22280cc))
* **routing:** новая задача через UI идёт в current_department, не в dev ([657bfcd](https://github.com/rdm9x/devboard/commit/657bfcdf946867f01afa9f4adfa0867d4c14c4d6))
* **S1.3-S1.5:** CSS scrollbar gap, column header z-index, i18n todo→В очереди ([630c755](https://github.com/rdm9x/devboard/commit/630c755815498cbd49fba2e407fe7be3df520743))
* **S1.4:** column header background opaque (var(--surface) не glass-bg-2) ([ba31f5d](https://github.com/rdm9x/devboard/commit/ba31f5dd4f0878ace5f5b80967fee9cd7399f64f))
* **S17.2:** ADR-006 prompt caching + model_hint end-to-end ([9a8149a](https://github.com/rdm9x/devboard/commit/9a8149a0611240055d7a720400adb9b28b21c198))
* **S17.3:** auto-mode restart — reader_thread guard before next session ([26789e2](https://github.com/rdm9x/devboard/commit/26789e2543bbbc3084f743b13bc88aee95055c4f))
* **S3.6:** demo idempotency toast — improved i18n key with reset hint ([3722d30](https://github.com/rdm9x/devboard/commit/3722d301dd7ea6255a7a24fc58f8dee396839245))
* **S5.1:** statistics show all models including haiku ([989a5e2](https://github.com/rdm9x/devboard/commit/989a5e26fd65511b2edb0fcb8c8cf805fea7b304))
* **S5.2:** move statsLifetime section before kpiGrid — lifetime counters shown first ([bfdc005](https://github.com/rdm9x/devboard/commit/bfdc00542f8a27dedd87276faa95bdcdbc93d377))
* **S6.2:** acceptance checklist — grid layout 16+1fr с гарантированным выравниванием ([a5b82ce](https://github.com/rdm9x/devboard/commit/a5b82cea07fa58f1bdfb6002440dc98445f5826c))
* **S6.2:** acceptance checklist — выравнивание чекбокса и текста на одной линии ([01376dd](https://github.com/rdm9x/devboard/commit/01376dd73e9f7b0ba27951cf1bbe9e15772c98c5))
* **S6.2:** removed duplicate .acceptance-item legacy override (was forcing 14px + cursor:default) ([a5fdfd8](https://github.com/rdm9x/devboard/commit/a5fdfd895fcb9ed55687d9bc2fa2d29b36a90ada))
* **S6.2:** tighten reader-mode typescale — TL;DR 18→14px, labels 11→10px ([1037153](https://github.com/rdm9x/devboard/commit/1037153576acd55be4dbe443ea75f3ef232dd88a))
* **S6.5:** add Cyrillic slug→i18n key mapping for Roles table display names ([418b2c9](https://github.com/rdm9x/devboard/commit/418b2c908cb841696ff31d888d0ade18ba0b6809))
* **S6.5:** убрать дубликат slug в Roles tab — оставить только display name ([ebd042b](https://github.com/rdm9x/devboard/commit/ebd042b81f6888ec006c05da342c10c863e14a55))
* **security:** isolate Devboard agents from external systems (Bitrix24) ([35333c8](https://github.com/rdm9x/devboard/commit/35333c88b73ba4ac8b976db75fa0fbb45bf4e4b2))
* **TASK_PROMPT:** лид не ждёт сигнала — делегирует todo задачи специалистов сам ([8ead9b2](https://github.com/rdm9x/devboard/commit/8ead9b23b54c34a014a1359067bcd55e510b9417))
* **TASK_PROMPT:** лид ставит wip ПЕРЕД делегированием — видимый прогресс ([f247828](https://github.com/rdm9x/devboard/commit/f247828fb91e5d83d08b00fd236960f489ef5774))
* **tasks:** «Доработать» возвращает в todo, а не в wip ([cdb5dc9](https://github.com/rdm9x/devboard/commit/cdb5dc9a52f7476e88d2326f4abde927df38a282))
* **team:** «Остановить» убивает всю process group, не только родителя ([e0acd7e](https://github.com/rdm9x/devboard/commit/e0acd7e2a1a37f59f4cd47efc36f7ea02a834c77))
* **team/start:** smart-default — запускаем lead с самой свежей todo задачей ([50bd940](https://github.com/rdm9x/devboard/commit/50bd940c877823177a8ffb5119c475e9b4b65363))
* **team:** subprocess моментально exit'ил — slug роли + env-strip ([8ccea24](https://github.com/rdm9x/devboard/commit/8ccea24d869fea28fb507f09fe40bcf58bca8532))
* **test:** fix artifacts API tests import path ([dd389fc](https://github.com/rdm9x/devboard/commit/dd389fc152fa5f4b77d2a280642a37c5ac640386))
* **test:** test_api_team_start_happy под B1 default role + сохранён marketing E2E artifact ([ad7a6ab](https://github.com/rdm9x/devboard/commit/ad7a6ab1f4e83bf744097f7286c67ea895354061))
* **ui:** confirm-диалог удаления — z-index выше карточки задачи ([f3d0d08](https://github.com/rdm9x/devboard/commit/f3d0d08ac1636d35dd24753c606272494a1e4352))
* update default sonnet model to claude-sonnet-4-6 in router ([bb7ffb7](https://github.com/rdm9x/devboard/commit/bb7ffb78135bbd0d463adbdb2c8ae9d43a2d4cb9))
* update llm_factory tests — OllamaProvider now implemented (E6.5) ([b86b4b2](https://github.com/rdm9x/devboard/commit/b86b4b2eacc4ab6a0db83446fa6854e733867e8d))
* Update test assertions for _has_pending_work_for_role refactoring ([eb7c5e4](https://github.com/rdm9x/devboard/commit/eb7c5e4eb9e91640cdf01ade8d852abe7efd7326))
* **urls:** repo path github.com/devboard/devboard → github.com/rdm9x/devboard ([adfa21b](https://github.com/rdm9x/devboard/commit/adfa21ba31d8094aae28f805e71d8411a4cf48a1))
* use EN fallbacks in tour.js to prevent RU flash on EN browser ([4c87df5](https://github.com/rdm9x/devboard/commit/4c87df54719ff069fd4dadb8251e90dcfd7186fd))
* **v1.6:** Statistics layout regression + task reader-mode v2 (полная переделка) ([e0dbc3f](https://github.com/rdm9x/devboard/commit/e0dbc3fff79b00d6e6b963c25baa65cb6d8b8f77))
* **v2.0.1+:** UTF-8 encoding + line endings + devboard-work locale/expertise ([7cdb58a](https://github.com/rdm9x/devboard/commit/7cdb58adcfe421e92b426a9a69e3f3512a065d2e))
* **v2.1.2:** token optim verified + auto-mode restart bug fix ([8eeed9f](https://github.com/rdm9x/devboard/commit/8eeed9f1a7e2bf032845d9941536b75087b32cda))
* **windows:** UTF-8 encoding для PowerShell и subprocess — лечим иероглифы ([4136882](https://github.com/rdm9x/devboard/commit/4136882f46a7cd7c2d1320dc4ef210cbed4935b7))
* динамическая валидация ролей + onboarding skipped flag ([2451d54](https://github.com/rdm9x/devboard/commit/2451d54e4d4d1b669e1fc848a457cda04bd88e17))
* добавить pyyaml в dependencies dashboard (roles/validator.py) ([05d9432](https://github.com/rdm9x/devboard/commit/05d94326928f9fb21c36e4d2e78641be525fd8b3))
* чип модели на карточках учитывает модель роли-исполнителя из БД ([c2e3151](https://github.com/rdm9x/devboard/commit/c2e31512a0a6492649161a125fc5e4549d82484c))


### Changed

* rename env vars PRIDE_* to DEVBOARD_* ([e00c537](https://github.com/rdm9x/devboard/commit/e00c5372c1be23940015dc5f8fb2fec7bfba3379))
* rename MCP server pride-tasks to devboard-tasks ([ec0cda7](https://github.com/rdm9x/devboard/commit/ec0cda7d6724643b73d1d92b9bae3afa8b5e5d23))
* rename pride_tasks module to devboard_tasks ([0eb5933](https://github.com/rdm9x/devboard/commit/0eb59333da95b8851010322e5316384ac55a2980))

## [2.1.2] - 2026-05-25

Token optimisation verified + auto-mode reliability fix.

### Added
- **ADR-006 token-opt audit** (S17.1): `docs/qa/token-opt-audit-2026-05.md` — checklist of 4 quick-wins; 2 of 4 confirmed applied, 2 gaps identified and fixed in S17.2.
- **Prompt caching enabled** (S17.2): `ANTHROPIC_PROMPT_CACHING_ENABLED=1` uncommented in `devboard-work.sh`; added to `devboard-work.ps1`. Expected −30% input tokens on repeated sessions.
- **model_hint end-to-end** (S17.2): UI dropdown (auto/haiku/sonnet/opus) in new-task modal; `app.js` passes value to API; `router.py` `pick()` uses hint as model override. 8 new tests in `test_router.py`.

### Fixed
- **Auto-mode restart race condition** (S17.3): `_auto_monitor_loop` was launching a new session before `_stream_reader` released the SQLite write-lock, causing `claude` to time out after 90 s with `is_error=1`. Fix: `reader_thread` guard in `_auto_can_start` blocks restart until cleanup completes. 4 new tests in `test_team_process.py`.

## [2.1.1] - 2026-05-25

Tutorial deep dive — full learning content for non-technical users.

### Added
- **Tutorial Intro expanded** (S16.1): `learn.page.intro.body` 934→4271 chars — concept explanation vs ChatGPT/Copilot, 7-role guide with LLM model rationale, ASCII task lifecycle diagram, "what devboard cannot do" section.
- **Tutorial Tasks expanded** (S16.1): `learn.page.tasks.body` 1548→8696 chars — 5 good/bad example pairs (UI fix, new feature, docs, business logic, analytics) with detailed breakdowns + "what to do when a task stalls" section.
- **Tutorial Departments+HR expanded** (S16.2): `departments.body` +4524 chars (7 department scenarios, lifecycle, SVG diagram), `hr.body` +5353 chars (6-step state machine, 3 full chat transcripts, 5 templates, troubleshooting).
- **Cmd+K global search** (S16.3): keyboard listener `Cmd/Ctrl+K` → focus `#search`; `?`/`Cmd+/` → shortcuts overlay; `Esc` closes modals. `shortcuts.body` expanded to 1584 chars with full shortcut table.

## [2.0.0] - 2026-05-23

First multi-team release of **devboard**. The single-team kanban becomes a platform of AI departments, each with its own roles, kanban, and chat. Existing v1.x installs upgrade automatically via an idempotent migration that moves every existing task, role, and chat message into the default `dev` department. Three accepted ADRs lock in the design.

### Added

- **Departments (ADR-003).** New `departments` table; `department_id` foreign key on `tasks`, `roles`, and `chat_messages`. `NULL` is reserved for global rows — HR/owner roles and the inter-department audit channel. Indexes `(department_id, status)` keep per-department kanban queries cheap. Migration script `scripts/migrate_v2_departments.py` is atomic, idempotent, and supports `--rollback`. Three new MCP tools (`list_departments`, `get_department`, `create_department`); existing tools (`create_task`, `list_tasks`, `chat_post`, `chat_recent`) accept an optional `department_id` (default `'dev'`). REST endpoints: `GET /api/departments`, `GET /api/departments/<id>`, `POST /api/departments`, `PATCH /api/departments/<id>/archive`. `GET /api/tasks` and `GET /api/chat` honour `?department=<id>` and fall back to `dev`.
- **HR role + 5 department templates (ADR-004).** New global role `roles/hr.md` (`department_id = NULL`) — a meta-agent that creates departments from YAML templates via a chat-driven edit loop with the owner. Five MVP templates live in `templates/departments/`: `marketing-v1`, `design-v1`, `sales-v1`, `support-v1`, `operations-v1`. HR pipeline state machine (`idle → hr_planning → awaiting_owner_review → hr_revising → hr_activating → active`) with hard limits: max 8 roles per department, max 5 edit iterations, whitelisted models only, no destructive-labelled roles. Every generated role file carries `extras.hr_meta` (template_id, hr_session_id, customizations) for auditable history.
- **Inter-department workflow (ADR-005).** New columns `tasks.requester_department_id` and `tasks.requester_role_slug`. Only a department Lead (or owner) can create cross-department tasks via `POST /api/departments/<target>/tasks`; rank-and-file roles are blocked at both the REST layer and the MCP layer. The receiving Lead may **take** or **counter-propose** — there is no `Decline`. `P1`/`P2` priorities and `requires_budget`/`destructive` labels escalate to the owner's Inbox. Global append-only `inter_department_events` table with SQL triggers that reject UPDATE/DELETE. Capacity badges in the sidebar (`N in work, M in queue`), position-preview on cross-task creation; no ETA promises. Owner has two escape hatches: `priority-bump` and `admin-override`. Rate limit: 10 `P3` cross-tasks per 24h per (requester, target) pair.

### Migration

Upgrade from any v1.x to v2.0.0 is **automatic and idempotent**:

- The dashboard runs `scripts/migrate_v2_departments.py` on first start. It creates the `departments` table, inserts the default row `id='dev'`, adds the `department_id` column to `tasks`/`roles`/`chat_messages`, and backfills every existing row to `'dev'`. Global roles (`hr`, `owner`, `user`, `пользователь`) keep `department_id = NULL`.
- The migration is wrapped in a single transaction. If any step fails the database is left on v1.x.
- A `--rollback` mode restores from the auto-created `*.pre-v2.bak` backup.
- The v1.6 → v2.0 path is covered end-to-end by the smoke test `mcp_server/tests/test_v2_migration_smoke.py` (replays the anonymised fixture `tests/fixtures/v1.6_snapshot.db`, asserts no row counts change, asserts the second and third runs are no-ops).

See [`docs/migration-v2.md`](docs/migration-v2.md) for the full upgrade guide.

## [2.1.0] - 2026-05-24

Night-batch release: Windows reliability + tutorial + token optimization.
Includes all of v2.0.1, v2.0.2, and v2.1.0 changes landed via automated sprints S13–S15.

### Added
- **Token optimization (ADR-006)** (S15.1/S15.2): `chat_recent` default limit 50→10; `model_hint` optional field on tasks (DB column + MCP tools `create_task`/`update_task`/`list_tasks`/`get_task`); `AGENTS.md` split into core (~70 lines) + `docs/AGENTS_EXTENDED.md` (full reference); `ANTHROPIC_PROMPT_CACHING_ENABLED` comment in `devboard-work.sh`. Expected: −30–50% tokens/session (baseline $2.92 → target $1.80).
- **Tutorial вкладка /learn** — see v2.0.2 below.
- **Docker-first + Windows reliability** — see v2.0.1 below.

### Fixed
- `scripts/migrate_s15_model_hint.py` — idempotent standalone migration for existing DBs.

## [2.0.2] - 2026-05-24 (tutorial)

### Added
- **Tutorial вкладка /learn** (S14.1): двухколоночный layout (TOC 200px + long-read article), 5 страниц, localStorage для текущей страницы, re-render при смене локали, a11y + light/dark.
- **Контент: Введение + Как формулировать задачи** (S14.2): метафора виртуальных сотрудников, 5-шаговый workflow, ограничения; примеры хороших/плохих задач с `.example-good` / `.example-bad` стилизацией; EN + RU.
- **Контент: Отделы + HR** (S14.3): когда нужен отдел, как создать, шаблоны; бриф для HR с примерами good/bad, edit-loop; EN + RU.
- **Страница Shortcuts + wizard интеграция** (S14.4): таблица горячих клавиш (`Esc`, `Ctrl/Cmd+Enter`, `Ctrl/Cmd+K` coming soon); кнопка «Открыть обучение» в last step first-run wizard; кнопка Replay tutorial в Settings.

## [2.0.1] - 2026-05-24 (windows reliability)

### Added
- **Docker-first Quick Start** (S13.1): `docker compose up` инструкция в README.md, README.ru.md, README_WINDOWS.md как primary path; порт исправлен 5000→4999 в Dockerfile EXPOSE/HEALTHCHECK и docker-compose.yml ports/healthcheck.
- **Windows diagnostic mode** (S13.2): `"Запустить devboard.bat" --diag` — печатает Python/OS/encoding/venv/ExecutionPolicy без запуска дашборда.
- **Cross-platform troubleshooting guide** (S13.3): `docs/INSTALL_TROUBLESHOOTING.md` — гайд по типичным ошибкам install на Windows/macOS/Linux.

### Fixed
- **setup.py Windows UTF-8** (S13.2): `sys.stdout.reconfigure(encoding="utf-8")` под `IS_WINDOWS` guard; `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1` propagated во все дочерние subprocess через `run()` helper.
- **ExecutionPolicy** (S13.2): батник автоматически делает `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` при запуске.
- **Error message Python not found** (S13.2): добавлена ссылка на python.org/downloads с явной инструкцией про галочку "Add Python 3.x to PATH".
- **CRLF protection** (S13.3): `.gitattributes` — `*.sh eol=lf`, `*.ps1 eol=crlf`, `*.py eol=lf`; устраняет `bad interpreter ^M` при клонировании на Windows с `autocrlf=true`.
- **HR subprocess encoding** (S13.3): `dashboard/hr.py::spawn_hr_subprocess` — добавлены `encoding="utf-8"`, `errors="replace"` и `env["PYTHONUTF8"]="1"`; кириллица в HR-сессиях на Windows больше не превращается в мусор.
- **devboard-start.ps1 hardcoded port** (S13.3): заменён `5000` на `$env:PRIDE_DASHBOARD_PORT` (по умолчанию `4999`) в сообщении «already running».
- **devboard-work.ps1 feature parity** (S13.3): добавлены output_locale (`data/.output_locale` → `LANG_PROMPT`), user_expertise (`data/.user_expertise` → `DEVBOARD_USER_EXPERTISE`), ветка `non-tech` с `$ExpertisePrompt`; паритет с `.sh`-версией достигнут.

## [Unreleased] / v2.0-alpha.1 (departments backend)

### Added

- **Departments data model** (S8.1, ADR-003): new `departments` table in SQLite; `department_id` column added to `tasks`, `roles`, `chat_messages`; `ensure_dev_department()` migrates all existing data to the default `dev` department; `scripts/migrate_v2_departments.py` with idempotent run and `--rollback` support.
- **MCP-tools: department support** (S8.2): `create_task`, `list_tasks`, `chat_post`, `chat_recent` accept optional `department_id` (default `'dev'`); three new tools — `list_departments`, `get_department`, `create_department`.
- **REST API: /api/departments** (S8.3): `GET /api/departments`, `GET /api/departments/<id>`, `POST /api/departments`, `PATCH /api/departments/<id>/archive`; `GET /api/tasks` and `GET /api/chat` now accept `?department=<id>` with backward-compatible fallback to `'dev'`.

## [Unreleased] / v1.6 (local)

### Fixed

- **Statistics layout regression** (S6.1): restored original KPI grid layout broken by S5.2. Lifetime counters moved into a dedicated `#statsLifetime` section at the top with new `.lifetime-counter-grid` / `.lifetime-counter-card` classes (4 cards in a row, 2×2 on ≤768 px, colour-coded: green / blue / accent / yellow). Existing sections (models, roles, heatmap) unchanged.
- **Task modal reader-mode v2** (S6.2): complete rewrite of task detail overlay. Shows TL;DR prominently (18 px, accent border-left), inline option-buttons for numbered choices (click posts a comment), acceptance checklist with localStorage state, and a collapsible "Technical details" section. Fallback to plain markdown for tasks without TL;DR. 6 i18n keys added. New `test_task_parser.py` (6 tests).

## [Unreleased] / v1.5 (local)

### Added

- **First-run wizard** (S5.3): full-screen overlay on first open — 4 steps (language, expertise level, theme, done). Saves `ui_locale`, `output_locale`, `user_expertise`, `devboard-theme` to localStorage. Launches onboarding tour automatically after completion. Settings → Danger zone: reset/restart buttons.
- **Expanded onboarding tour** (S5.4): 12 steps covering all 6 nav-items (Board, Inbox, Statistics, Roles, Archive, Settings), topbar controls (Start, Auto mode), and chat panel. Replaces the previous 5-step tour.
- **Task reader-mode** (S5.5): task modal now shows structured view — large TL;DR, steps checklist, acceptance checklist, and inline answer buttons for option questions. Raw markdown collapsed under "Technical details" toggle. Backend: `GET /api/tasks/<id>/parsed` endpoint.
- **Statistics lifetime counters** (S5.2): 4 large KPI cards (tasks done, total created, completion rate %, in progress) always shown across full history including archived tasks. Count-up animation on render.

### Fixed

- **Statistics haiku model** (S5.1): `COALESCE(SUM(total_cost_usd), 0.0)` prevents `TypeError` crash in stats endpoint when haiku sessions have `NULL` cost — all models including `claude-haiku-4-5-20251001` now appear in the models breakdown.
- **Inbox nav label** (S5.7): RU sidebar nav label «Inbox» → «На столе»; EN unchanged.
- **Inbox group height** (S5.7): `.inbox-groups { align-items: start }` — each group sizes to its own content instead of stretching to match the tallest group.

## [Unreleased] / v1.4 (local)

### Added

- **i18n coverage** (S4.1): wrapped ~28 hardcoded Russian `title`/`aria-label`/`placeholder` attributes in `kanban.html` and `app.js` with `data-i18n-attr` — all tooltips now follow UI locale.
- **`name_en` in example roles** (S4.8): all 6 `roles/examples/*.md` now have `name_en` and `slug` frontmatter fields; passes role validator.
- **AGENTS.md caveats** (S4.6): added 4 entries to "Частые подводные камни" — Settings, Statistics, i18n public API, plain-language mode.
- **README features** (S4.4): `README.md` and `README.ru.md` now mention Settings tab, Statistics tab, dual-language i18n, and plain-language mode.

### Changed

- **Port unified to 4999** (S4.3): `dashboard/app.py` default, `.env.example`, `devboard-start.sh`, `README.md`, `README.ru.md`, `CONTRIBUTING.md`, `DEPLOYMENT.md`, `README_WINDOWS.md`, `setup.py`, `docs/launch/devto-post.md`.
- **Error responses** (S4.2): backend (`app.py`, `tools.py`) now returns both `{"причина": …, "reason": …}` dual-key; frontend reads `err.причина || err.reason`.
- **`ARCHITECTURE.md`** (S4.5): ADR-002 → Accepted, new endpoints (`/api/settings/static-info`, `/api/stats/aggregates`, `/api/demo`), `name_en` mentioned in roles frontmatter section.

### Fixed

- **Stale path refs** (S4.7): removed all `/D.AI/команда` from docstrings/comments in `app.py`, `server.py`, `db.py`, `devboard-work.sh`, `roles/*.md`, `approval_gates.md`.
- **Orphaned TODO** (S4.9): removed `TODO(E2.3)` comment from `locale-switcher.js` — `i18n-loader.js` (E2.3) is long done.

## [Unreleased] / v1.3 (local)

### Added

- **Statistics tab** (S3.2): new sidebar entry with 5 sections — KPI cards (sessions, turns, cost, files, lines, hours), model breakdown table with inline bars, role activity bars, 24h hourly heatmap, top achievements. Zero external dependencies; vanilla CSS animations. Backend: `GET /api/stats/aggregates?range=today|24h|week|all` with 60s cache.
- **Sidebar reorder** (S3.3): Board → Inbox → Statistics → Roles → Archive → Settings. Default view on first load is Board; `last_view` persisted in localStorage.
- **Plain-language mode** (S3.4): `user_expertise` toggle in Settings (Developer / Non-developer). Stored in `localStorage`; sent to `POST /api/team/start`; saved in `data/.user_expertise`; read by `commands/devboard-work.sh` which adds a `--append-system-prompt` block for non-technical users.

### Removed

- **Usage section from Settings** (S3.1): moved to the dedicated Statistics tab. Settings now has 5 sections (Language / Theme / Team / Backups / Danger zone).

## [Unreleased] / v1.2 (local)

### Added

- **Settings page** (S2.1): full settings tab with 6 sections — Language, Theme, Team, Backups, Usage, Danger zone. Replaces the read-only "Status" sidebar item.
- **Dual-axis i18n** (S2.2): separate `ui_locale` (interface language) and `output_locale` (team chat/task language). Output locale stored in `data/.output_locale` and injected into claude via `--append-system-prompt`.
- **EN role names** (S2.3): roles display as `Team Lead / Backend / QA / Architect / Frontend / DevOps / Tech Writer` when `ui_locale=en`. Resolved via `ROLE_DISPLAY` map in `app.js`; `name_en` frontmatter added to all `roles/*.md`.
- **Chat UX** (S2.4): auto-scroll to bottom on load; floating ⬇ button with unread badge when scrolled up; auto-scroll on new messages if already at bottom.

### Fixed

- `.gitignore`: added `data/.env.local` and `data/.output_locale` to prevent accidental credential/runtime-state commits.

## [1.1.0] - 2026-05-22

### Changed

- Product renamed: `pride-team` → `devboard` across the entire repo (sidebar brand, README, packages, configs, launcher scripts).
- Owner role renamed: `пользователь`/`пользователь` → `пользователь`/`user` in code, i18n, tests, and DB migration script (`scripts/migrate_user_to_user.py`) for open-source friendliness.
- i18n RU: todo column label "К работе" → "В очереди".

### Fixed

- CSS: scrollbar in kanban columns no longer overlaps card borders (`padding-right: 8px; scrollbar-gutter: stable` on `.column .cards`).
- CSS: column header no longer hidden by top-card hover transform (`position: sticky; z-index: 2` on `.column h2`).

## [1.0.0] - Unreleased

First public release. Open-source baseline of devboard — a local kanban driven by a small fleet of AI role-bots (Team Lead, Backend, QA, and optional specialists).

### Added

- MIT `LICENSE` and `NOTICE` files at the repository root.
- Top-level `.gitignore` covering `.env`, virtualenvs, build artifacts, IDE files, and SQLite WAL/SHM siblings.
- `gitleaks` audit run on the full git history; no secrets leaked.
- English UI with runtime i18n switcher backed by `static/i18n/{ru,en}.json`.
- Onboarding tour: 5-step first-run popovers across kanban, task detail, run-team, approvals, and chat.
- Empty-state illustrations and copy for empty kanban columns and chat thread.
- Demo mode: one-click seeding of a sample task graph for first-time exploration.
- `README.md` rewritten as the public landing page (quickstart, screenshots placeholder, roles, configuration, architecture-at-a-glance).
- `CONTRIBUTING.md` covering setup, code style, branching, adding roles and LLM providers, testing, and PR process.
- `ARCHITECTURE.md` with component diagram, data model, and three end-to-end flow diagrams (create task, run team, approval gate).
- `CHANGELOG.md` (this file) in Keep a Changelog 1.1.0 format.
- Issue and pull request templates under `.github/`.
- `Dockerfile` and `docker-compose.yml` for VPS deployment; image runs as a non-root user.
- GitHub Actions CI workflow: `ruff check`, `mypy`, and `pytest` on every push and pull request.
- Multi-LLM support via `LLMProvider` abstraction with Claude, OpenAI, and Ollama backends (see [ADR-001](docs/adr/0001-llm-provider.md)).
- Per-role provider/model selection through YAML frontmatter (`llm`, `model`, `temperature`, `max_tokens`) in `roles/*.md` (see [ADR-002](docs/adr/0002-role-format.md)).
- Configurable roles: load any `roles/<name>.md` without code changes; strict frontmatter validation with clear `RoleConfigError` messages.
- Role marketplace v0: import a role from a remote URL into the local `roles/` directory.
- UI for adding, editing, and deleting roles from the dashboard *Roles* page.
- Five example community roles shipped under `roles/examples/`: Product Manager, Designer, Security Auditor, Code Reviewer, Data Analyst.
- Per-role MCP tool allowlist (`tools:` field) — declarative allowlist enforced at subagent spawn.
- Unit and integration test suites under `mcp_сервер/tests/`, `дашборд/tests/`, and `smoke/tests/`.
- Coverage reporting via `pytest-cov`; baseline coverage threshold enforced in CI.
- `.pre-commit-config.yaml` wiring `ruff`, `mypy`, and `gitleaks` to run before every commit.
- Stress test for the kanban write path — eight concurrent writers against `fcntl` + `BEGIN IMMEDIATE`, asserts no lost updates and no `database is locked` errors.

### Changed

- Renamed Cyrillic source folders to Latin equivalents for cross-platform tooling:
  `роли/` → `roles/`, `дашборд/` → `dashboard/`, `команды/` → `commands/`, `мcp_сервер/` → `mcp_server/`.
- Launcher scripts renamed to Latin: `devboard-start.sh`, `devboard-work.sh`, and their Windows `.ps1`/`.bat` counterparts.
- Internal module imports and `pyproject.toml` package paths updated to match the new folder names.
- Default UI language is now English; Russian remains available via the in-app language switcher.
- Team Lead invocation goes through `create_provider()` instead of a hard-coded `claude --print` call.
- Role files now require explicit `schema_version: 1` frontmatter; existing roles migrated.
- Dashboard *Roles* page shows the new `name` / `description` / `llm` / `model` fields and the per-role tool allowlist.

### Fixed

- Race condition in `_atomic_modify` where a stale `fcntl` lock could persist after an abnormal exit; lock file is now cleaned up on startup.
- Stream-json parser no longer crashes on partial UTF-8 fragments split across SSE chunks.
- Backup thread now exits cleanly on `SIGTERM`; previously could leave a half-written `.backup` snapshot.

### Security

- `gitleaks` audit run against the full git history before the public release — no secrets leaked.
- `.env`, `.env.*`, and `*.key` patterns added to `.gitignore`.
- Docker image runs as a non-root user (`uid 1000`) with a read-only root filesystem where possible.
- Approval-gated operations (`git push`, `ssh`, `systemctl restart`, destructive shell commands) cannot be executed by subagents directly; they must go through the human approval flow documented in `approval_gates.md`.
- CI runs `gitleaks` and `pip-audit` on every pull request.
- All third-party LLM SDKs are imported lazily inside their provider modules so a user who does not need a given provider is not forced to install its dependencies.

<!--
When releasing:
1. Replace [Unreleased] with [X.Y.Z] - YYYY-MM-DD
2. Add an empty [Unreleased] section at the top with Added/Changed/Fixed/Security headings
3. Bump the version in setup.py / pyproject.toml
4. Create an annotated git tag vX.Y.Z and push it
5. Cut a GitHub release using the new section as the release notes body
-->
