# Glass Refrain — Accessibility Requirements

> **Status**: Foundation (UX Review Approved)  
> **Author**: ux-designer + accessibility-specialist (via team-ui skill)  
> **Last Updated**: 2026-05-14  
> **Version**: 1.0  
> **Engine**: Unity 6000.3.x  
> **Committed Tier**: Enhanced (Basic + Standard + Extended Support)

---

## Purpose

This document defines Glass Refrain's **accessibility baseline and enhanced targets** for all player-facing UI, gameplay systems, and content.  
It ensures that the widest possible audience can engage with the game's emotional core, duel mechanics, and mystery narrative. Accessibility is a **design-first commitment**, not a post-ship fix.

---

## M0 Scope

- Baseline accessibility contracts for foundational UI
- Commitment levels (baseline must-pass, enhanced targets, stretch goals)
- Controller-first design with keyboard/mouse parity
- Readability and contrast baselines
- Reduced-motion support direction
- Subtitle and localization baseline
- Documentation of known M0 gaps (deferred to Vertical Slice or Alpha)

---

## Non-Goals

- Do not implement accessibility code yet
- Do not create full UI Toolkit theme variants in M0
- Do not build player settings UI in M0
- Do not profile performance for accessibility features in M0
- Do not create full test matrix in M0

---

## Committed Accessibility Tier: Enhanced

### What This Means

**Glass Refrain commits to the "Enhanced" accessibility tier**, which includes:
- All "Baseline" requirements (must-pass for any screen)
- All "Standard" requirements (keyboard/controller parity, motor accessibility, audio alternatives)
- Extended support for specialized input/output needs (remapping, text scaling, colorblind modes, extended subtitles)

### Tier Progression

| Tier | Scope | Commitment |
|------|-------|------------|
| **Baseline** | Core usability; controller+keyboard support; readable text; no color-only state | **MUST PASS** all screens |
| **Standard** | Keyboard full parity; focus clarity; contrast floors; motor accessibility | **MUST PASS** by Vertical Slice |
| **Enhanced** | Remapping; text scaling; high-contrast mode; colorblind variants; extended subtitles | **TARGET** by Vertical Slice; ship in Alpha |
| **Comprehensive** | Screen reader support; full voice control; braille display bridging | Deferred to post-launch updates |

---

## Baseline Requirements (MUST PASS)

These are non-negotiable for any shipped screen.

### Controller & Keyboard Support

- [ ] Every interactive screen is **fully operable via gamepad only**
- [ ] Every interactive screen is **fully operable via keyboard only**
- [ ] Every interactive screen supports **mouse input** (when applicable to genre)
- [ ] Focus order is **explicit and predictable** (documented in per-screen UX specs)
- [ ] No dead-end focus nodes (always a way forward and back)
- [ ] Back/Cancel action is **globally consistent** and always available
- [ ] Initial focus is **visible and context-safe** (never on a destructive action)

### Readability & Type

- [ ] **Body text minimum**: 24 px @1080p (scales proportionally at higher resolutions)
- [ ] **Captions minimum**: 20 px @1080p
- [ ] **Interactive labels**: 22 px @1080p
- [ ] **Line length max**: 68 characters for body, 56 for tooltips, 42 for subtitles
- [ ] No required text rendering below minimum sizes
- [ ] Fonts are readable at all target resolutions and aspect ratios (16:9, 21:9)

### Contrast & Color

- [ ] **Primary text on active background**: ≥ 7:1 contrast ratio (WCAG AAA)
- [ ] **Standard body text**: ≥ 4.5:1 contrast ratio (WCAG AA)
- [ ] **Large display text** (≥32 px): ≥ 3:1 contrast ratio (WCAG AA for large text)
- [ ] **Non-text UI indicators** (bars, focus rings): ≥ 3:1 contrast ratio
- [ ] **No color-only state signaling** — all states use color + shape, icon, or text
- [ ] **Colorblind-safe palette** — primary UI uses non-red/green distinction where possible
- [ ] Disabled state is indicated by shape/opacity change + text label, never color alone

