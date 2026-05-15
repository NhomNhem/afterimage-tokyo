## Why

M0 already has key architecture decisions across runtime foundation, gameplay truth ownership, presentation boundaries, DI scope strategy, and shared contracts, but they are not yet captured in a single traceable record set. Creating lean ADRs plus a technical requirement registry now makes First Playable Duel decisions auditable and evaluable by consistency and gate checks without expanding M0 scope.

## What Changes

- Create five M0 ADR documents under `docs/architecture/adr/` to record already-made decisions
- Create `docs/architecture/tr-registry.yaml` with stable technical requirement IDs for the M0 skeleton layer
- Link each TR entry to source GDDs, ADR references, implementation references, and test references
- Mark unresolved items explicitly as `Open` rather than inventing architecture
- Keep this change documentation-only with no runtime code, scene, prefab, UI/VFX implementation, generated DI enablement, or new gameplay behavior changes

## Capabilities

### New Capabilities
- `m0-architecture-decision-records`: Lean ADR and technical requirement traceability layer for the current M0 architecture decisions.

### Modified Capabilities
- None

## Impact

- New docs under `docs/architecture/adr/`:
  - `ADR-0001-m0-runtime-foundation-and-scene-composition.md`
  - `ADR-0002-m0-gameplay-truth-ownership-boundaries.md`
  - `ADR-0003-m0-presentation-and-debug-read-only-boundaries.md`
  - `ADR-0004-m0-di-and-assembly-boundary-strategy.md`
  - `ADR-0005-m0-shared-contracts-strategy.md`
- New or updated `docs/architecture/tr-registry.yaml` with M0 TR entries and cross-references
- No runtime/system behavior impact; this is governance and traceability documentation only
