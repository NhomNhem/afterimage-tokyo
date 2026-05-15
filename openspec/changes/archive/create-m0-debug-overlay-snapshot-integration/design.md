# Design

## Problem

The first duel spans many systems, and their current state is hard to read without a shared developer-facing snapshot. The overlay must not become gameplay UI or a hidden authority layer.

## Approach

Build a small pure C# aggregation model that accepts read-only snapshots from the existing M0 systems and emits a single aggregate snapshot plus per-channel groups. Each channel remains independent and visible or hidden through overlay state only.

## Debug Channels

Required channels:

- Input
- Locomotion
- Target Context
- Combat Core
- Enemy Intent / Telegraph
- Health / Damage / Hit Reaction
- Memory State
- Memory VFX Response
- Encounter Framework

## Rules

- The overlay is read-only.
- The overlay never mutates source systems.
- The overlay never infers missing gameplay truth.
- Last accepted/rejected reasons are pass-through data only.
- No UI Toolkit, UXML, USS, MonoBehaviour overlay, or scene wiring in this change.

## Notes

This change should stay small enough to review independently from the actual debug UI implementation. The goal is the data model and contracts, not the final presentation layer.
