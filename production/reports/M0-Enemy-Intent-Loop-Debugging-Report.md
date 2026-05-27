# M0 Enemy Intent Loop Debugging Report

**Date:** 2026-05-19
**Task:** Fix M0 Enemy Intent Loop regression
**Status:** BLOCKED - Requires manual Unity Editor investigation

---

## Issue Description

The M0 Enemy Intent Loop in `M0EnemyIntentLoopDriver` was not progressing through state transitions. The enemy state remained stuck at "Idle" and never transitioned to Telegraph, Commit, Active, or Recovery states.

---

## Investigation Steps

### 1. Initial Scene Inspection
- Verified `Enemy_M0TargetablePlaceholder` GameObject exists in Gameplay_CombatPrototype.unity
- Verified `M0EnemyIntentLoopDriver` component is attached
- **Finding:** Scene reference fileID mismatch - loopDriver pointed to MeshFilter (fileID: 500000014) instead of MonoBehaviour (fileID: 500000013)
- **Action:** Fixed scene reference fileID

### 2. Injection Investigation
- Checked VContainer registration in `GameplayLifetimeScope`
- **Finding:** `RegisterComponentInHierarchy` for loopDriver was failing injection
- **Finding:** `M0EnemyIntentModel` logger was not being injected via VContainer
- **Actions:**
  - Changed to `RegisterComponent` with manual `Construct` call in build callback
  - Added `FindObjectOfType` fallback for loopDriver reference
  - Added public `InjectLogger` method to `M0EnemyIntentModel`
  - Added manual logger injection via reflection in build callback

### 3. Coroutine Behavior Analysis
- Original implementation used coroutine-based loop with `yield return WaitForSeconds`
- **Finding:** Coroutine started but got stuck at first yield, never resumed
- **Verification:** GameObject was active, Time.timeScale was 1
- **Decision:** Converted to Update-based timer loop to bypass coroutine yield issue

### 4. Update-Based Loop Investigation
- Replaced coroutine with Update method using timer-based state machine
- **Finding:** Update method is never called despite GameObject being active
- **Verification:**
  - Added Awake log: Confirmed Awake called
  - Added Start log: Confirmed Start called with gameObject.active=True
  - Added Update log: Update never called
  - Added OnDisable/OnDestroy logs: Neither called
- **Scene File Verification:**
  - GameObject has `m_IsActive: 1` (active)
  - Component has `m_Enabled: 1` (enabled)
  - GameObject has no parent (root level)

### 5. Code Cleanup
- Removed all temporary Debug.Log calls per user request ("không được sử dụng UnityEngine.Debuglog")
- Used only logger for all diagnostic output
- Removed diagnostic lifecycle methods (Awake, OnDestroy, OnDisable) after investigation

---

## Files Modified

### M0EnemyIntentLoopDriver.cs
- Converted coroutine loop to Update-based timer loop
- Added initial EnterIdle call in Start
- Removed all Debug.Log calls
- Added state machine with phases: 0=Idle, 1=Telegraph, 2=Commit, 3=Active, 4=Recovery

### M0EnemyIntentModel.cs
- Made InjectLogger method public for manual injection
- Removed temporary Debug.Log calls

### GameplayLifetimeScope.cs
- Changed loopDriver registration from RegisterComponentInHierarchy to RegisterComponent
- Added manual Construct call in build callback
- Added FindObjectOfType fallback for loopDriver
- Added manual logger injection to M0EnemyIntentModel

### Gameplay_CombatPrototype.unity
- Fixed loopDriver fileID from 500000014 (MeshFilter) to 500000013 (MonoBehaviour)

---

## Technical Details

### Enemy Timing Values (Serialized)
- idleDuration: 1.50s
- telegraphDuration: 0.75s
- commitDuration: 0.20s
- activeDuration: 0.15s
- recoveryDuration: 0.60s

### Injection Chain
```
GameplayLifetimeScope.Configure()
  → RegisterComponent<M0EnemyIntentLoopDriver>()
  → Register<M0EnemyIntentModel>()
  → Register<INhemLogger>()

GameplayLifetimeScope.BuildCallback()
  → Resolve<INhemLogger>()
  → FindObjectOfType<M0EnemyIntentLoopDriver>() (fallback)
  → Resolve<M0EnemyIntentModel>()
  → loopDriver.Construct(model, logger)
  → model.InjectLogger(logger) (reflection)
```

---

## Decisions Made

1. **Manual Injection:** Used manual Construct call and FindObjectOfType fallback instead of relying solely on VContainer automatic injection
2. **Reflection-Based Logger Injection:** Used reflection to inject logger into M0EnemyIntentModel since VContainer registration was not working
3. **Update-Based Timer Loop:** Replaced coroutine with Update-based approach to bypass yield suspension issue
4. **Code Cleanup:** Removed all Debug.Log calls per user requirements, using only project logger

---

## Current Blocker

**Issue:** Unity's Update method is not being invoked on M0EnemyIntentLoopDriver

**Evidence:**
- GameObject is active (m_IsActive: 1 in scene file)
- Component is enabled (m_Enabled: 1 in scene file)
- Awake and Start methods are called successfully
- OnDisable and OnDestroy are never called
- Update method is never called
- No code disables the GameObject or component

**Possible Causes (Requires Manual Investigation):**
- Script execution order issue
- Scene configuration problem
- Unity engine bug or unexpected behavior
- GameObject hierarchy issue not visible in scene file
- Editor-only vs runtime behavior difference

---

## Recommendations

1. **Manual Unity Editor Investigation:**
   - Open Gameplay_CombatPrototype scene in Unity Editor
   - Select Enemy_M0TargetablePlaceholder GameObject
   - Verify component is enabled in Inspector
   - Verify GameObject is active in Hierarchy
   - Check if any parent GameObject is disabled
   - Check script execution order settings
   - Test with a simple Debug.Log in Update to confirm Unity behavior

2. **Alternative Approaches:**
   - Try using FixedUpdate instead of Update
   - Try using a custom tick system (e.g., M0GameplayTickHandler)
   - Move loop logic into a service instead of MonoBehaviour

3. **Code Review:**
   - Review if any other scripts in the scene might be affecting this GameObject
   - Check for any script that might disable GameObjects at runtime

---

## Logs Summary

### Expected Behavior
```
[M0EnemyLoop] Driver enabled
[M0EnemyLoop] RunLoop starting (Update-based timer)
[M0DebugOverlay] Snapshot update received combatState=Neutral enemyState=Idle
[M0EnemyLoop] Tick transition Telegraph -> Commit
[M0DebugOverlay] Snapshot update received combatState=Neutral enemyState=Telegraph
[M0EnemyLoop] Tick transition Commit -> Active
... (cycle continues)
```

### Actual Behavior
```
[M0EnemyLoop] Driver enabled
[M0EnemyLoop] RunLoop starting (Update-based timer)
[M0DebugOverlay] Snapshot update received combatState=Neutral enemyState=Idle
[M0DebugOverlay] Snapshot update received combatState=Neutral enemyState=Idle
... (enemyState remains Idle forever)
```

---

## Next Steps

**BLOCKED** - Requires manual investigation in Unity Editor to determine why Update is not being called on this specific GameObject/component.

Once the Update invocation issue is resolved, the Update-based timer loop should work correctly and the enemy intent state transitions should function as expected.
