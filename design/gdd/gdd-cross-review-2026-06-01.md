# Cross-GDD Review Report
Date: 2026-06-01
GDDs Reviewed: 11
Systems Covered: M0 Core Gameplay (Combat, Locomotion, Health, Enemy, Lock-On/Camera, Memory, Encounter, Input, Debug)

---

## Verdict: CONCERNS (Not Blocking)

- ✓ No blocking inconsistencies found
- ✓ No blocking design theory violations
- ⚠️ 3 advisory items identified (manageable, non-blocking)
- ✓ All ownership boundaries aligned
- ✓ All acceptance criteria consistent across GDDs
- ✓ Player fantasy coherent and unified
- ✓ Pillar alignment perfect (zero orphaned systems)

**Status**: M0 GDD design is sound and ready for architecture handoff. Advisory items should be resolved before final implementation tuning.

---

## Phase 2: Cross-GDD Consistency Review

**Verdict: PASS**

### 2a: Dependency Bidirectionality

✓ **PASS** — All critical dependencies are reciprocal and bidirectional:
  - Lock-On / Target Context ↔ Input Mapping
  - Lock-On & Combat Camera ↔ Lock-On / Target Context
  - All systems → Debug Overlay (reciprocated)
  - Combat Core ↔ Player Locomotion
  - Health / Damage ↔ Combat Core

⚠️ **WARNING: Async Initialization Pattern** — [Encounter Framework ↔ Lock-On / Target Context]
  - Lock-On / Target Context lists Encounter as upstream seeding dependency
  - Encounter Framework lists Lock-On as upstream dependency
  - This pattern is asymmetric but appears intentional (one-time initialization handoff)
  - **Recommendation**: If this becomes a common pattern across future systems, document it explicitly in architecture guide

⚠️ **WARNING: Documentation Gap** — [Player Locomotion]
  - Player Locomotion does not expose explicit Dependencies section
  - Relationships section references Input Mapping, Combat Core, Lock-On / Target Context but dependency list is incomplete
  - **Recommendation**: Add explicit Dependencies list for consistency with other M0 GDDs

### 2b: Rule Contradictions

✓ **PASS — Floor/Ceiling Rules** — Window timing rules (startup, active, recovery) consistent across:
  - Combat Core (owns windows)
  - Enemy Intent & Telegraph (uses identical window concepts)
  - Player Locomotion (respects window constraints)

✓ **PASS — Resource Ownership** — All primary resources owned uniquely:
  - Health: Health / Damage / Hit Reaction (owner)
  - CounterWindow: Combat Core (owner)
  - Reveal acceptance: Memory State (owner)
  - Telegraph: Enemy Intent & Telegraph (owner)
  - Target truth: Lock-On / Target Context (owner)
  - No conflicts detected

✓ **PASS — State Transitions** — Combat action state machine consistent:
  - Combat Core → Combat Action → Recovery → Locomotion Idle
  - Player Locomotion respects recovery constraints
  - Dodge recovery transitions aligned with ownership
  - Hit reaction state handoff explicit

✓ **PASS — Timing Assumptions** — All window types consistently named and defined:
  - Startup window
  - Active window
  - Recovery window
  - Parry window
  - Dodge window
  - Counter window
  - Telegraph window
  - No conflicting definitions

✓ **PASS — Stacking Rules** — Stacking constraints clear and consistent:
  - One active target max (Lock-On / Target Context)
  - One active duel max (Encounter Framework)
  - One simple enemy (Enemy Intent & Telegraph)

### 2c: Stale References

✓ **PASS — CounterWindow References** — CounterWindow referenced in:
  - Combat Core (owner, defines window)
  - Lock-On / Target Context (reads for readability context, does not own)
  - Memory State (reads for reveal request context, does not own)
  - Health / Damage / Hit Reaction (reads for consequence timing, does not own)
  - Player Locomotion (reads for recovery timing, does not own)
  - All references valid, ownership unambiguous

✓ **PASS — EnemyPunishWindow References** — EnemyPunishWindow referenced in:
  - Enemy Intent & Telegraph (owner, defines punish window)
  - Combat Core (reads to detect counter opportunity, does not own)
  - Health / Damage / Hit Reaction (reads for stagger classification, does not own)
  - Player Locomotion (reads for recovery context, does not own)
  - All references valid, ownership unambiguous