### Subtitles & Audio

- [ ] **All dialogue has subtitles** (no audio-only narrative)
- [ ] **Subtitles max 2 lines** by default (3 lines if player adjusts settings)
- [ ] **Subtitle safe zone** enforced (10% horizontal margin, 8% bottom margin from edge)
- [ ] **Subtitles support Latin + CJK languages** without truncation
- [ ] **Speaker identification** uses text label (never color-only)
- [ ] **Audio description option** for critical cutscene/lore moments (deferred M0)

### Motion & Flashing

- [ ] **No hazardous flashing** (>3 flashes/sec at >25% screen coverage)
- [ ] **Motion sensitivity warning** in first-launch flow (if any distortion overlays used)
- [ ] **Reduced-motion mode available** in settings (toggle all non-critical motion off)
- [ ] **Critical information is not motion-dependent** (e.g., health status visible without animation)

### Focus & Navigation

- [ ] **Focus indicator always visible** (never disappears, never becomes unclear)
- [ ] **Focus indicator has sufficient size & contrast** (≥3 px outline, ≥3:1 ratio vs background)
- [ ] **No focus traps** (infinite loop focus states)
- [ ] **Tab order matches visual reading order** (left-to-right, top-to-bottom)
- [ ] **Modal focus lock works predictably** (focus trapped inside modal, restored on close)

### Error Handling

- [ ] **All error messages are text-based** (not icon-only)
- [ ] **Errors explain what happened and how to recover** (not just "Error")
- [ ] **No time-limited dismissal** of critical errors (player must act to close)
- [ ] **Error state is recoverable** (never locks out all actions)

---

## Standard Requirements (MUST PASS by Vertical Slice)

These enable deeper engagement for players with diverse physical, sensory, and cognitive needs.

### Input Method Parity

- [ ] **Keyboard has equivalent action for every gamepad action**
  - D-pad up/down = Tab/Shift+Tab (or arrow keys)
  - D-pad left/right = alternative nav where applicable
  - Confirm = Enter or Space
  - Cancel = Esc or Backspace
- [ ] **Mouse support does not create exclusive affordances**
  - All mouse-hover content is also available via focus
  - No click-only actions without keyboard/gamepad equivalent
