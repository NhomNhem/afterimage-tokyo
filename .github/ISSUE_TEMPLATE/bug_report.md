---
name: Game Bug Report
about: Báo lỗi gameplay, UI, combat, scene, build hoặc hệ thống trong game
title: "[Bug] "
labels: bug
assignees: ''
---

## Description

Mô tả ngắn gọn bug đang xảy ra.

Ví dụ:
- Player bị kẹt ở một vị trí.
- Enemy không tấn công.
- UI không hiện đúng.
- Game crash khi chuyển scene.
- Animation bị lỗi khi dùng skill.

---

## Steps to Reproduce

Các bước để tái hiện lỗi:

1. Mở game / mở scene:
2. Vào màn chơi / khu vực:
3. Thực hiện hành động:
4. Kết quả lỗi xuất hiện:

Ví dụ:

1. Open `TokyoStreet_Demo` scene
2. Start Play Mode
3. Press `Left Shift` to dash near the wall
4. Player clips through the wall

---

## Expected Behavior

Điều đúng ra phải xảy ra là gì?

Ví dụ:
- Player không thể đi xuyên tường.
- Enemy phải phát hiện player trong phạm vi 10m.
- UI health bar phải giảm khi player nhận sát thương.
- Skill phải phát animation trước khi gây damage.

---

## Actual Behavior

Điều thực tế đang xảy ra.

Bao gồm:
- Error message trong Console
- Screenshot / video nếu có
- Log liên quan

Ví dụ:

```txt
NullReferenceException: Object reference not set to an instance of an object
PlayerCombat.Update() at Assets/_Project/Combat/PlayerCombat.cs:42