✓ **PASS — Reveal Request Pattern** — Reveal request chain:
  - Combat Core requests reveal (when meaningful validated context occurs)
  - Memory State accepts/rejects reveal (owns acceptance decision)
  - Memory VFX Response plays VFX (if accepted, presentation-only)
  - All elements exist, names match, behaviors align

### 2d: Data/Tuning Knob Ownership

✓ **PASS** — No two GDDs claim ownership of the same data or tuning knob:
  - Player health: owned by Health / Damage / Hit Reaction only
  - Enemy health: owned by Health / Damage / Hit Reaction only
  - Damage values: owned by Health / Damage / Hit Reaction only
  - Combat state: owned by Combat Core only
  - Movement state: owned by Player Locomotion only
  - Target focus state: owned by Lock-On / Target Context only
  - Telegraph timing: owned by Enemy Intent & Telegraph only
  - Parry eligibility: owned by Enemy Intent & Telegraph only
  - Counter window duration: owned by Combat Core only
  - Reveal acceptance: owned by Memory State only

### 2e: Formula Compatibility

✓ **PASS — Timing Compatibility** — Window formulas align across systems:
  - Combat Core window durations are compatible with Enemy Intent & Telegraph window definitions
  - Enemy attack active frames overlap with player hurtbox during valid hit window
  - All window input/output ranges are compatible

✓ **PASS — Damage/Reaction Compatibility** — Hit event types map cleanly to reaction categories:
  - Combat Core emits: LightHit, HeavyHit, CounterHit, EnemyHit, ParryStagger
  - Health / Damage / Hit Reaction consumes: LightHitReact, HeavyHitReact, CounterStagger, ParryStagger, EnemyHit
  - All mappings are clean and non-redundant
  - No range incompatibilities

⚠️ **WARNING — Counter Window Duration Variance** — [Combat Core + Player Locomotion]
  - **Open Design Question**: "Does counter window duration change if it came from dodge vs parry?"
  - **Current Status**: Unresolved design choice
  - **Risk**: If variance is implemented later, verify that acceptance criteria in Lock-On / Target Context, Player Locomotion, and Enemy Intent & Telegraph still support both cases
  - **Recommendation**: Resolve before implementation tuning begins. If variance is chosen, document the duration ratio in tuning contract.
  - **Status**: Not blocking (acceptance criteria remain compatible either way)

### 2f: Acceptance Criteria Cross-Check

✓ **PASS — Combat Validity Consistency**:
  - Combat Core: "target focus does not force attacks to hit"
  - Lock-On / Target Context: "target focus does not force attacks to hit"
  - Player Locomotion: "movement does not decide hit validity"
  - Consistent across all systems

✓ **PASS — Dodge/Parry Consistency**:
  - Combat Core: "parry succeeds only when timing is correct and attack is parry-eligible"
  - Enemy Intent & Telegraph: "enemies tag attacks ParryEligible or DodgePunishable"
  - Player Locomotion: "dodge and parry are movement expressions, not validity decisions"
  - Consistent across all systems

✓ **PASS — Reveal Acceptance Consistency**:
  - Memory State: "reveal only triggers from meaningful validated combat context"
  - Memory VFX Response: "VFX plays only after accepted Memory State context"
  - Combat Core: "Combat Core requests reveal context, Memory State decides acceptance"
  - Chain is logically consistent

✓ **PASS — Health/Defeat Consistency**:
  - Health / Damage / Hit Reaction: "damage applies only after confirmed Combat Core result"
  - Combat Core: "Combat Core owns hit resolution"
  - Memory State: "defeat does not trigger reveal without explicit Memory State acceptance"
  - Defeat ownership unambiguous

✓ **PASS — Debug Visibility Consistency**:
  - All 11 M0 GDDs specify debug visibility requirements
  - Debug Overlay lists 8 upstream dependencies matching all owning systems
  - No system claims exclusive debug access to another system's state

---

## Phase 3: Game Design Holism Review

**Verdict: PASS**

### 3a: Progression Loop Competition

