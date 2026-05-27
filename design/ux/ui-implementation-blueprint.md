# Glass Refrain — UI Implementation Blueprint

> **Status**: Blueprint (UX Review Approved, Pre-Code)
> **Author**: ux-designer + unity-ui-specialist (via team-ui skill)
> **Last Updated**: 2026-05-14
> **Version**: 1.0
> **Engine**: Unity 6000.3.x
> **UI Framework**: UI Toolkit
> **Execution Model**: Sequential work packages (WP1..WP8), not all-at-once

---

## Purpose

This document outlines the **implementation roadmap and architecture contracts** for Glass Refrain's foundational UI identity in Unity.
It defines the sequenced work, component responsibilities, data contracts, risks, and definition-of-done for Phase 3 (Implementation) so that code work remains aligned to approved UX and visual design.

---

## M0 Scope

- Foundational UI infrastructure only (not production screens)
- Work package sequencing and dependencies
- Component/service architecture map
- Data contract outlines (not code)
- Risk identification and mitigation
- Definition-of-done checklist
- No code implementation yet
- No UXML/USS templates yet
- No asset creation yet

---

## Non-Goals

- Do not write UI code
- Do not create UI Toolkit components
- Do not build specific screen layouts
- Do not implement accessibility UI yet
- Do not optimize performance yet
- Do not handle edge cases (deferred to implementation phase)

---

## Core Implementation Principles

1. **UI Observes Only** — UI consumes read-only state; gameplay owns truth
2. **Tokenized Styling** — USS tokens drive all visual/motion/accessibility variants
3. **Controller-First** — Gamepad navigation is the primary design surface; mouse/keyboard are parity additions
4. **Accessibility-Native** — Accessibility features are built-in, not bolted on
5. **Testability** — Architecture enables focused unit testing and integration regression matrix

---

## Sequenced Work Packages (WP1..WP8)

### WP1 — Contract Freeze & Scope Baseline

**Goal**: Lock all incoming UX and visual constraints before implementation begins.

**Tasks**:
- [ ] Finalize `design/ux/ui-identity.md` acceptance criteria
- [ ] Finalize `design/ux/interaction-patterns.md` measurable defaults (timings, buffering, contrast ratios)
- [ ] Finalize `design/ux/accessibility-requirements.md` baseline + enhanced tier scope
- [ ] Lock platform targets (16:9, 21:9 layouts)
- [ ] Define "UI observes state only" enforcement rules (no direct gameplay mutations from UI)
- [ ] Establish naming conventions for components, prefabs, and USS classes

**Definition of Done**:
- [ ] All three UX foundation docs are reviewed and approved
- [ ] Enforcement rules are documented as code review checklist
- [ ] Naming conventions are committed to style guide

---

### WP2 — Runtime UI Skeleton

**Goal**: Establish single-root UIDocument entry and foundational layer containers.

**Tasks**:
- [ ] Create `UIDocument_Root` prefab with PanelSettings
- [ ] Implement layer container hierarchy:
  - `ve-backdrop` (background/vignette)
  - `ve-screen-stack` (primary screen presentation)
  - `ve-hud-minimal` (persistent minimal HUD layer)
  - `ve-modal-layer` (modal dialogs)
  - `ve-transient-overlay` (toasts, transitions, subtitles)
- [ ] Define layer visibility rules and Z-ordering
- [ ] Implement non-blocking update cadence per layer
- [ ] Add debug layer container for dev overlays

**Definition of Done**:
- [ ] Single UIDocument root is the canonical entry point
- [ ] Layer containers are non-overlapping responsibility zones
- [ ] Layer visibility/disable behavior is deterministic and testable
- [ ] No unused containers; each has explicit purpose

---

### WP3 — Tokenized Theme System

**Goal**: Build USS token infrastructure for all visual, motion, and accessibility variants.

**Tasks**:
- [ ] Create root USS stylesheet with token definitions:
  - `--gr-color-*` (surface/accent/text token groups)
  - `--gr-type-*` (size/weight/family families)
  - `--gr-spacing-*` (padding/margin scale 8-based)
  - `--gr-surface-*` (frost/blur/opacity intensities)
  - `--gr-motion-*` (transition durations, easing)
  - `--gr-focus-*` (focus ring style, size, color)
- [ ] Create variant theme files:
  - `theme-default.uss` (baseline)
  - `theme-high-contrast.uss` (enhanced accessibility)
  - `theme-colorblind.uss` (color-vision safe)
  - `theme-reduced-motion.uss` (motion-free alternatives)
- [ ] Implement theme-switching service (runtime variant swap without reload)
- [ ] Document token semantics (what each token is for, not just its value)

