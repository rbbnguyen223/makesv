---
name: game-client-analysis
description: Reconstruct an old online game's client-side state, bootstrap, resource loading, server dependencies, and offline execution path.
---
# Game Client Analysis

Analyze in this order:
1. Startup/bootstrap
2. Configuration
3. Server discovery
4. Authentication/session
5. Resource/CDN loading
6. Game-state initialization
7. UI/state transitions
8. Inventory/character data
9. Save/load behavior
10. Runtime crash after bypasses

For offline reconstruction compare:
- local fake server preserving the original client protocol
- client-side removal/replacement of mandatory online dependencies

Do not choose from intuition. Establish the blocking dependency first.

For every bypass record exact file/function, condition/request, observed failure, proposed replacement and test proving success.
