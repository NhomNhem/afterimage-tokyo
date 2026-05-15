# Glass Refrain — UI Identity Foundation

> **Status**: Foundation (UX Review Approved)  
> **Author**: ux-designer (via team-ui skill)  
> **Last Updated**: 2026-05-14  
> **Version**: 1.0  
> **Engine**: Unity 6000.3.x  
> **UI Framework**: UI Toolkit  
> **Primary Input**: Gamepad-first, keyboard/mouse parity required

---

## Purpose

This document establishes the **emotional and behavioral foundation** for all Glass Refrain player-facing UI.  
It defines the core pillars, emotional direction, interaction philosophy, and constraints that all future screens and systems must honor. This is not a final HUD spec or complete menu design — it is the identity contract that prevents UI from becoming generic, cluttered, or tonally inconsistent.

---

## M0 Scope

- Foundational identity framework only
- Constraints and guardrails for future screens
- Emotional direction and design language definition
- No M0 implementation code
- No production-ready HUD yet
- No menu screens yet
- No full accessibility implementation yet (baseline direction only)

---

## Non-Goals

- Do not implement UI Toolkit code
- Do not create UXML/USS
- Do not design specific menu screens
- Do not build full accessibility solutions yet
- Do not create production art assets
- Do not solve platform-specific issues beyond direction

---

## Core Identity Pillars

### 1. Emotional Minimalism
**Rule**: Show only what is needed for the current decision.  
**Spirit**: Each UI element should feel intentional and necessary, never decorative.  
**Avoid**: persistent dense HUD blocks, decorative noise, status spam.

### 2. Elegant Restraint
**Rule**: Precision over abundance; fewer elements with stronger intent.  
**Spirit**: Beauty held in tension with sadness; controlled power.  
**Avoid**: flashy micro-animations, exaggerated callouts, novelty interactions.

### 3. Psychological Overlays
**Rule**: Distortion overlays may influence mood, never critical readability.  
**Spirit**: Memory interference visualized but never at cost of control.  
**Avoid**: obscuring health, prompts, subtitles, or focus state.

### 4. Quiet Domestic Atmosphere
**Rule**: Menus and pauses feel intimate and human-scale.  
**Spirit**: Like remembering in a quiet room, not commanding a system dashboard.  
**Avoid**: sterile control-panel layouts, aggressive gamification framing.

### 5. Grounded Cinematic UX
**Rule**: UI behaves like part of the scene rhythm, not detached app UI.  
**Spirit**: In-world and composed; never arcade or snappy.  
**Avoid**: mobile-style snap/bounce, instant stack explosions, hyperactive HUD clutter.

---

## Emotional Direction

### Target Emotional Blend
- **Lonely**: UI reinforces the protagonist's isolation
- **Emotionally fragile**: interactions feel delicate, not robust
- **Calm but unsettling**: low-pressure surface masking subtle dread
- **Restrained elegance**: beauty without spectacle
- **Guiding phrase**: **"fragments of fading memories"**

### Tone Statement
UI should feel like memory fragments surfacing through rain: controlled, quiet, and intimate — never loud, never playful, never hyperactive.

---

## Interaction Philosophy

### Principles (in priority order)
1. **Clarity over speed**: A clear interaction that takes 200ms beats a snappy one that confuses
2. **Consistency over novelty**: Same inputs produce same outcomes across all screens
3. **One-action dominance**: Every screen has one primary action; others are secondary or hidden
4. **Progressive disclosure**: Show only what is needed now; reveal depth when context demands it
5. **Deterministic controller behavior**: Gamepad controls are predictable and muscle-memory-friendly

### Navigation Philosophy

#### Single Readable Stack Model
- **In-World Layer** (moment-to-moment HUD prompts)
- **Overlay Layer** (inventory, map, journal, status)
- **Blocking Modal Layer** (confirmation/error/system interrupts)

Only one blocking modal at a time. No hidden jumps.

#### Navigation Guarantees
- Forward = deeper context
- Back = previous context, always available, globally consistent semantic meaning
- Replace = state transition, not history growth
- Every interactive screen is fully operable via gamepad only
- Initial focus is always visible, intentional, and context-safe
- Focus order follows spatial logic (top-to-bottom, left-to-right unless justified)
- No dead-end focus nodes

---

## Visual Language Philosophy

### Core Intent
UI should feel like **fading memory fragments**: elegant, sparse, and slightly unstable.

### Material Language
- **Frosted glass planes**: translucent, low-noise, restrained depth
- **Desaturated cyan-violet accent**: cool-tone focus/selection/progress signaling
- **Humanist sans typography** with serif micro-accent: readable and poetic
- **High intentional whitespace**: negative space carries hierarchy

### Visual Rules
- Sparse composition
- No ornamental clutter
- Subtle texture and imperfection for memory tone
- Cinematic anchoring to scene context
- At least **35% quiet area** on major menu screens

### Anti-Patterns
- Rainbow rarity overload
- Constant glow pulses
- Thick always-on borders everywhere
- Dense icon grids without grouping
- Mobile-app style bright CTA dominance

---

## Motion Philosophy

### Motion Intent
Motion communicates **state change and emotional rhythm**, not excitement.

### Motion Rules
- Transitions are soft, directional, and minimal
- Major panels: gentle fade/slide (180–280 ms)
- Focus shifts: subtle luminance/outline response, no jumpy scaling
- Combat-critical feedback may be sharper but brief
- Return to stillness quickly after event confirmation
- No spring/bounce overshoot

