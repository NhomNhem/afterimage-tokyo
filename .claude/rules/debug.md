# Debug Overlay Rules — Glass Refrain M0

## Purpose

Debug Overlay is the explanation layer for M0 tuning.

It must remain read-only.

## Must Display

- encounter state
- combat state
- locomotion state
- enemy intent state
- target focus state
- camera state
- health values
- memory state
- reveal requested/accepted/rejected
- last accepted/rejected request reason

## Forbidden

Debug Overlay must not:

- change gameplay state
- own combat truth
- own input routing
- own reveal validity
- own camera state
- hide gameplay readability problems

If the duel only makes sense with Debug Overlay on, gameplay readability is failing.