✓ **PASS** — No system attempts to be primary progression driver:
  - Combat Core: core loop authority, not progression expansion
  - Player Locomotion: movement support, not progression
  - Health / Damage: consequence layer, not progression
  - Enemy Intent: telegraph clarity, not progression
  - All systems anchor to `read → evade/parry → counter → reveal`
  - All systems serve Combat As Interpretation as core identity
  - Zero competition detected

### 3b: Player Attention Budget

✓ **PASS** — Core loop requires exactly 4 simultaneous active layers:
  1. **Read enemy intent** — identify what enemy is committing to
  2. **Manage spacing + select defense** — choose dodge/parry based on threat
  3. **Execute parry/dodge timing** — commit to defensive answer with precise timing
  4. **Counter during window** — capitalize if counter window opens

Lock-On, Camera, and Memory are downstream responses (passive), not parallel active tracks:
  - Lock-On / Target Context: passive readability aid (does not require active decision)
  - Lock-On & Combat Camera: passive framing response (does not require active decision)
  - Memory State / Memory VFX: passive consequence response (does not require active decision)

**Result**: 4 active systems (within comfortable cognitive limit of 3-4). No cognitive overload detected.

### 3c: Dominant Strategy Detection

✓ **PASS** — No high-reward/low-risk strategy exists. All viable paths require reading correctly:
  - Counter strategy: requires earned setup (successful dodge/parry first) → high-risk, high-reward
  - Parry strategy: demands precise timing, fails if mistimed → high-risk, high-reward
  - Dodge strategy: requires spatial awareness and positioning → high-risk, moderate-reward
  - Heavy attack strategy: trades commitment for opening size → balanced risk/reward
  - All paths require interpreting enemy intent correctly
  - No skip shortcuts bypass the interpretive loop
  - Dominant strategy detected: None

### 3d: Economic Loop Analysis

✓ **PASS** — Single primary resource identified: **Control State** (player agency during recovery/action-lock)
  - **Sources**: recovery windows (safe to act), successful parry (defensive success), successful dodge (defensive success)
  - **Sinks**: hit reaction (temporary control suppression), action commitment (temporary action-lock)
  - **Loop**: Sources → Control Restoration → Sinks → back to Sources
  - **Characteristics**:
    - No infinite sources (all arise from valid gameplay events)
    - No sinks without recovery path (all lead to readable neutral return)
    - No positive feedback loops (counter opens opportunity window, but must re-read to capitalize; no automatic advantage escalation)
    - Balanced cycle: players experience tension (action-lock) → recovery → re-engagement
  - **Secondary notes**:
    - Health is failure boundary (M0 scope), not progression resource (intentional)
    - Stamina/Mana absent in M0 (explicitly deferred)
    - No economy imbalance detected

### 3e: Difficulty Curve Consistency

⚠️ **WARNING — Timing Ratio Risk** — [Enemy Intent & Telegraph + Combat Core]
  - **Issue**: Enemy punish window duration, telegraph clarity, and recovery timing are authored independently from Combat Core's counter-window narrowness and parry-window precision
  - **Risk**: If Telegraph expands enemy recovery windows while Combat Core tightens counter windows faster, difficulty spikes unpredictably for players reading correctly
  - **Example**: Enemy recovery might be 0.8s, Counter window 0.25s. If Telegraph is tuned to be more readable (longer), recovery extends to 1.0s. If Counter window is later tightened to 0.15s for feel, the ratio becomes unbalanced and counter feels inconsistent.
  - **Recommendation**: Establish published timing ratios as tuning contract:
    - Example: "counter window duration ≤ enemy recovery window × 0.35"
    - Example: "parry window duration ≤ enemy active frames × 0.6"
    - Publish these ratios in tuning knobs section before implementation iteration
  - **Severity**: Moderate (manageable through tuning contract, not blocking)

### 3f: Pillar Alignment

✓ **PASS** — All 11 M0 systems map cleanly to design pillars. Zero orphaned systems:

**Combat As Interpretation** (core pillar):
- Combat Core: "player interprets danger and responds"
- Enemy Intent & Telegraph: "readable enemy intent enables interpretation"
- Lock-On / Target Context: "target context supports focused interpretation"
- Player Locomotion: "movement supports interpretive rhythm"
- Input Mapping: "input intent routing supports explicit interpretation"
- Encounter Framework: "encounter structure enables duel interpretation"
- Debug Overlay: "debug visibility aids interpretation understanding"

