---
name: Game Feature Request
about: Đề xuất gameplay feature, system, content, tool, UI/UX hoặc cải tiến cho game
title: "[Feature] "
labels: enhancement
assignees: ''
---

## Summary

Mô tả ngắn gọn feature hoặc cải tiến muốn thêm vào game.

Ví dụ:
- Thêm hệ thống lock-on target cho combat.
- Thêm companion đi theo player.
- Thêm UI memory journal.
- Cải thiện camera khi combat trong hẻm nhỏ.
- Thêm enemy type mới cho khu Tokyo Street.

---

## Feature Type

- [ ] Gameplay Mechanic
- [ ] Combat System
- [ ] Player Controller
- [ ] Enemy AI
- [ ] Boss Mechanic
- [ ] Companion / Party System
- [ ] Quest System
- [ ] Dialogue / Narrative
- [ ] Memory / Flashback System
- [ ] Inventory / Item System
- [ ] Skill / Ability
- [ ] UI / UX
- [ ] Camera
- [ ] Animation
- [ ] VFX / Shader
- [ ] Audio / Music
- [ ] Level Design
- [ ] Save / Load
- [ ] Performance / Optimization
- [ ] Editor Tool
- [ ] Build / Deployment
- [ ] Documentation
- [ ] Other:

---

## Problem / Motivation

Feature này giải quyết vấn đề gì?

Ví dụ:
- Combat hiện tại thiếu cảm giác “đã tay”.
- Player dễ bị lạc trong map Tokyo Street.
- Game cần hệ thống ký ức để hỗ trợ tone buồn / mystery.
- Enemy hiện tại chưa đủ áp lực.
- Designer cần tool để setup encounter nhanh hơn trong Unity Editor.

---

## Design Goal

Mục tiêu thiết kế của feature này là gì?

Ví dụ:
- Tăng cảm giác hành động nhanh, mượt, giống Blade & Soul.
- Làm player cảm thấy cô đơn nhưng vẫn có kết nối cảm xúc với companion.
- Biến ký ức thành một phần của gameplay, không chỉ là cutscene.
- Giúp combat có chiều sâu nhưng không quá phức tạp.

---

## Proposed Solution

Mô tả cách feature nên hoạt động.

Nên ghi rõ:

- Người chơi làm gì?
- Game phản hồi như thế nào?
- Feature xuất hiện ở đâu?
- Feature liên quan tới system nào?
- Có cần UI, animation, VFX, audio không?

Ví dụ:

Player có thể lock-on enemy bằng phím `Tab`.

Khi lock-on:

- Camera xoay nhẹ về hướng enemy.
- Player movement chuyển sang strafe.
- Skill melee tự ưu tiên target đang lock.
- UI hiển thị marker trên đầu enemy.
- Nếu enemy đi quá xa, lock-on tự hủy.

---

## Gameplay Flow

Mô tả flow sử dụng feature trong game.

```txt
Player enters combat
→ Enemy appears
→ Player presses Tab to lock-on
→ Camera focuses target
→ Player uses dash + slash combo
→ Enemy staggered
→ Player executes finisher
