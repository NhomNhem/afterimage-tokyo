Dưới đây là **workflow/skills chuẩn** cho project `Glass Refrain / afterimage-tokyo`. Mình viết dạng có thể copy vào `AGENTS.md`, `CLAUDE.md`, hoặc `docs/workflows/agent-workflow.md`.

---

# Glass Refrain — Agent Workflow & Skills

## 0. Core rule

```txt
OpenSpec defines what should change.
Skills define how agents work.
AgentMemory keeps context.
Superpower accelerates command usage.
Coding agents implement.
Review/gate decides whether it is accepted.
```

Không paste prompt trần cho task lớn. Với story/runtime/architecture work, luôn đi theo workflow:

```txt
OpenSpec
→ AgentMemory
→ Skill/Superpower command
→ Coding implementation
→ Smoke evidence
→ Evidence review
→ Code review
→ Gate check
→ Story done / OpenSpec archive
→ AgentMemory update
```

Repo `Claude-Code-Game-Studios` có sẵn nhóm skills cho Stories & Sprints như `/create-epics`, `/create-stories`, `/dev-story`, `/sprint-plan`, `/sprint-status`, `/story-readiness`, `/story-done`, và nhóm review/QA như `/code-review`, `/gate-check`, `/smoke-check`, `/test-evidence-review`. 

---

# 1. Tool responsibility map

## OpenSpec — Source of truth

Dùng cho:

```txt
- change-id
- proposal
- design/spec delta
- tasks
- acceptance criteria
- validation evidence
- archive history
```

Ví dụ hiện tại:

```txt
openspec/changes/create-m0-playable-combat-prototype-scene
```

Không để agent tự mở rộng scope ngoài OpenSpec change đang active.

---

## Claude-Code-Game-Studios Skills — Studio workflow

Dùng cho:

```txt
- tạo epic/story
- kiểm tra readiness
- dev story
- smoke check
- code review
- gate check
- story done
- sprint status
- tech debt
```

Repo này được thiết kế theo mô hình collaborative, không autonomous: agent hỏi, đưa option, user quyết định, draft, rồi mới approve. 

---

## Superpower — Command accelerator

Dùng để:

```txt
- chạy skill nhanh hơn
- chuẩn hoá prompt context
- tránh paste prompt thủ công dài mỗi lần
- gọi đúng routine/command trong Claude Code
```

Rule:

```txt
Nếu có skill/command phù hợp, dùng skill/command trước.
Prompt chỉ bổ sung context, không thay thế workflow.
```

---

## AgentMemory — Persistent context

Dùng để nhớ:

```txt
- current milestone
- current active OpenSpec change
- project rules
- forbidden patterns
- technical decisions
- latest verified status
- known blockers
```

AgentMemory không thay thế OpenSpec.

Không dùng AgentMemory làm source of truth cho:

```txt
- acceptance criteria chính thức
- story completion
- release/archive status
```

---

## ChatGPT / Codex

Dùng cho:

```txt
- architecture review
- prompt/brief writing
- decision review
- risk analysis
- code review reasoning
- workflow/gate judgment
```

---

## Windsurf / OpenCode

Dùng cho:

```txt
- implementation
- scene/code edits
- running tests
- producing reports/evidence
```

---

# 2. Workflow A — New milestone / big system

Dùng khi bắt đầu một mảng lớn mới:

```txt
Examples:
- M0 First Playable Duel
- Vertical Slice Tokyo District
- Combat Feel Polish
- Production Animation Pipeline
- Boss Duel Framework
```

Flow:

```txt
1. OpenSpec propose
2. /create-epics
3. /create-stories
4. /sprint-plan
5. /story-readiness
6. /dev-story
7. /smoke-check
8. /test-evidence-review
9. /code-review
10. /gate-check
11. /story-done
12. OpenSpec archive
13. AgentMemory update
```

Template:

```txt
OpenSpec:
Create or update change/spec for: <system-or-milestone>

Run:
/create-epics <project-or-milestone>
/create-stories <epic-id>
/sprint-plan <sprint-id>

Constraints:
- Keep scope aligned with OpenSpec.
- Do not implement before story readiness.
- Do not skip review/gate.
```

---

# 3. Workflow B — Existing story/change implementation

Dùng khi epic/story đã có, nhưng chưa implement.