**Definition of Done**:
- [ ] All tokens are defined and consistent across files
- [ ] Theme variants are tested for readability (contrast ratios verified)
- [ ] Theme switching works at runtime without flicker or errors
- [ ] Token documentation is clear enough for designers to use independently

---

### WP4 — Navigation, Focus, Modal Infrastructure

**Goal**: Implement gamepad-first focus routing and modal management.

**Tasks**:
- [ ] Implement `FocusManager` service:
  - Track current focus context
  - Restore last valid focus on layer return
  - Validate focus state (never null, always visible)
- [ ] Implement `ScreenStackService`:
  - Push/Pop/Replace/ClearTo screen operations
  - Coordinate focus restoration with transitions
- [ ] Implement `ModalManager` service:
  - Modal stack with depth enforcement (max 2)
  - Focus trap inside modal (focus never escapes)
  - Input consumption by layer (no bleed-through)
  - Restore prior focus on modal close
- [ ] Define explicit navigation graph per screen (focus order, wrap rules, override points)
- [ ] Implement input gating (120 ms buffers for Confirm/Cancel post-transition)
- [ ] Add edge-case handling: empty containers, nested modals, rapid open/close

**Definition of Done**:
- [ ] Focus is never null; always restorable
- [ ] Modal stack never exceeds depth 2
- [ ] Input consumption is deterministic (top layer always wins)
- [ ] Navigation graph is defined for all Phase 3 screens
- [ ] Unit tests cover focus edge cases and modal transitions

---

### WP5 — Presenter/Data Binding Foundation

**Goal**: Establish read-only data flow from gameplay state to UI.

**Tasks**:
- [ ] Define presenter lifecycle:
  - OnEnable: subscribe to state changes
  - OnDisable: unsubscribe cleanly
  - OnDestroy: cleanup
- [ ] Create presenter base class with state subscription pattern
- [ ] Establish data contract shapes (interfaces, read-only data objects)
- [ ] Implement localization integration (all UI text keys + formatting args, no raw strings)
- [ ] Define animation policy hooks (skippable, reduced-motion compliant)
- [ ] Add validation: UI cannot mutate gameplay state directly
- [ ] Create examples: simple read-only presenter binding pattern

**Definition of Done**:
- [ ] Presenter lifecycle is documented with code examples
- [ ] Data contracts are interface-only (no implementation dependencies)
- [ ] All UI text is localization-keyed
- [ ] Animation hooks are wired to accessibility settings
- [ ] Code review enforces UI → state observation boundary

---

### WP6 — Minimal Persistent HUD Presenter

**Goal**: Implement baseline HUD presenter for exploration state.

**Tasks**:
- [ ] Create `HudPresenter` service consuming read-only HUD data model
- [ ] Implement HUD state-visibility rules:
  - Exploration: max 4 persistent elements
  - Combat: reveal additional telemetry (max 6)
  - Low-health: add critical alert channel (max 7)
- [ ] Implement element visibility binding (show/hide based on state, not manual toggle)
- [ ] Create HUD layout zones (edge-anchored, minimal center coverage)
- [ ] Add threshold-based visual state changes (no gameplay logic in UI)
- [ ] Validate readability at all text-scale/contrast variants

**Definition of Done**:
- [ ] HUD respects element budgets per state
- [ ] Visibility rules are deterministic (not random/race-condition prone)
- [ ] Element count never exceeds documented budgets
- [ ] Readability validated at min/default/max text scales
- [ ] No gameplay state ownership in HUD

---

### WP7 — Subtitle Presenter + Accessibility Bridge

**Goal**: Implement subtitle presenter and plug in player accessibility settings.

**Tasks**:
- [ ] Create `SubtitlePresenter` consuming timed subtitle stream
- [ ] Implement subtitle safe-zone behavior (10% horizontal, 8% bottom margins)
- [ ] Implement subtitle priority/interrupt rules (queuing, dismissal, speaker labeling)
- [ ] Create `AccessibilitySettingsBridge` mapping player settings to token variants
- [ ] Wire accessibility toggle → theme swap (default ↔ high-contrast/colorblind/reduced-motion)
- [ ] Implement text-scale preset mapping (small/default/large → token values)
- [ ] Expose accessibility settings to UI layer (no direct gameplay dependency)
- [ ] Add motion intensity hooks for optional effects

**Definition of Done**:
- [ ] Subtitles respect safe zones and never overlap critical UI
- [ ] Subtitle timing is deterministic (no jitter)
- [ ] Accessibility setting changes apply immediately (no restart required)
- [ ] Theme variants load and render without flicker
- [ ] Accessibility settings persist across sessions

---

### WP8 — Validation & Hardening

**Goal**: Run full integration tests and finalize Phase 3 sign-off.

