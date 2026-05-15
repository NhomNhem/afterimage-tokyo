# Glass Refrain — Interaction Pattern Library

> **Status**: Foundation (UX Review Approved)  
> **Author**: ux-designer (via team-ui skill)  
> **Last Updated**: 2026-05-14  
> **Version**: 1.0  
> **Engine**: Unity 6000.3.x  
> **UI Framework**: UI Toolkit  
> **Primary Input**: Gamepad-first, keyboard/mouse parity required

---

## Purpose

This library defines baseline **interaction patterns and behavioral contracts** for Glass Refrain player-facing UI.  
It standardizes input behavior, readability floors, disclosure rules, stress-state handling, and QA acceptance gates so interactions remain intuitive, accessible, and tonally coherent across all screens.

---

## M0 Scope

- Foundational interaction contracts (not per-widget implementation)
- Measurable controller defaults and readability floors
- HUD disclosure thresholds
- Stress-state and error handling behavior
- Accessibility baseline + QA validation checklist
- Not per-screen UX specs yet
- Not code implementation yet
- Not complete accessibility suite yet

---

## Non-Goals

- Do not specify individual screen layouts
- Do not implement code
- Do not create UI Toolkit components yet
- Do not design specific menu screens
- Do not solve platform-specific issues beyond contract defaults

---

## Global Contract Defaults (Controller Interaction)

### Focus Wrap Rules (Default)

- **Linear lists (vertical/horizontal)**: `Wrap = Off`
  - At boundary, focus remains on edge item
  - Edge feedback: 1 subtle nudge animation (80–120 ms) + optional soft tick SFX
- **Tab strips / carousels**: `Wrap = On`
  - Left from first moves to last; right from last moves to first
- **2D grids**: `Wrap = Off` by default
  - Optional per-row wrap allowed only when all rows are equal length
- **Radial selectors**: `Wrap = On` (continuous cycle expected by mental model)
- **Empty container behavior**: focus falls back to nearest valid parent control in ≤1 frame

### Hold-Repeat Timings (Default)

- **Initial hold delay**: `300 ms`
- **Repeat interval (standard nav)**: `90 ms`
- **Acceleration threshold**: after `1200 ms` continuous hold
- **Accelerated interval**: `60 ms`
- **Slider/stepper repeat interval**: `120 ms` per step
- **Boundary repeat behavior**: repeats are consumed but do not move focus; boundary feedback throttled to max 4/sec

### Input Buffering Windows (Default)

- **Confirm / Submit buffer**: `120 ms`
- **Cancel / Back buffer**: `120 ms`
- **Directional navigation buffer**: `0 ms` (no queued directional replay)
- **Context-appearance grace buffer** (new focusable appears after transition): `150 ms`
- **Post-close protection window** (ignore accidental double-close/close+confirm): `180 ms`
- **Buffer expiration rule**: expired buffered input is dropped silently (no late replay)

### Layer Conflict Resolution (Default)

Input is consumed by the highest active layer only.

Priority order (highest to lowest):
1. **Blocking system modal** (confirm dialogs, fatal errors, save prompts)
2. **Top-most modal panel**
3. **Non-blocking overlay panel** (codex/help/map overlay)
4. **Current screen root** (menu page / pause root)
5. **HUD context actions**
6. **Gameplay input context**

Rules:
- One input event → one consuming layer
- Lower layers never receive consumed input
- Modal stack depth hard cap: `2` (base modal + one child confirmation)
- Opening a higher layer auto-suspends lower-layer focus memory; closing restores last valid focus

---

## Readability Floors (Accessibility)

### Minimum Type Sizes (1080p reference, before user scaling)

- **Body text min**: `24 px`
- **Caption / helper text min**: `20 px`
- **Interactive labels min**: `22 px`
- **Subtitle text min**: `24 px`

Scaling:
- UI scale options must preserve these floors at all supported resolutions
- At 4K, sizes scale proportionally; never render below floor-equivalent legibility

### Contrast Targets by Token Group

- **Primary text / critical numerics / essential icons**: `≥ 7:1`
- **Standard body text / interactive labels**: `≥ 4.5:1`
- **Large display text (≥ 32 px)**: `≥ 3:1`
- **Non-text functional indicators (bars, focus rings, icons)**: `≥ 3:1`
- **Disabled state controls**: `≥ 3:1` against background + non-color cue (icon/state text/opacity + shape change)

### Maximum Line Length

