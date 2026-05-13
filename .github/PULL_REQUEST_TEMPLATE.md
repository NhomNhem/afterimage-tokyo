## Summary

Brief description of what this PR does.

Example:
- Adds lock-on targeting system for melee combat.
- Fixes player dash clipping through walls.
- Updates Tokyo Street lighting and post-processing.
- Adds memory journal UI prototype.

---

## Type of Change

- [ ] Gameplay feature
- [ ] Combat system
- [ ] Player controller
- [ ] Enemy AI
- [ ] Boss mechanic
- [ ] Companion / party system
- [ ] UI / UX
- [ ] Camera
- [ ] Animation
- [ ] VFX / Shader
- [ ] Audio
- [ ] Level design
- [ ] Narrative / dialogue
- [ ] Save / load
- [ ] Performance / optimization
- [ ] Editor tool
- [ ] Bug fix
- [ ] Documentation improvement
- [ ] Build / deployment
- [ ] Refactor
- [ ] Other:

---

## Changes

-
-
-

Example:

- Added `LockOnTargetingService`
- Added lock-on marker UI prefab
- Updated player movement to support strafe mode
- Added target switching with keyboard input
- Added basic tests for target selection logic

---

## Gameplay Impact

What changes for the player?

Example:
- Player can now lock onto nearby enemies.
- Combat camera now follows the selected target.
- Dash no longer passes through walls.
- Enemy attack timing is more readable.

---

## Technical Notes

Mention important implementation details.

Example:
- Uses `VContainer` for service registration.
- Uses `R3` for target change events.
- Uses ScriptableObject config for tuning values.
- Uses Unity Input System action: `Combat/LockOn`.
- Compatible with Unity 6000.3.x.

---

## Scenes / Prefabs Changed

List changed Unity assets if relevant.

- [ ] Scene:
- [ ] Prefab:
- [ ] ScriptableObject:
- [ ] Animator Controller:
- [ ] Material / Shader:
- [ ] UI Document / UXML / USS:
- [ ] Audio Mixer:
- [ ] Other:

---

## How to Test

Steps for reviewer to verify this PR:

1. Open Unity project
2. Open scene:
3. Enter Play Mode
4. Perform:
5. Confirm:

Example:

1. Open `TokyoStreet_CombatTest`
2. Press Play
3. Approach enemy group
4. Press `Tab` to lock-on
5. Confirm camera focuses target and UI marker appears

---

## Expected Result

What should happen after testing?

Example:
- Player can lock onto the nearest enemy within range.
- Lock-on breaks when enemy dies or moves too far away.
- No errors appear in Unity Console.
- Camera movement feels smooth.

---

## Screenshots / Videos

Attach screenshots, GIFs, or short gameplay videos if this affects visuals, UI, animation, level design, or player feel.

---

## Checklist

- [ ] I tested this in Unity Play Mode
- [ ] I tested this in the relevant scene
- [ ] No new errors in Unity Console
- [ ] No missing references in prefabs or scenes
- [ ] No unintended scene changes
- [ ] New scripts are placed in the correct project folder
- [ ] New systems are registered in DI / installer if needed
- [ ] ScriptableObject configs are assigned if needed
- [ ] Input actions are updated if needed
- [ ] UI works at common resolutions
- [ ] Performance impact is acceptable
- [ ] Build still succeeds
- [ ] Documentation / OpenSpec / GDD updated if needed

---

## Related Issues

Closes #
Related to #

---

## Additional Context

Anything reviewers should know:

- Known limitations
- Temporary placeholder assets
- Follow-up tasks
- Design risks
- Dependencies on another PR