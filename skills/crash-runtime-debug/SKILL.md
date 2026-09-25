---
name: crash-runtime-debug
description: Analyze Android runtime crashes using logcat, tombstones, Houdini logs, ADB, gdbserver and register dumps.
---
# Crash Runtime Debugging

Runtime evidence > static inference.

1. Locate the complete crash/tombstone/logcat record.
2. Preserve the original log.
3. Extract signal, fault address, PC, LR/backtrace, registers, memory dumps, thread and ABI/translator information.
4. Convert PC/call-site carefully and never silently alter an address.
5. If register/memory values already exist, do not demand gdbserver merely to reproduce them.
6. If evidence is insufficient, specify the exact breakpoint/register/memory observation required.
7. Compare successive crashes and record changes.

## Required conclusion
CONFIRMED: exact values observed.
DERIVED: what those values establish.
NOT ESTABLISHED: what remains unknown.
NEXT: one concrete diagnostic action.
