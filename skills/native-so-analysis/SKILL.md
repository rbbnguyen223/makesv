---
name: native-so-analysis
description: Evidence-first analysis of ARM/ARM64/x86 native shared libraries with Ghidra, disassembly, symbols, strings, relocations, and object layouts.
---
# Native .so Analysis

1. Record SHA-256, file size, architecture, ELF type and load-bias information.
2. Identify exported/imported symbols and debug information.
3. Run strings and cross-reference important strings.
4. Analyze functions around confirmed crash PCs.
5. For important instructions record file, address, instruction and registers.
6. Separate confirmed memory values from inferred object fields/types.
7. Correlate static analysis with runtime registers.
8. Never rename functions/classes solely because nearby strings look suggestive.

## Crash rule
If a crash log contains registers/memory, use those actual values before static naming.

## Output
Address | Instruction | Evidence | Interpretation | Confidence