**Melancholic Elegance**:
- Combat Core: "restrained, precise combat feel"
- Player Locomotion: "measured footwork, grounded control"
- Lock-On & Combat Camera: "stable, readable framing (not cinematic spectacle)"
- Enemy Intent & Telegraph: "emotional rhythm in threat, not chaotic pressure"
- Memory VFX Response: "brief, restrained visual response"
- Input Mapping: "deliberate input routing, not reactive spam"
- Debug Overlay: "clean, functional visibility"

**Personal Restoration Over Power Fantasy**:
- Combat Core: "success as regained fluency, not raw dominance"
- Health / Damage / Hit Reaction: "consequence as learning opportunity, not punishment"
- Memory State: "restore truth, not accumulate power"

**Distorted Memory Spaces**:
- Enemy Intent & Telegraph: "enemy behavior reflects emotional distortion"
- Memory State: "memory-state-aware response to restored truth"

### 3g: Player Fantasy Coherence

✓ **PASS** — All player fantasies converge on single unified identity:

**Unified Fantasy**: "I am reading emotional distortion through precise footwork and timing to restore fragmented truth."

**System-level fantasy breakdown**:
- Combat Core: "I interpret danger and respond with timing and precision"
- Player Locomotion: "I control measured spacing and footwork"
- Health / Damage / Hit Reaction: "I learn from failure and recover"
- Enemy Intent & Telegraph: "I recognize emotional rhythm in threat and commitment"
- Lock-On / Target Context: "I stay mentally focused on the emotional presence I'm confronting"
- Lock-On & Combat Camera: "I see the duel clearly without distraction"
- Memory State: "I recognize when my understanding shifts"
- Memory VFX Response: "I feel the fracture of false memory"
- Encounter Framework: "I engage this confrontation completely"
- Input Mapping: "I express my intentions clearly"
- Debug Overlay: "I understand the system's truthfulness"

**Result**: Zero conflicting identities. All systems reinforce same core fantasy of interpretive restoration through combat.

---

## Cross-System Scenario Walkthrough (Phase 4)

### Scenario 1: Enemy Attack → Parry → Counter Window

**Trigger**: Enemy enters committed attack sequence → player reads telegraph

**Activation order**:
1. Enemy Intent & Telegraph: emits telegraph signal, marks attack as ParryEligible
2. Combat Core: exposes parry window based on telegraph timing
3. Player presses parry input
4. Input Mapping: routes parry intent to Combat Core
5. Combat Core: validates parry input against active window
6. If valid → Combat Core: opens CounterWindow
7. Lock-On / Target Context: provides enemy direction context (passive)
8. Lock-On & Combat Camera: frames counter opportunity (passive)
9. Player presses counter input (if they recognize window)
10. Combat Core: validates counter input, emits hit event
11. Health / Damage / Hit Reaction: applies enemy stagger (if configured)
12. Combat Core: emits reveal request (if counter was meaningful)
13. Memory State: accepts/rejects reveal (conditional)
14. Memory VFX Response: plays response VFX (if accepted, passive)

**Data flow validation**: ✓ All outputs are valid inputs for downstream systems. No incompatibilities detected.

**Failure modes checked**:
- ✓ No race conditions (only one active parry/counter per frame)
- ✓ No feedback loops (counter opens window; must re-read to capitalize; no auto-advantage)
- ✓ No broken state transitions (all state changes explicit)
- ✓ No contradictory messaging (all systems in agreement on outcome)
- ✓ No compounding difficulty (counter difficulty is independent from attack difficulty)
- ✓ No reward conflicts (counter hit, parry success, and reveal are separate events)
- ✓ No undefined behavior (all rules specified)

**Verdict**: Scenario is sound. No interaction issues detected.

### Scenario 2: Player Defeated → Encounter Reset

**Trigger**: Player health reaches zero → Encounter Framework observes

