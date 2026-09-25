---
name: android-apk-analysis
description: Analyze Android APK structure, manifest, DEX, native libraries, assets, endpoints, and startup flow for offline reconstruction.
---
# Android APK Analysis

1. Inventory AndroidManifest.xml, classes*.dex, lib/*/*.so, assets, res, META-INF and native data/config.
2. Determine the actual ABI used.
3. Trace startup: manifest -> Application/activity -> native loading -> network/bootstrap.
4. Search exact strings for URLs, hosts, ports, API paths, class names, errors, state names and asset identifiers.
5. Cross-reference DEX/Java/Kotlin with native .so.
6. Record exact filenames, offsets, symbols and commands.
7. Never claim an endpoint or protocol from a single string.
8. Never rewrite smali/Java wholesale when one method is enough.
