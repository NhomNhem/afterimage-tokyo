## Context

The previous `tune-m0-enemy-telegraph-readability` pass established a baseline readability and evidence rubric. This proposal is the next M0 feel pass: improve what the player and debug tooling can read from the existing enemy intent loop without moving gameplay authority.

The current M0 loop remains:

```txt
read -> evade/parry -> counter -> reveal
```

Enemy readability is successful only if the `read` step gives enough information for the player to choose evade/parry and understand the later counter/reveal result.

## Design Direction

Expose a small, stable readability model from Enemy Intent and Telegraph:

- current phase
- phase time remaining or normalized progress
- attack tags for the committed intent
- whether the player-facing defensive answer is expected to be dodge, parry, or spacing
- whether recovery/punish is available
- human-readable reason text for debug/evidence

Presentation systems may consume this model to align animation, VFX, audio, camera emphasis, or overlay labels, but cannot author phase state or timing truth.

## Ownership Boundaries

Enemy Intent and Telegraph:

- owns phase truth and transition timing
- owns attack tag continuity from Commit through Active
- owns punish window availability
- emits immutable snapshots/read models

Combat Core:

- owns accepted/rejected defensive actions
- owns counter opportunity truth
- owns hit resolution and reveal request context

Presentation and Debug:

- observe snapshots
- show phase, cue, tag, and reason information
- never mutate gameplay state
- never infer combat results independently

## Verification Strategy

Automated verification should cover:

- phase readability snapshot immutability
- Telegraph, Commit, Active, Recovery labels remain distinguishable
- attack tags remain stable from Commit through Active
- punish availability is exposed only from enemy intent truth
- Debug Overlay or presentation adapters cannot mutate enemy intent state
- no direct `UnityEngine.Debug.Log*` calls are introduced in owned gameplay/presentation code

Manual verification should cover:

- observe at least three complete enemy loops in the M0 duel scene
- confirm Telegraph is readable before Active begins
- confirm Commit/Active transition is visible or otherwise explainable
- confirm Recovery/punish window can be identified in time for counter decision
- classify console output as hard errors, known external warnings, or expected debug output

## Risks

- Readability tuning can accidentally become difficulty tuning if phase durations change without evidence.
- Visual/audio cue work can drift into presentation owning phase truth.
- Debug overlay improvements can become gameplay dependencies if not kept read-only.
- Existing test asmdefs that reference Odin-serialized configs must include correct Odin serialization references to avoid compile regressions.