Flow:

```txt
1. AgentMemory load current context
2. /story-readiness <change-id>
3. /dev-story <change-id>
4. /smoke-check <change-id>
5. /test-evidence-review <change-id>
6. /code-review <change-id>
7. /gate-check <change-id>
8. /story-done <change-id>
9. OpenSpec archive
10. AgentMemory update
```

Template:

```txt
/story-readiness <change-id>

Context:
- Current milestone: <milestone>
- Current story: <story>
- Current constraints: <rules>
- Known blockers: <blockers>

Return:
- READY / NOT READY
- missing decisions
- dependencies
- scope risks
```

Then:

```txt
/dev-story <change-id>

Implement only the approved OpenSpec/story scope.

Forbidden:
- scope creep
- hidden fallback
- unrelated refactors
- direct UnityEngine.Debug.Log
- runtime FindObjectOfType/GameObject.Find
- presentation mutating gameplay truth

Output:
- files changed
- tests run
- evidence
- remaining blockers
```

---

# 4. Workflow C — Bug / regression / scene verification

Dùng cho task hiện tại.

Flow:

```txt
1. /smoke-check <change-id>
2. Fix only the blocker
3. PlayMode evidence
4. /test-evidence-review <change-id>
5. /code-review <change-id>
6. /gate-check <change-id>
```

Không cần `/create-epics`. Không cần `/dev-story` nếu bug chỉ là wiring/verification trong active change.

Current task:

```txt
/smoke-check create-m0-playable-combat-prototype-scene
```

Prompt:

```txt
Use OpenSpec change:
create-m0-playable-combat-prototype-scene

Use AgentMemory context:
- Current milestone: M0 First Playable Duel — Phase 1 Visible Playable Prototype.
- Current blocker: GameplayLifetimeScope.loopDriver is null at runtime.
- Enemy loop cleanup has removed fallback/reflection.
- M0EnemyIntentLoopDriver.Tick(float) should be called by M0GameplayTickHandler.Update().
- Do not start Story 1-7.
- Do not start Animancer implementation.

Task:
Manually assign Loop Driver in GameplayLifetimeScope to:
Enemy_M0TargetablePlaceholder / M0EnemyIntentLoopDriver

Then run PlayMode smoke verification.

Forbidden:
- FindObjectOfType
- FindAnyObjectByType
- GameObject.Find
- reflection-based injection
- direct UnityEngine.Debug.Log / LogWarning / LogError
- CombatCore rule changes
- InputActionAsset binding changes
- Story 1-7 implementation
- Animancer implementation

Expected:
- no loopDriver InvalidOperationException
- enemy transitions Idle -> Telegraph -> Commit -> Active -> Recovery -> Idle
- Debug Overlay enemyState no longer stays Idle
- F6 calls real IEnemyDebugHarness
- F6 -> Q -> wait Neutral -> E passes

Output:
- PASS / FAIL
- scene reference fixed: yes/no
- enemy loop restored: yes/no
- F6 real harness: yes/no
- Story 1-6 pass: yes/no
- logs/evidence
- files changed
- confirm no forbidden fallback was added
```

Lý do hiện tại chưa nên nhảy Story 1-7: validation report trước đó khuyến nghị hoàn tất PlayMode verification cho `create-m0-playable-combat-prototype-scene`, code review, archive change này rồi mới tới `wire-m0-health-hit-reactions`. 

---

# 5. Workflow D — Smoke evidence review

Sau khi có log/report:

```txt
/test-evidence-review <change-id>
```

Template:

```txt
/test-evidence-review create-m0-playable-combat-prototype-scene

Review the PlayMode evidence.

Confirm:
- no bootstrap error
- Game View renders
- Player visible
- Enemy visible
- WASD movement visible
- attack states visible/logged
- enemy intent transitions visible/logged
- debug overlay visible
- debug overlay values update
- F6 reaches real debug harness
- F6 -> Q -> wait Neutral -> E passes
- no gameplay errors
- no forbidden API findings
- no scope creep

Return:
APPROVED / INSUFFICIENT EVIDENCE / FAIL

Also list:
- missing evidence
- risky assumptions
- required reruns
```

The current visible prototype exit criteria is that the player can be controlled and observed in Game View without relying only on console logs. 

---

# 6. Workflow E — Code review