- **Body copy max**: `68 characters` per line
- **Tooltip/help text max**: `56 characters` per line
- **Subtitle line max**: `42 characters` per line (2 lines max default)

### Subtitle Safe-Zone Behavior

- Subtitle block must remain inside:
  - `10%` horizontal safe margin from each side
  - `8%` bottom margin from screen edge
- If HUD/alerts overlap subtitle zone, subtitles auto-shift upward in fixed increments
- Subtitle reflow must avoid covering critical prompts and low-health alerts
- No subtitle placement may rely on color alone for speaker distinction

---

## Explicit Disclosure Thresholds (Anti-Clutter Operationalized)

### HUD Element Budget by State (Persistent Simultaneous Elements)

- **Exploration (low threat)**: max `4`
- **Combat (standard)**: max `6`
- **Combat (critical/low health)**: max `7` (includes one critical alert channel)
- **Pause/menu overlay active over gameplay**: gameplay HUD collapses to max `2` background essentials

If a new element would exceed budget, lowest-priority tertiary element is hidden first.

### Information Priority Bands

- **Primary**: required for immediate action/survival (health, lock-on target, core prompt)
- **Secondary**: useful but not always urgent (resource meter, stance/state tag)
- **Tertiary**: supportive/diagnostic/contextual (buff details, lore hint, controller education text)

### Tertiary Hide/Show Rules

- Tertiary elements default hidden during combat unless:
  - player opens details view, or
  - player fails same action `2` times within `10 s`, or
  - system detects new mechanic exposure window
- Tertiary tutorial hints auto-hide after `4 s` without input
- Tertiary blocks cannot appear while critical alert channel is active unless player explicitly expands info

---

## Stress-State Transition Behavior

### Error States

- Error feedback stack: **inline message + subtle audio cue + recovery action hint**
- No full-screen takeover for recoverable errors
- Error text persistence:
  - minor input error: `1.5 s`
  - action unavailable/context error: `2.5 s`
- Tone rule: avoid punitive language; use factual, restrained phrasing

### Interruptions (Context Swaps, Cut-ins, Forced Notices)

- Interruption entry transition: `120–180 ms`
- On interruption start:
  - consume current confirm input
  - freeze lower-layer focus
  - set focus to interruption's primary action
- On interruption end:
  - restore prior layer + last valid focus in ≤`1` frame

### Modal Stacking

- Hard cap stack depth: `2`
- Third modal request behavior: reject + queue request or collapse into current modal content
- Child modal must always include explicit back/cancel path

### Low-Health / Critical Alerts

- Use one dedicated critical channel only (no competing warning spam)
- Visual pulse frequency cap: `≤ 1 Hz`
- No flashing above accessibility safety thresholds
- Alert escalation:
  1. subtle persistent indicator
  2. gentle pulse + low-intensity audio cue
  3. optional haptic pulse (if enabled)
- When health recovers above threshold + hysteresis buffer, alert decays smoothly over `300–500 ms`

### Reduced-Motion Variant (Stress States)

- Replace scale/pulse animations with opacity or static icon state
- Disable camera-like UI drift and aggressive transitions
- Keep all timing semantics intact so interaction remains predictable

---

## Implementation Constraints (Handoff-Ready)

### MUST

- Support full controller-only traversal for every player-critical flow
- Use defined timing defaults unless section-specific exception is documented
- Maintain deterministic layer priority and single-consumer input routing
- Meet readability floors and contrast targets
- Provide reduced-motion path for all animated feedback in critical flows
- Preserve focus on open/close transitions and restore last valid focus on return

### MAY

- Add screen-specific focus wrap overrides when justified by control topology
- Use contextual tertiary reveal triggers beyond defaults if they do not break HUD budget
- Add subtle haptics/audio texture for stress feedback if disable toggles exist
- Use adaptive prompt text length as long as max line length rules are preserved

### NEVER

- Never require pointer/mouse hover to access critical actions
- Never communicate required state using color alone
- Never exceed modal stack depth cap
- Never replay expired buffered inputs
- Never use rapid flashing/strobing to signal urgency
- Never block recovery path behind secondary menus

---

## Canonical Examples (Art Director + UI Programmer)

### Example A — Pause Menu Vertical List (Controller)

- **Pattern**: Linear list, wrap off, boundary nudge feedback
- **Art Director handoff**: calm focus ring, restrained edge nudge, high-contrast selected state
- **UI Programmer handoff**: initial hold `300 ms`, repeat `90/60 ms`, confirm/cancel buffer `120 ms`, focus restore on submenu close

