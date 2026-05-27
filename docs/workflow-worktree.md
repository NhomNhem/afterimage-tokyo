# Workflow làm việc với Git Worktree + Submodule + Test + Merge + Push

## 1. Tư duy tổng quan

Project `afterimage-tokyo` hiện có 2 tầng Git:

```txt
J:\afterimage-tokyo                  # Parent repo
J:\afterimage-tokyo\afterimage-tokyo # Unity submodule
```

Parent repo **không lưu trực tiếp toàn bộ code Unity**. Parent repo chỉ lưu một **submodule pointer** trỏ tới một commit cụ thể trong Unity submodule.

Vì vậy mỗi lần làm feature trong Unity submodule, workflow đúng thường là:

```txt
1. Làm code trong worktree / submodule
2. Test trong Unity PlayMode
3. Commit trong submodule
4. Đưa commit đó vào submodule main
5. Push submodule trước
6. Commit parent pointer
7. Push parent sau
```

Nguyên tắc quan trọng:

```txt
Submodule code commit phải tồn tại trên remote trước.
Parent repo chỉ được push sau khi remote submodule đã có commit mà parent đang trỏ tới.
```

Nếu làm ngược lại, máy khác hoặc CI clone parent repo sẽ không checkout được submodule commit.

---

## 2. Khi nào dùng worktree?

Dùng worktree khi muốn làm song song nhiều lane mà không làm bẩn `main`.

Ví dụ:

```txt
J:\afterimage-tokyo-wt-lockon-decision
J:\afterimage-tokyo-wt-visual-polish
J:\afterimage-tokyo-wt-guardrails-refresh
```

Mỗi worktree nên có một nhiệm vụ rõ ràng:

```txt
lockon-decision       -> chỉ xử lý LockOn behavior
visual-polish         -> chỉ xử lý Parry/Counter visual feedback
guardrails-refresh    -> chỉ sửa docs/rules/agent guardrails
```

Không nên làm nhiều scope trong một worktree.

---

## 3. Luồng làm việc chuẩn với một worktree

### Bước 1: Vào đúng worktree

Ví dụ visual polish:

```powershell
cd J:\afterimage-tokyo-wt-visual-polish\afterimage-tokyo
```

Kiểm tra branch / commit / trạng thái:

```powershell
git status --short --branch
git log --oneline -5
```

---

### Bước 2: Kiểm tra scope trước khi code

Trước khi cho agent code, xác định rõ:

```txt
Allowed:
- File nào được sửa
- System nào được động vào
- Evidence nào cần tạo

Forbidden:
- Combat core rewrite nếu không thuộc scope
- Input architecture rewrite nếu không thuộc scope
- Scene/prefab/material thay đổi nếu không được yêu cầu
- Direct UnityEngine.Debug.Log trong project code
- DOTween authority thay đổi nếu không thuộc scope
```

Ví dụ visual-polish lane:

```txt
Allowed:
- Assets/_Project/Code/Presentation/M0CombatVisualFeedbackAdapter.cs

Forbidden:
- Combat core
- Input mapping
- Target context
- Camera
- Scene/prefab/material dependency changes
```

---

### Bước 3: Sau khi agent code xong, kiểm tra diff

```powershell
git status --short
git diff --stat
git diff -- Assets/_Project/Code/Presentation/M0CombatVisualFeedbackAdapter.cs
```

Nếu thấy file ngoài scope:

```txt
STOP
Không commit ngay.
Review xem có scope creep không.
```

---

## 4. Test trước khi commit

### 4.1. Test compile / domain reload

Trong Unity:

```txt
1. Focus Unity Editor
2. Chờ domain reload / compile xong
3. Kiểm tra Console
```

Không được có:

```txt
Compile error
Missing reference do code mới gây ra
Runtime exception khi chưa PlayMode
```

---

### 4.2. Test PlayMode sạch

Trước mỗi lượt test quan trọng:

```txt
1. Stop PlayMode
2. Clear Console
3. Enter PlayMode lại
4. Test đúng kịch bản
5. Đọc Console mới, không đọc log cũ
```

Lý do Clear Console:

```txt
Nếu không clear, lỗi cũ như Renderer.material hoặc NullReferenceException có thể vẫn nằm trong Console,
làm mình tưởng lỗi vẫn còn dù code đã fix.
```

---

## 5. Test LockOn

### Kịch bản test

```txt
Tab 1 -> LockOn acquired / overlay Enemy
Tab 2 -> LockOn released / overlay None
Tab 3 -> LockOn acquired / overlay Enemy
```

### Evidence log mong muốn

```txt
[M0Input] LockOn pressed
[M0Target] AcquireReason: LockOn toggled on
[M0Target] LockOn acquired
[M0Target] LockOn released
```

### PASS khi