Sau smoke evidence pass:

```txt
/code-review <change-id>
```

Template:

```txt
/code-review create-m0-playable-combat-prototype-scene

Focus:
- No FindObjectOfType / FindAnyObjectByType / GameObject.Find.
- No reflection injection.
- No direct UnityEngine.Debug.Log / Warning / Error in project-owned code.
- Explicit serialized references only.
- Missing required scene references fail fast.
- M0EnemyIntentLoopDriver.Tick(float) is called from M0GameplayTickHandler.Update().
- IEnemyDebugHarness points to the same loop driver instance.
- Debug Overlay is read-only.
- Visual feedback is read-only.
- CombatCore rules unchanged.
- InputActionAsset bindings unchanged.
- No Story 1-7 Health implementation.
- No Memory Reveal implementation.
- No Animancer implementation/root motion authority.
- No input architecture refactor.

Return:
APPROVED / APPROVED WITH SUGGESTIONS / CHANGES REQUIRED / FAIL

Include:
- blockers
- architecture risks
- scope creep findings
- scene/prefab wiring assessment
- whether ready for gate-check
```

Presentation systems must observe gameplay state and must not own gameplay truth; M0’s priority list also treats Combat Core, Enemy Intent, Memory State, and Encounter Framework as bottleneck systems that many others depend on. 

---

# 7. Workflow F — Gate check

Sau code review:

```txt
/gate-check <change-id>
```

Template:

```txt
/gate-check create-m0-playable-combat-prototype-scene

Decide whether this OpenSpec change can be completed/archived.

Required:
- PlayMode smoke evidence approved.
- Code review approved.
- No bootstrap errors.
- No forbidden APIs.
- No fallback dependency lookup.
- No direct Unity debug logs.
- Visible prototype criteria met.
- No scope creep into Story 1-7 / Animancer / Memory Reveal.

Return:
PASS / PASS WITH NOTES / BLOCKED / FAIL

If PASS:
- list final evidence
- list known deferred items
- state whether ready for /story-done and OpenSpec archive

If BLOCKED:
- list exact blocker
- next minimal task
```

---

# 8. Workflow G — Story done / archive

Chỉ chạy khi gate pass.

```txt
/story-done <change-id>
```

Then:

```txt
OpenSpec archive <change-id>
AgentMemory update current status
```

Template:

```txt
/story-done create-m0-playable-combat-prototype-scene

Close only if:
- /test-evidence-review approved
- /code-review approved
- /gate-check passed
- OpenSpec tasks/evidence updated
- known deferred items documented

Do not mark unrelated stories done.
Do not update sprint status beyond evidence.
```

---

# 9. Workflow H — Sprint status reconciliation

Dùng khi sprint tracker/docs lệch nhau.

```txt
/sprint-status
/consistency-check
```

Template:

```txt
/sprint-status sprint-1

Reconcile:
- OpenSpec active/archive changes
- story markdown
- production/sprint-status.yaml
- production/sprints/sprint-1.md
- latest PlayMode/test evidence

Do not trust stale status claims without fresh evidence.

Return:
- current status table
- mismatches
- proposed status updates
- evidence level
- next action
```

Sprint validation đã phát hiện nhiều mismatch: sprint YAML stale, active playable prototype còn nhiều task chưa check, và chưa có fresh PlayMode run. 

---

# 10. Workflow I — Tech debt / architecture rule update

Dùng khi phát hiện anti-pattern như fallback DI.

```txt
/tech-debt
/architecture-decision
/architecture-review
```

Template:

```txt
/tech-debt runtime-di-fallback-rule

Context:
We found runtime fallback lookup used to hide broken DI/scene references.

Rule:
Runtime gameplay code must not use:
- FindObjectOfType
- FindAnyObjectByType
- GameObject.Find
- Resources.Load as dependency resolver
- reflection-based injection

Required:
- explicit serialized references
- VContainer registration
- fail-fast InvalidOperationException for required missing references

Output:
- debt item
- owner
- risk
- enforcement checklist
- suggested ADR/rule update
```

---

# 11. Workflow J — Animancer / animation work

Không dùng trước khi visible prototype pass. Khi bắt đầu animation:

```txt
/story-readiness story-1-11-animator-adapters
/dev-story story-1-11-animator-adapters
```

Template:

