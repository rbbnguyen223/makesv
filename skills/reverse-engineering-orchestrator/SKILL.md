---
name: reverse-engineering-orchestrator
description: Orchestrate APK, native .so, runtime crash, asset, protocol, and code-reconstruction analysis. Use for game reverse-engineering tasks.
---
# Reverse Engineering Orchestrator

## Mission
Coordinate evidence-first reverse engineering of an Android game/client. Never invent addresses, symbols, fields, protocols, or runtime behavior.

## Mandatory workflow
1. Inspect the workspace before changing anything.
2. Identify APK, extracted APK, lib/*.so, assets, logs, scripts, and prior reports.
3. Build a short evidence map: file -> artifact -> finding.
4. Prefer direct evidence over naming proximity or guesses.
5. Classify findings: CONFIRMED, DERIVED, UNKNOWN.
6. For every UNKNOWN, give one concrete next action that can produce evidence.
7. Before modifying code/binaries, state the exact proposed change and wait for explicit approval unless the user already requested the change.
8. Preserve a backup before destructive changes and record exactly what changed.
9. Re-test and compare logs before another change.

## Anti-loop rule
Do not repeat an action that produced the same evidence. Update the evidence map and choose the next diagnostic step.

## Output
### CONFIRMED
### DERIVED
### UNKNOWN
### NEXT ACTION
### FILES TO TOUCH