**Tasks**:
- [ ] Run UX threshold validation matrix (controller behavior, readability, accessibility)
- [ ] Stress-test modal stack (rapid open/close, nesting, interrupts)
- [ ] Stress-test focus restoration (open overlay → close → verify prior focus intact)
- [ ] Run accessibility validation (controller-only, keyboard-only, reduced-motion, contrast)
- [ ] Performance profile UI update cadence
- [ ] Regression test: repeated state changes without memory leaks
- [ ] Finalize integration review and sign-off

**Definition of Done**:
- [ ] All UX threshold checks pass (contrast, readability, input timing)
- [ ] Accessibility matrix fully passing
- [ ] No known regressions or blocker bugs
- [ ] Performance profile shows no surprises
- [ ] Phase 3 sign-off approved

---

## Component/Service Architecture

### UIRootComposition

**Owns**:
- Root `UIDocument` and PanelSettings
- All layer containers (backdrop, screen stack, HUD, modal, transient)
- Layer visibility orchestration

**Does Not Own**:
- Individual screen logic
- Focus management (delegates to FocusManager)
- Theme switching (delegates to ThemeTokenService)

### ScreenStackService

**Owns**:
- Screen lifecycle (Push/Pop/Replace/ClearTo)
- Screen transition state
- Focus coordinate with FocusManager

**Contracts**:
- Screen screens must be prefabs loaded additive-ready
- Each screen must expose enter/exit animation contract
- Each screen must communicate its initial focus target

### FocusManager

**Owns**:
- Current focus context (which element has focus)
- Focus restoration on layer transitions
- Focus validation (never null, always visible)

