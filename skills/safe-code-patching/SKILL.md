---
name: safe-code-patching
description: Make minimal, reversible code or text patches while preserving the existing project and UI.
---
# Safe Code Patching

1. Do not rewrite whole files for a local change.
2. Read the actual current file before constructing a patch.
3. Patch against content that exists NOW, not an earlier copy.
4. Prefer structural anchors over huge exact-text replacements.
5. Before writing, show target file, exact region and intended change.
6. Create a backup before destructive changes.
7. Verify patch count: expected 1 for a unique replacement; fail closed on 0 or >1.
8. Re-read the changed region after writing.
9. Run the smallest relevant test.

## Patch failure
If an oldText patch says "not found", STOP. Do not invent another oldText. Read the actual file and re-anchor the patch.