```txt
- Tab lần 1 acquire được target
- Tab lần 2 release được target
- Tab lần 3 acquire lại được target
- Overlay LockOn Target khớp state thật
- Không có exception mới
```

### FAIL khi

```txt
- Tab không nhận input
- Tab 2 không release trong scope toggle-release
- Overlay hiện Enemy khi IsLockedOn=false
- Có exception liên quan TargetContext / Input / TickHandler
```

---

## 6. Test Parry / Counter

### Kịch bản test dương tính

```txt
1. Chờ enemy vào Telegraph / Commit / Active đúng timing
2. Nhấn Q / Parry đúng window
3. Quan sát CounterWindow opened
4. Nhấn E / Counter trong CounterWindow
5. Quan sát Counter consumed + CounterActive
```

### Evidence log PASS

```txt
[M0Input] Parry pressed
[M0Combat] State changed: Neutral -> ParryStartup
[M0Combat] State changed: ParryStartup -> ParryActive
[M0Combat] State changed: ParryActive -> ParryRecovery
[M0Combat] Parry success: CounterWindow opening
[M0Combat] CounterWindow opened duration=3
[M0Input] Counter pressed
[M0Combat] CounterWindow Counter consumed
[M0Combat] State changed: Neutral -> CounterActive
```

### Log fail không nhất thiết là bug

Các log sau có thể xuất hiện nếu bấm sai timing hoặc spam input:

```txt
[M0Combat] Parry fail: enemy intent not parry-eligible
[M0Combat] Parry rejected: not in Neutral
```

Không xem đây là blocker nếu sau đó vẫn đạt được sequence PASS.

### PASS khi

```txt
- Có ít nhất một sequence Parry success -> CounterWindow opened
- Counter trong window được consumed
- State chuyển sang CounterActive
- Không có exception mới
```

---

## 7. Test Visual Feedback fallback

### Kịch bản visual

```txt
Q / Parry    -> player flash cyan/blue
E / Counter  -> player flash gold/yellow + scale bump
```

### Runtime error không được xuất hiện

```txt
Not allowed to access Renderer.material on prefab object.
NullReferenceException: M0CombatVisualFeedbackAdapter.Awake()
```

### Rule code đúng

Dùng `sharedMaterial` để đọc/check:

```csharp
var shared = playerRenderer.sharedMaterial;
```

Dùng `MaterialPropertyBlock` để override màu runtime:

```csharp
playerRenderer.GetPropertyBlock(propertyBlock);
propertyBlock.SetColor(BaseColorId, color);
playerRenderer.SetPropertyBlock(propertyBlock);
```

Không dùng `.material` trong fallback/Awake path:

```csharp
playerRenderer.material // tránh trong fallback/Awake
```

### PASS khi

```txt
- Không còn Renderer.material prefab error
- Không còn Awake NullReferenceException
- Có visual flash / scale feedback quan sát được
- Không cần scene/prefab/material dependency mới nếu fallback đã đủ
```

---

## 8. Khi nào commit trong worktree?

Chỉ commit khi đủ điều kiện:

```txt
- Diff đúng scope
- Code compile
- PlayMode smoke test pass hoặc có lý do rõ nếu chưa test được
- Không có lỗi console mới
- Evidence/log đã ghi lại được
```

Commit trong worktree/submodule:

```powershell
git add <file>
git commit -m "fix: use property block for m0 visual feedback fallback"
```

Không commit nếu:

```txt
- Có file ngoài scope chưa hiểu vì sao thay đổi
- Unity scene/prefab bị dirty ngoài ý muốn
- Console có exception mới chưa xử lý
- Test chưa đủ mà commit message nghe như đã hoàn tất
```

---

## 9. Khi nào merge/cherry-pick về main submodule?

Sau khi lane/worktree đã:

```txt
- Code review local ổn
- Test PlayMode đủ cho scope
- Commit sạch
```

Đưa commit từ worktree về Unity submodule chính:

```powershell
cd J:\afterimage-tokyo\afterimage-tokyo

git fetch J:\afterimage-tokyo-wt-visual-polish\afterimage-tokyo HEAD
git cherry-pick FETCH_HEAD
```

Kiểm tra:

```powershell
git log --oneline -5
git status --short
```

Kỳ vọng commit mới nằm trên stack main/submodule checkout.

---

## 10. Detached HEAD trong submodule

Submodule thường ở detached HEAD:

```txt
HEAD detached from 78819cbb
```

Điều này bình thường.

Nhưng cần nhớ:

```powershell
git push origin main
```

sẽ push local branch `main`, không nhất thiết push commit detached hiện tại.

Nếu đang đứng ở detached commit đúng, ví dụ `17ef8ea7`, và muốn push commit đó lên remote `main`:

```powershell
git push origin HEAD:main
```