- [ ] **Input device switching is seamless** (switching gamepad to keyboard mid-screen doesn't break focus)

### Motor Accessibility

- [ ] **Hold/Repeat defaults are documented** (300 ms initial, 90 ms repeat)
- [ ] **No double-tap requirements** (use single actions where possible)
- [ ] **No time-critical inputs required** for critical paths (extended time is OK if settings allow)
- [ ] **Confirm/Cancel buffers prevent accidental double-submit** (120 ms window)
- [ ] **Controller remapping documented** (even if not implementable in M0)

### Visual Hierarchy

- [ ] **Primary action is visually distinct** (larger, brighter, centered, or first focus)
- [ ] **Secondary actions are visually de-emphasized** (smaller, lower contrast, or collapsed by default)
- [ ] **Disabled states are unambiguous** (grayed out + text label, not color-only)
- [ ] **Related controls are grouped spatially** (not scattered randomly)
- [ ] **Labels are always present** (icons alone are insufficient)

### Audio Alternatives

- [ ] **Gamepad haptic feedback is optional** (can be disabled in settings)
- [ ] **UI audio cues are optional** (can be muted without losing function)
- [ ] **Critical audio information has visual feedback** (e.g., dialog cue tone also has on-screen indicator)

---

## Enhanced Requirements (TARGET by Vertical Slice; SHIP in Alpha)

These support players with specialized accessibility needs and preference for customization.

### Text Scaling & Readability

- [ ] **At least 3 text scale presets** (small, default, large)
- [ ] **Minimum scale preserves readability** (smallest preset ≥ 20 px body at 1080p)
- [ ] **Maximum scale prevents clipping** (largest preset fits on screen without overflow)
- [ ] **Text scale settings persist** across sessions
- [ ] **Live preview available** in settings (change and see immediately)
- [ ] **Long localized strings don't break layout** at max scale (layout reflows or scrolls)

### Contrast Modes

- [ ] **High-contrast mode available** (≥7:1 for all text, stark distinct colors)
- [ ] **High-contrast colors tested** against colorblind vision modes
- [ ] **High-contrast mode persists** across sessions
- [ ] **Visual design maintains intent** in high-contrast variant (not just numeric change)

### Colorblind Accessibility

- [ ] **Protanopia (red-blind) simulation testing** done
- [ ] **Deuteranopia (green-blind) simulation testing** done
- [ ] **Tritanopia (blue-yellow-blind) simulation testing** done
- [ ] **Colorblind mode uses distinguishable colors** (not red/green pairs)
- [ ] **All color-coded UI has non-color redundancy** (shape, pattern, text, or icon)
- [ ] **Optional colorblind-safe UI variant** available in settings

### Extended Subtitles

- [ ] **Speaker identification** always visible (text label, not color-only)
- [ ] **Sound effect descriptions** available for critical audio events (optional; "[sword clash]")
- [ ] **Music mood descriptions** optional for immersion-critical moments
- [ ] **Subtitle customization options**: size, background opacity, font choice
- [ ] **Subtitle timing** adjustable if player reads slower (optional delay before auto-dismiss)

### Control Remapping

- [ ] **Full control remapping interface** available in settings
- [ ] **Remapping persists** across sessions
- [ ] **Duplicate keybinds prevented** (warning if player assigns same key to two actions)
- [ ] **Remapping includes all critical inputs** (movement, combat, menu navigation, pause)
- [ ] **Default presets available** for common accessibility layouts (left-handed, one-handed, etc.)

### Motion Intensity Controls

- [ ] **Reduced-motion toggle** (no parallax, minimal camera shake, instant state changes)
- [ ] **Optional additional motion settings** (camera drift, animation intensity, distortion blur)
- [ ] **Motion settings persist** across sessions
- [ ] **Distortion overlays respect motion settings** (optional intensity slider if visual effects used)
- [ ] **All critical game state is readable without motion** (health, status, prompts all visible without animation)

### Navigation Aids

- [ ] **Auto-focus placement** always context-correct (never on destructive action)
- [ ] **Navigation tooltips** explain what each button does (e.g., "Y - View Stats")
- [ ] **Gamepad control hints** can be shown/hidden in settings
- [ ] **Keyboard control hints** can be shown/hidden in settings
- [ ] **Focus indicators customizable** (size, color, intensity)

---

## Known M0 Gaps (Deferred to Vertical Slice or Alpha)

These are important accessibility features deferred beyond M0 due to scope:

- [ ] Screen reader support (Vertical Slice or Alpha)
- [ ] Voice control integration (Alpha+)
- [ ] Braille display bridging (Post-launch)
- [ ] Full button remapping UI implementation (Alpha; documented, not coded in M0)
- [ ] Text-to-speech for lore/codex entries (Alpha+)
- [ ] Audio description for cutscenes (Vertical Slice)
- [ ] Language support beyond Latin + CJK (Post-launch based on audience demand)

---

## Implementation Notes

### For art-director

- **Visual indicators must never rely on color alone** — pair with shape, size, or position
- **High-contrast variant requires distinct colors** (tested against colorblind vision)
- **Focus ring visibility is non-negotiable** (always ≥3 px, ≥3:1 contrast)
- **Text readability under overlays** must be verified (no critical text disappears under distortion)
- **Motion effects must respect reduced-motion settings** (swap to opacity-only or instant state change)

### For unity-ui-specialist

- **Build tokenized theme system** that supports all contrast/scale/motion variants
- **USS token layer** should define baseline, high-contrast, colorblind, and reduced-motion variants
- **Theme switching should not require scene reload**
- **All accessibility settings must be data-driven** (not hardcoded in code or art)
- **Validate text floors** at all scale tiers before runtime

### For ui-programmer

- **All text through localization system** (no hardcoded player-facing strings; all support variable length)
- **All input mapping through rebindable action system** (InputSystem actions, not raw key checks)
- **All animations and motion should respect accessibility toggle**
- **Focus restoration on modal close is deterministic** (not random)
- **Data contracts should emit accessibility-relevant state** (disabled, selected, error, etc.)

### For gameplay systems

- **UI must never own or modify gameplay state** (UI is observer only)
- **Audio events routed through audio system** (not direct playback from UI)
- **Motion-critical feedback must have non-motion alternatives** (haptics optional, visual always present)

---

## QA Validation Matrix

| Scenario | Baseline Pass Criteria | Notes |
|----------|---|---|
| **Controller-only flow** | Complete critical path with controller only, no mouse required | Test all menus, dialogs, error recovery |
| **Keyboard-only flow** | Complete critical path with keyboard only, no mouse required | Test all menus, Tab order correct, Esc/Enter work |
| **Mouse flow** | Complete critical path with mouse, no keyboard required | Verify no hover-only affordances |
| **Reduced-motion ON** | All critical feedback visible without motion; no flashing; instant state changes | Stress-test combat HUD, error alerts |
| **Text scale MIN** | Body text readable at smallest preset; no layout clipping; line length caps respected | Verify all UI tiers scale proportionally |
| **Text scale MAX** | Body text readable at largest preset; no overflow; layout reflows if needed | Verify buttons don't become unreachable |
| **Contrast ratio check** | All text meets documented contrast thresholds; disabled states clear | Use contrast checker tool on captured screenshots |
| **Colorblind simulation** | Protanopia/Deuteranopia/Tritanopia modes; no color-only state still works | Use online colorblind simulator |
| **Subtitle safe zone** | Subtitles never overlap critical UI; 10% horizontal and 8% bottom margins held | Test under max HUD density in combat |
| **Focus regression** | Open/close overlays 10 times; focus never null; no accidental double-input | Rapid modal stress test |
| **Error recovery** | All error messages explain recovery; no lockout; always a way forward | Test network errors, invalid input, etc. |

---

## Risks

1. **Accessibility feature drift** — if not regularly tested, variants (high-contrast, colorblind, reduced-motion) may diverge from baseline
2. **Localization interaction with accessibility** — longer strings in other languages may break text-scale layouts
3. **Motor accessibility under pressure** — time-critical moments (boss fights) may unintentionally exclude players with slower inputs
4. **Theme variant performance** — accessibility settings toggling many CSS tokens may impact performance
5. **Input device switching** — seamless gamepad↔keyboard transition may have edge cases

---

## Open Questions

1. Should motion intensity be a single toggle or a scale (0-100%)?
2. Are there game-specific accessibility concerns (distortion overlays, psychological themes) that need special handling?
3. Should colorblind mode also adjust non-UI color (lighting, enemy tells) or UI only?
4. Should audio description be read via TTS or human-recorded for key moments?
5. Should text-scaling presets include a "custom" option or be fixed tiers?

---

## Acceptance Criteria

- [ ] Baseline requirements are documented and testable
- [ ] Standard requirements are documented with Vertical Slice target
- [ ] Enhanced requirements are documented with Alpha target
- [ ] M0 gaps are explicitly listed and deferred to later milestone
- [ ] QA validation matrix is executable without ambiguity
- [ ] Implementation notes are actionable for all disciplines
- [ ] No contradictions between layers (Baseline, Standard, Enhanced)
- [ ] All risks are documented with mitigation assigned
- [ ] Committed tier (Enhanced) is realistic for project scope and timeline

---

## Change Control

Any deviation from this accessibility requirement (removing baseline, deferring standard, or postponing enhanced) requires:
- Explicit justification
- Impact analysis on player accessibility
- Re-assessment at next milestone gate
- Documentation of alternative accessibility support

This preserves our commitment to inclusive game design.