**Activation order**:
1. Combat Core: detects valid enemy hit
2. Health / Damage / Hit Reaction: applies damage, reduces player health to 0
3. Health / Damage / Hit Reaction: emits defeat request
4. Player Locomotion: enters disabled state (movement restricted)
5. Encounter Framework: observes player health state
6. Encounter Framework: marks encounter as ended (player defeat)
7. Debug Overlay: displays defeat state
8. (Future) Reset input triggers Encounter Framework reset sequence

**Data flow validation**: ✓ Defeat ownership clear, no system interference.

**Failure modes checked**:
- ✓ No ambiguous ownership (Health owns defeat decision)
- ✓ No race conditions (health check happens once per damage event)
- ✓ No competing responses (only Encounter Framework manages encounter lifecycle)

**Verdict**: Scenario is sound. Reset pathway clear and explicit.

### Scenario 3: Successful Counter → Memory Reveal

**Trigger**: Player executes successful counter during meaningful combat exchange

**Activation order**:
1. Combat Core: validates counter input, emits CounterHit event + reveal request
2. Health / Damage / Hit Reaction: applies enemy stagger (if configured)
3. Memory State: evaluates reveal request against current memory context
4. If accepted → Memory State: emits accept signal
5. Memory VFX Response: observes accept signal, selects VFX response
6. Memory VFX Response: plays response (brief, non-interrupting)
7. Lock-On & Combat Camera: remains stable (does not react to memory response)
8. Encounter Framework: observes state remains in_active
9. Player can immediately re-read for next enemy action

**Data flow validation**: ✓ Reveal is separate from combat validity. Memory response does not interrupt duel rhythm.

**Failure modes checked**:
- ✓ No ambiguous authority (Combat Core requests, Memory State decides)
- ✓ No feedback loops (memory response is purely visual/consequential)
- ✓ No message conflicts (memory response != combat success; both are communicated clearly)
- ✓ No rhythm interruption (VFX is brief, duel continues)

**Verdict**: Scenario is sound. Memory integration successful without breaking combat readability.

---

## Summary of Issues

| Category | Count | Severity | Items |
|----------|-------|----------|-------|
| Blocking Inconsistencies | 0 | — | — |
| Blocking Design Issues | 0 | — | — |
| Warnings | 3 | Advisory | Async dependency pattern, Player Locomotion docs gap, counter timing ratios |
| Passes | 16+ | Clean | All ownership, rules, references, criteria, attention, fantasy, scenarios |

---

## GDDs Flagged for Advisory Follow-Up

| GDD | Issue | Type | Priority | Action |
|-----|-------|------|----------|--------|
| Player Locomotion | Missing explicit Dependencies section | Documentation | Low | Add Dependencies list listing Input Mapping, Combat Core, Lock-On / Target Context |
| Encounter Framework | Async initialization pattern | Documentation | Optional | Document pattern if it becomes template for future systems |
| Combat Core + Enemy Intent & Telegraph | Counter-window timing ratios unspecified | Design | Recommended | Publish timing ratios before implementation tuning (e.g., counter ≤ recovery × 0.35) |

---

## Recommended Actions

### Immediate (Before Implementation Tuning)
1. **Establish counter-window timing ratios** — Combat Core + Enemy Intent & Telegraph should define published ratio (e.g., counter window ≤ enemy recovery × 0.35) to prevent accidental difficulty spikes during tuning iteration

### Short-term (Before Production Handoff)
2. **Enhance Player Locomotion documentation** — Add explicit Dependencies section for consistency with other M0 GDDs

### Optional (For Future Reference)
3. **Document async initialization pattern** — If Encounter Framework ↔ Lock-On initialization pattern becomes template for future systems, document it explicitly in architecture guide

---

## Explicit Non-Goals

- No gameplay code changes
- No runtime behavior changes
- No deep system redesign
- No new RPG/map/inventory scope
- No architecture decisions (architecture review is separate)

---

## Next Steps

✓ **Ready for**: `/create-architecture` or `/architecture-review`
✓ **Ready for**: `/gate-check` (Systems Design phase)
✓ **Not ready yet**: Implementation tuning (resolve counter timing ratios first as advisory)

**Handoff recommendation**: Architecture can proceed. Timing ratio advisory should be resolved before final implementation tuning iteration begins.