### Reduced-Motion Variant
- Remove non-essential movement
- Keep instant state clarity (opacity/state swaps acceptable)
- No distortion flicker that risks discomfort

---

## Audio Feedback Philosophy

### Audio UX Intent
Audio cues confirm intent and outcome with low intrusiveness.  
Silence is part of the identity; use cues sparingly.

### Cue Taxonomy
- `ui/focus`: soft navigation tick (non-fatiguing)
- `ui/confirm`: restrained affirmative cue
- `ui/cancel`: soft negative/return cue
- `ui/error`: clear but not harsh warning cue
- `ui/modal-open`: gentle attention draw
- `ui/modal-close`: resolution release
- `ui/critical`: high-priority state alert (rare)
- `ui/memory-shift`: psychological layer transition cue

### Audio Rules
- One cue per meaningful event
- No cue stacking for a single action
- Priority ducking: critical gameplay > critical UI > standard UI

---

## Information Hierarchy Philosophy

### Priority Tiers
- **Tier 0 (Critical now)**: survival/combat-immediate info
- **Tier 1 (Actionable soon)**: objective/context prompts
- **Tier 2 (Reference)**: inventory/stats/detail layers
- **Tier 3 (Lore/ambient)**: optional narrative/supporting context

### HUD Disclosure Policy
- Exploration: minimal HUD baseline (max 4 persistent elements)
- Combat: reveal only combat-essential data (max 6 elements)
- Investigation/dialogue: shift emphasis to narrative comprehension
- Return to minimal state after peak moments

### Cognitive Load Controls
- Limit simultaneous alert channels
- Chunk related information spatially
- Preserve layout memory (stable anchors)
- Avoid moving targets for recurring actions

---

## Controller-First Principles (Explicit)

1. UI must be complete and comfortable without cursor use
2. Focus indicator must be unmistakable at all times
3. Focus travel must be predictable and recoverable
4. Initial focus defaults to safest meaningful action
5. Back/cancel behavior is globally consistent
6. High-frequency actions minimize traversal distance
7. If mouse hover reveals info, focus must reveal equivalent info

---

## Accessibility Direction

### Baseline Requirements (must pass all)
- Keyboard-only usable
- Gamepad-only usable
- Readable text at minimum supported size (24 px @1080p body floor)
- No color-only meaning (paired with shape, text, or icon)
- No unsafe flashing without warning
- Subtitles for all dialogue (max 2 lines, Latin + CJK support)
- UI scales across all supported resolutions (16:9, 21:9)

### Enhanced Targets
- Full control remapping support
- Adjustable text scale presets (live preview)
- High contrast mode
- Subtitle customization (size, background, speaker labels)
- Input hold/toggle alternatives
- Notification duration options
- Motion intensity controls for overlays/distortion

---

## Implementation Notes

### For art-director
- Preserve restraint, negative space, and low-noise composition
- All visual additions must align to game-concept tone (melancholic, restrained, elegant)
- Validate readability under overlays/distortion scenes
- Use tokenized visual system to prevent style drift

### For unity-ui-specialist
- Use UI Toolkit as default framework
- Implement layer containers (ScreenStack, HUD, Modal, TransientOverlay)
- Build tokenized USS theme system with accessibility variants
- Controller-first navigation with explicit focus routing
- UI observes state only; no gameplay ownership

### For ui-programmer
- All text through localization system (no hardcoded player-facing strings)
- Support gamepad, keyboard, and mouse input with documented parity
- Implement accessibility features per committed tier
- Wire data binding to read-only gameplay state interfaces
- Respect input buffering defaults and focus restore behavior

---

## Risks

1. **Tone collapse into generic minimal UI** if "psychological overlay" usage lacks explicit boundaries
2. **Controller feel drift** without measurable interaction defaults enforced
3. **Accessibility edge cases** shipping without hard numeric thresholds
4. **Cross-discipline interpretation risk** — philosophy is strong, but handoff ambiguity could cause inconsistent implementation
5. **Theme variant drift** from spec without token snapshot tests and visual checklist per variant

---

## Open Questions

1. Which screens are prioritized for first detailed pattern specs (Pause, HUD, Inventory, Settings)?
2. Should psychological overlays affect menu screens, or world/HUD only?
3. What is the desired default HUD density in exploration (ultra-minimal vs minimal+objective)?
4. Which enhanced accessibility targets are required for first playable vs later milestone?
5. How will distortion effects be toggled on/off independent of accessibility motion settings?

---

## Acceptance Criteria

- [ ] All five emotional pillars are present and documented
- [ ] Navigation model is unambiguous and tested across all three layers
- [ ] Visual language tokens are defined (color, type, spacing, surface, motion)
- [ ] Controller-first behavior is testable (focus order, wrap rules, input timing)
- [ ] Accessibility baseline is documented and measurable (contrast ratios, text floors, reduced-motion rules)
- [ ] Audio cue taxonomy is defined with ducking priority rules
- [ ] Implementation handoff is clear (separate notes for art-director, unity-ui-specialist, ui-programmer)
- [ ] No contradictions between emotional pillars and implementation guidance
- [ ] Risk register is current and mitigation plans are assigned

---

## Next Steps

1. All designers and programmers must read this document before touching any UI
2. Run `/ux-design` on the first priority screens (see Open Questions)
3. Create detailed `design/ux/[screen-name].md` specs aligned to this identity
4. Build unity-ui-specialist UI Toolkit skeleton with tokenized theming
5. Validate all implementation against this foundation periodically