### Example B — Codex Entry with Progressive Disclosure

- **Pattern**: Primary summary visible; tertiary lore details hidden behind "Expand"
- **Art Director handoff**: clear hierarchy between summary and expanded layer; avoid clutter in default state
- **UI Programmer handoff**: tertiary block toggled by explicit action; auto-collapse on exit; line length caps enforced in text container

### Example C — Low-Health Alert During Combat + Modal Interrupt

- **Pattern**: critical channel active, then interruption modal appears
- **Art Director handoff**: low-health indicator remains unsettling but restrained; modal remains readable and dominant
- **UI Programmer handoff**: modal consumes input by layer priority, freezes HUD interactions, restores prior focus and alert state after close

---

## Validation Checklist (Pass/Fail QA Mapping)

| Section | Pass Criteria | Fail Criteria |
|---|---|---|
| Controller Contract Defaults | Focus behavior, repeat timings, and buffers match documented values within tolerance ±20 ms | Inconsistent timings, random wrap behavior, or nondeterministic focus restoration |
| Layer Conflict Resolution | Top active layer always consumes input; no bleed-through; modal depth never exceeds 2 | Input triggers lower layer while modal active; stack depth >2 |
| Readability Floors | Type floors met at all supported resolutions; line length limits respected | Any critical text below floor or over-length causing truncation without fallback |
| Contrast Targets | Token groups meet ratio targets; non-color cues present for functional states | Required info distinguishable only by hue/saturation |
| Disclosure Thresholds | HUD visible element count stays within state budgets; tertiary info follows trigger rules | Persistent clutter exceeds budget; tertiary appears unprompted in critical states |
| Stress-State Behavior | Error/interruption/modal/critical alerts follow timing and tone rules | Harsh/frenetic feedback, missing recovery path, or alert spam conflicts |
| Accessibility — Controller Only | Full start-to-exit critical flow possible on controller with no dead-ends | Any critical flow requires mouse/touch/keyboard fallback |
| Accessibility — Reduced Motion | All critical animations have reduced-motion equivalents; no excessive flashes | Reduced-motion toggle leaves key feedback missing or retains high-intensity motion |
| Accessibility — Subtitles | Safe-zone rules hold under HUD overlap; subtitle readability maintained | Subtitle overlap with critical UI or out-of-safe-zone clipping |
| Regression Stability | Reopen/close overlays repeatedly without focus loss or duplicate input side effects | Focus null states, accidental double-submit, or stale buffered actions replayed |

---

## QA Execution Notes (Required Test Modes)

1. **Controller-only test pass** (no mouse interaction allowed)
2. **Reduced-motion enabled pass** (stress sequences + combat UI)
3. **Low-vision/readability pass** (minimum scale, max HUD density state)
4. **Interrupt storm pass** (rapid modal open/close, errors, critical alerts)

---

## Change Control

Any deviation from this library (timings, budgets, readability floors, or layer rules) must include:
- rationale
- impacted screens/flows
- accessibility impact note
- QA test additions

This preserves interaction trust while allowing intentional exceptions.

---

## Risks

1. **Timing drift** if implementation doesn't mirror ±20 ms tolerances documented here
2. **Focus edge cases** during rapid open/close/interrupt sequences
3. **Tertiary info discoverability** — auto-hide rules may suppress helpful context
4. **Reduced-motion parity** — ensuring all critical feedback works without motion
5. **Cross-platform input buffering** — ensuring console and PC feel identical

---

## Open Questions

1. Should hold-repeat timings be different for menus vs HUD navigation?
2. Is tertiary auto-reveal on "2 failures within 10s" the right learning curve, or should it be configurable?
3. Should modal stack depth ever allow depth > 2 for advanced scenarios?
4. How should input buffering behave during async data loads or network latency?
5. Are there game-specific stress states (e.g., boss phase transitions) that need special UX handling?

---

## Acceptance Criteria

- [ ] All controller defaults are documented with specific numeric values
- [ ] Layer conflict resolution is unambiguous and testable
- [ ] Readability floors are measurable (specific px sizes, contrast ratios)
- [ ] HUD disclosure budgets are enforced by state
- [ ] Stress-state behavior is defined for all common scenarios
- [ ] No contradictions between different sections
- [ ] Implementation notes are actionable for art-director, unity-ui-specialist, and ui-programmer
- [ ] QA checklist is executable without referring back to design docs
- [ ] All risks are documented with mitigation strategies assigned