```txt
/story-readiness story-1-11-animator-adapters

Context:
Animancer Pro is preferred runtime animation playback layer, but it must stay behind project-owned services/drivers.

Check:
- Enemy loop verified?
- Story 1-6 defensive loop verified?
- Visible prototype pass?
- Animation scope limited to presentation-only observer?

Return:
READY / NOT READY
```

Implementation prompt:

```txt
/dev-story story-1-11-animator-adapters

Implement minimal Animancer M0 Presentation Adapter.

Rules:
- Do not call Animancer directly from CombatCore, Input, EnemyIntentModel, domain services, or ability logic.
- Use project-owned animation services/drivers.
- Gameplay sends typed animation requests/intents.
- Animation chooses clip/transition/fade/layer.
- Animation must not apply damage.
- Animation events must not open CounterWindow or mutate gameplay truth.
- Root motion disabled by default.
- No FindObjectOfType/GameObject.Find fallback.
- No direct UnityEngine.Debug.Log.
- Missing clips/transitions must produce clear NhemLogger error.

Acceptance:
- Player Idle/Locomotion/LightAttack/HeavyAttack/Dodge/Parry/Counter visible.
- Enemy Telegraph/Active/Recovery visible.
- Disabling animation does not break gameplay state.
```

Animancer brief đã chốt rõ: Animancer Pro là playback layer ưu tiên, nhưng gameplay không phụ thuộc trực tiếp vào Animancer; intent đi qua project-owned animation service/driver. 

---

# 12. Current M0 recommended sequence

Tại thời điểm hiện tại:

```txt
1. /smoke-check create-m0-playable-combat-prototype-scene
2. Fix Loop Driver scene reference manually.
3. Verify enemy loop.
4. Verify F6 real harness.
5. Verify F6 -> Q -> wait Neutral -> E.
6. /test-evidence-review create-m0-playable-combat-prototype-scene
7. /code-review create-m0-playable-combat-prototype-scene
8. /gate-check create-m0-playable-combat-prototype-scene
9. /story-done create-m0-playable-combat-prototype-scene
10. OpenSpec archive.
11. AgentMemory update.
12. Then validate Story 1-7 or Story 1-11-lite depending on visible needs.
```

Strict next-sequence docs also say: finish PlayMode verification for `create-m0-playable-combat-prototype-scene`, code review, complete/archive, then validate/apply Story 1-7. 

---

# 13. Skill selection cheat sheet

| Situation                          | Use                                                    |
| ---------------------------------- | ------------------------------------------------------ |
| Start a new milestone              | `/create-epics`                                        |
| Break epic into stories            | `/create-stories`                                      |
| Plan sprint                        | `/sprint-plan`                                         |
| Check story before coding          | `/story-readiness`                                     |
| Implement approved story           | `/dev-story`                                           |
| Verify scene/runtime behavior      | `/smoke-check`                                         |
| Review logs/screenshots/test proof | `/test-evidence-review`                                |
| Review code and architecture       | `/code-review`                                         |
| Decide pass/block/fail             | `/gate-check`                                          |
| Close story                        | `/story-done`                                          |
| Reconcile stale trackers           | `/sprint-status`, `/consistency-check`                 |
| Record architectural debt          | `/tech-debt`, `/architecture-decision`                 |
| Multi-domain implementation        | `/team-combat`, `/team-ui`, `/team-qa`, `/team-polish` |

---

# 14. Project rules included in every prompt

```txt
Project rules:
- Use Unity 6000.3.x.
- Use Unity New Input System.
- Use VContainer.
- Use NhemLogger/NhemLogging, not direct UnityEngine.Debug.Log.
- No runtime FindObjectOfType / GameObject.Find fallback.
- No reflection-based injection.
- Missing required dependencies fail fast.
- Presentation is read-only.
- CombatCore owns combat authority.
- Debug Overlay must not mutate gameplay truth.
- Animation/Animancer must not mutate gameplay truth.
- Root motion disabled unless explicitly approved.
- Debug defines must not alter gameplay truth.
```

---

# 15. One-line workflow

```txt
OpenSpec decides scope → AgentMemory loads context → Skill/Superpower runs process → Coding agent edits → Smoke proves runtime → Evidence review checks proof → Code review checks architecture → Gate decides → Story done/archive → Memory updates.
```
