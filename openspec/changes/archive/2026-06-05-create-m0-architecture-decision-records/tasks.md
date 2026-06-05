## 1. ADR Artifact Authoring

- [x] 1.1 Create `docs/architecture/adr/ADR-0001-m0-runtime-foundation-and-scene-composition.md` with the required runtime foundation coverage.
- [x] 1.2 Create `docs/architecture/adr/ADR-0002-m0-gameplay-truth-ownership-boundaries.md` with the required gameplay truth ownership coverage.
- [x] 1.3 Create `docs/architecture/adr/ADR-0003-m0-presentation-and-debug-read-only-boundaries.md` with the required presentation/debug read-only coverage.
- [x] 1.4 Create `docs/architecture/adr/ADR-0004-m0-di-and-assembly-boundary-strategy.md` with the required DI and asmdef boundary coverage.
- [x] 1.5 Create `docs/architecture/adr/ADR-0005-m0-shared-contracts-strategy.md` with the required contracts strategy coverage.
- [x] 1.6 Verify all ADR text records already-made decisions only and marks unresolved items as `Open`.

## 2. Technical Requirement Registry

- [x] 2.1 Create or update `docs/architecture/tr-registry.yaml` with required entry fields (`id`, `title`, `status`, `source_gdds`, `adr_refs`, `implementation_refs`, `test_refs`, `notes`).
- [x] 2.2 Add all required minimum TR IDs with stable titles and ADR cross-references.
- [x] 2.3 Mark unresolved or not-yet-confirmed mappings as `Open` in `status` and/or `notes` without inventing architecture.

## 3. Scope and Quality Validation

- [x] 3.1 Validate the change remains documentation-only (no runtime, scene, prefab, UI/VFX, generated DI, or gameplay behavior changes).
- [x] 3.2 Validate ADR and TR outputs are structured for `/consistency-check` and `/gate-check` evaluability.
- [x] 3.3 Run `openspec status --change "create-m0-architecture-decision-records"` and confirm artifacts are apply-ready.