Cách sạch hơn nếu muốn local branch main cũng trỏ tới commit đó:

```powershell
git switch main
git merge --ff-only 17ef8ea7
git push origin main
```

Nếu remote main protected:

```powershell
git switch -c fix/m0-visual-feedback-property-block 17ef8ea7
git push origin fix/m0-visual-feedback-property-block
```

Sau đó tạo PR trong submodule repo.

---

## 11. Push khi nào?

### Push submodule khi

```txt
- Commit trong submodule đã test pass
- Commit là commit mà parent sẽ trỏ tới
- Không còn exception mới trong PlayMode
- Nếu cần PR thì branch đã sẵn sàng
```

Push submodule:

```powershell
cd J:\afterimage-tokyo\afterimage-tokyo

git push origin HEAD:main
```

Hoặc nếu local main đã đúng:

```powershell
git push origin main
```

Verify remote:

```powershell
git ls-remote origin main
```

Kỳ vọng hash remote là commit mới.

---

## 12. Commit parent pointer khi nào?

Sau khi submodule commit đã tồn tại trên remote.

Vào parent repo:

```powershell
cd J:\afterimage-tokyo
```

Kiểm tra:

```powershell
git status --short
git diff --submodule
git ls-tree HEAD afterimage-tokyo
```

Nếu thấy:

```txt
M afterimage-tokyo
```

nghĩa là parent pointer cần commit.

Commit parent pointer:

```powershell
git add afterimage-tokyo
git commit -m "chore: integrate m0 visual feedback property block fix"
```

Push parent:

```powershell
git push origin main
```

---

## 13. Push order chuẩn

Luôn theo thứ tự:

```txt
1. Push submodule trước
2. Push parent sau
```

Lý do:

```txt
Parent repo chỉ lưu hash của submodule.
Nếu parent được push trước nhưng submodule remote chưa có hash đó,
người khác/CI sẽ không checkout được project đầy đủ.
```

---

## 14. Khi nào archive / close story?

Chỉ archive khi đủ:

```txt
- Code đã merge vào đúng branch
- Submodule đã push
- Parent pointer đã push
- Evidence file đã cập nhật
- Story-done / code-review / release-gate đã pass hoặc pass with accepted notes
- Không còn FAIL blocker
```

Không archive nếu:

```txt
- Còn exception runtime chưa xử lý
- Evidence chưa cập nhật commit mới
- Parent chưa trỏ đúng submodule commit
- Submodule commit chưa tồn tại trên remote
```

---

## 15. Evidence cần ghi gì?

Evidence nên ghi:

```txt
- Submodule commit hash
- Parent commit hash
- Unity PlayMode test date/time
- Test scenario
- PASS / PARTIAL / FAIL rõ ràng
- Known warnings nếu có
- Non-blocking follow-up nếu có
```

Ví dụ:

```md
## Verification Snapshot

Submodule commit: `17ef8ea7 fix: use property block for m0 visual feedback fallback`
Parent commit: `<parent commit> chore: integrate m0 visual feedback property block fix`

### Results

- LockOn first press acquire: PASS
- LockOn second press release: PASS
- LockOn reacquire: PASS
- Renderer.material prefab error absent: PASS
- M0CombatVisualFeedbackAdapter.Awake NRE absent: PASS
- Parry success opens CounterWindow: PASS
- Counter consumes CounterWindow: PASS
- CounterActive transition: PASS

### Console

Result: PASS WITH KNOWN WARNINGS

Known warnings:
- Animation presentation adapter missing
- Animation presentation not assigned

Notes:
- Known animation warnings accepted for current M0 smoke slice.
- Parry fail/rejected logs can appear from mistimed manual input and are non-blocking when positive sequence is proven.
```

---

## 16. Checklist nhanh mỗi lần làm lane mới

```txt
[ ] Tạo hoặc vào đúng worktree
[ ] Xác định scope allowed/forbidden
[ ] Agent/code chỉ sửa đúng file/system
[ ] Check git diff --stat
[ ] Check file ngoài scope
[ ] Unity compile/domain reload sạch
[ ] Clear Console trước PlayMode
[ ] PlayMode test đúng scenario
[ ] Không có exception mới
[ ] Có positive evidence log/screenshot
[ ] Commit trong submodule/worktree
[ ] Cherry-pick/merge về submodule main checkout
[ ] Push submodule commit lên remote
[ ] Commit parent submodule pointer
[ ] Push parent repo
[ ] Update evidence
[ ] Run story-done/code-review/release-gate
[ ] Archive sau khi no blockers
```

---

## 17. Rule vàng

```txt
Worktree để cô lập scope.
Submodule commit để lưu code Unity.
Parent commit để lưu pointer tới submodule commit.
Test trước merge.
Push submodule trước parent.
Archive sau evidence + review gate.
```