**Does Not Own**:
- Input routing (that's Layer/Modal Manager)
- Screen transitions

### ModalManager

**Owns**:
- Modal stack (depth cap: 2)
- Focus trap behavior (focus locked inside modal)
- Layer priority input consumption
- Modal lifecycle (open/close/dismiss)

**Contracts**:
- Modal must include explicit back/cancel path
- Modal focus trap is automatic (no manual implementation per modal)
- Child modals optional but always dismissible

### ThemeTokenService

**Owns**:
- Token definitions (USS custom properties)
- Theme variant loading and switching
- Runtime token value resolution

**Contracts**:
- Theme variants must be complete (no partial overrides)
- Switching does not require scene reload
- All visual elements use tokens (never hardcoded values)

### AccessibilitySettingsBridge

**Owns**:
- Player accessibility preferences (read-only)
- Mapping preferences to theme/tokens/behavior
- Exposing accessibility state to UI layer

**Contracts**:
- Settings are read-only from gameplay perspective
- Theme switching triggered by settings changes
- Motion sensitivity maps to reduced-motion toggle

### SubtitlePresenter

**Owns**:
- Subtitle rendering and lifecycle
- Safe-zone placement logic
- Speaker identification display
- Subtitle priority queue

**Contracts**:
- Consumes timed subtitle stream (read-only)
- Does not block gameplay
- Respects subtitle safe-zone rules

### HudPresenter

**Owns**:
- HUD element visibility binding
- HUD layout management
- State-to-visibility mapping

**Contracts**:
- Consumes read-only HUD data model
- Never owns or mutates gameplay state
- Respects element count budgets per state

---

## Data Contract Outline

All data contracts are **read-only interfaces/snapshots**. UI consumes only, never mutates.

### Screen State Read Model

```
IScreenState {
  ScreenId CurrentScreenId { get; }
  IReadOnlyList<ScreenId> AllowedTransitions { get; }
  bool IsModalOpen { get; }
  float TransitionProgress { get; }
}
```

### HUD Read Model

```
IHudState {
  float? PlayerHealth { get; }
  float? PlayerMaxHealth { get; }
  string ObjectiveText { get; }
  IReadOnlyList<IHudNotification> ActiveNotifications { get; }
  CriticalAlertState CriticalAlert { get; }
}
```

### Subtitle Read Model

```
ISubtitleStream {
  IObservable<SubtitleLine> OnSubtitleAppear { get; }
  IObservable<Unit> OnSubtitleDismiss { get; }
}

record SubtitleLine(
  string SpeakerKey,
  string TextKey,
  string[] FormattingArgs,
  float DurationSeconds,
  bool IsInterruptible
);
```

### Accessibility Settings Read Model

```
IAccessibilitySettings {
  TextScaleTier TextScale { get; }
  ContrastMode ContrastMode { get; }
  ColorblindMode ColorblindMode { get; }
  bool ReducedMotionEnabled { get; }
  float MotionIntensity { get; }
  bool InputHintsVisible { get; }
  IObservable<Unit> OnSettingsChanged { get; }
}
```

---

## Implementation Risks

### Risk 1: Focus Edge Cases During Rapid Transitions

**Description**: Opening/closing overlays rapidly may leave focus in invalid state.
**Mitigation**: Explicit focus validation logic; unit tests for open/close sequences.
**Owned By**: FocusManager implementation + QA.

### Risk 2: Theme Variant Drift

**Description**: High-contrast/colorblind/reduced-motion variants may diverge from baseline.
**Mitigation**: Token snapshot tests; visual checklist per variant; automated contrast validation.
**Owned By**: Visual design review + theme validation tests.

### Risk 3: Subtitle Timing Jitter Under Load

**Description**: Subtitle appear/dismiss timing may drift during stress.
**Mitigation**: Timestamp-driven presenter logic (not frame-based); idle frame budget.
**Owned By**: SubtitlePresenter implementation + perf profiling.

### Risk 4: Input Buffering Edge Cases

**Description**: Input buffers may retain stale commands during device switching or rapid state changes.
**Mitigation**: Buffer expiration + early consumption; input trace logging for debugging.
**Owned By**: Input system integration review + stress tests.

### Risk 5: UI Accidentally Depends on Gameplay Internals

**Description**: Presenter may directly reference gameplay implementation instead of read models.
**Mitigation**: Code review gate on UI → domain dependencies; interface-only contracts.
**Owned By**: Architecture review + code review checklist.

### Risk 6: Unity 6000.3.x API Behavior Differences

**Description**: UI Toolkit APIs may behave differently than assumed.
**Mitigation**: Validate all runtime APIs against pinned engine docs before final integration.
**Owned By**: unity-ui-specialist verification before WP8.

---

## Definition of Done (Phase 3 Completion)

Phase 3 is complete when ALL of the following are true:

- [ ] **WP1-WP8 all work packages completed** with sign-offs
- [ ] **Single root `UIDocument`** with layer containers implemented
- [ ] **Screen stack, focus manager, modal focus trap** fully functional
- [ ] **Explicit gamepad navigation** defined and tested for all Phase 3 screens
- [ ] **Tokenized USS theming** with approved visual identity + accessibility variants
- [ ] **HUD and subtitle presenters** integrated via read-only contracts
- [ ] **All UI text** uses localization pipeline (no hardcoded strings)
- [ ] **Motion is skippable** and reduced-motion preference is respected
- [ ] **UI audio** routed through audio event system (not direct playback)
- [ ] **UX thresholds validated**: controller behavior, readability, accessibility
- [ ] **"UI observes state only" verified** in architecture review
- [ ] **All accessible paths tested**: controller-only, keyboard-only, mouse-only, reduced-motion
- [ ] **No blocking regressions** or known accessibility violations
- [ ] **Phase 3 sign-off approved** by lead-programmer + ux-designer

---

## Success Criteria (How We Know Phase 3 Succeeded)

1. **Playable foundation exists** — a developer can boot the game and navigate menus with gamepad
2. **Accessibility is built-in** — all paths work with keyboard, gamepad, and mouse without retrofit
3. **Architecture is sound** — UI observes state, never owns gameplay truth
4. **Performance is acceptable** — UI update cadence does not spike frame time
5. **Identity is preserved** — UI feels calm, restrained, and tonally consistent
6. **Ready for content** — art-director and ui-programmer can build screens on top of this foundation

---

## Known Limitations (M0 to Address Before Vertical Slice)

- [ ] No player settings UI for accessibility (documented, not implemented)
- [ ] No advanced remapping UI (documented contracts, not implemented)
- [ ] No screen-reader integration (deferred)
- [ ] No full animation library (core motion patterns only)
- [ ] No production HUD (minimal prototype only)
- [ ] No persistent data for settings (session-only in M0)

---

## Risks

1. **Scope creep** if "UI foundation" expands to include production screens
2. **Performance surprise** if tokenized theming is unexpectedly expensive
3. **Unity 6000.3.x instability** if underlying engine APIs have bugs (mitigate with early profiling)
4. **Accessibility feature gap** if enhanced tier scope expands late (document cutoff clearly)

---

## Open Questions

1. Should theme switching be instant or fade-animated?
2. Should modal focus trap work for **all** modals or only blocking ones?
3. Should screen transitions have audio cues, or leave that to art director?
4. Should HUD density presets be player-customizable or system-determined?
5. Should input buffering be configurable for accessibility, or locked to defaults?

---

## Acceptance Criteria

- [ ] All WP definitions are clear and testable
- [ ] Component architecture is unambiguous
- [ ] Data contracts are interface-only (no implementation details leak)
- [ ] Risks are documented with mitigation assigned
- [ ] Success criteria are measurable and achievable
- [ ] Definition of Done is verifiable for Phase 3 completion
- [ ] No contradictions between UX foundation, visual spec, and implementation blueprint
