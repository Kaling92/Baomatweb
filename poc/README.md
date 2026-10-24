# A11y Observer Lab

This is a controlled, observation-only Android sample for studying the mechanics discussed in the supplied 2025 thesis. It receives a small set of accessibility events and traverses the accessibility-node tree **only for the lab application's own package** (`edu.example.a11ylab`). It logs aggregate counts for nodes, clickable nodes, and editable nodes. It does not log node text, content descriptions, view identifiers, screenshots, or input values; does not write observations to storage or send them over a network; and does not perform clicks, gestures, global actions, overlays, permission changes, or other UI actions.

This is deliberately not an implementation of malware behavior. In particular, it does not reproduce phishing, tapjacking, credential collection, security-setting interference, Restricted Settings circumvention, or privilege escalation. The user must enable the service through Android Settings, and the service configuration is restricted to this app's package.

## Relation to the source thesis

Fekadu's thesis reports static analysis of Android APKs using Apktool, JADX, JEB, Kavanoz, and FlowDroid, followed by TinyBERT/XGBoost classification of API-call patterns. Dynamic runtime analysis is explicitly outside its scope. This module is a safe, supplementary emulator demonstration of event delivery and node-tree traversal; it does not reproduce the thesis's static-analysis pipeline, malware corpus, FlowDroid dataset, or classifier results. The repository's replication-first acquisition and run procedure is in [`../report/replication_protocol.md`](../report/replication_protocol.md). Refer to [`../literature_review/summary.md`](../literature_review/summary.md) for detailed source attribution and limitations.

## Requirements

Use Android Studio with Android SDK Platform 35 and JDK 17 or later. The Android Gradle Plugin is 8.7.3 and requires Gradle 8.9 or later when building from the command line. Create a fresh Android 13 or 14 emulator (API 33 or 34) with no personal accounts or data. The project has no third-party app dependencies. The APK's `minSdk` is 26 and `targetSdk` is 35.

## Build and install

Open the `poc` directory in Android Studio, allow Gradle project sync, select an API 33/34 emulator, and build the `app` debug variant. Alternatively, from a PowerShell terminal in `poc`, run:

```powershell
gradle :app:assembleDebug
adb devices
adb install -r .\app\build\outputs\apk\debug\app-debug.apk
adb shell am start -n edu.example.a11ylab/.MainActivity
```

If Gradle is not installed, build the debug variant from Android Studio instead. Connect only an emulator intended for this lab; do not install this sample on a personal or production device.

## Enable and observe the service

Enable the service explicitly in the emulator UI by opening **Settings → Accessibility → Installed/Downloaded apps → Lab-only UI observer** and accepting the operating system's disclosure. Labels vary by emulator image. On Android 13 or later, if the emulator marks the sideloaded app as restricted, open the app's **App info** screen, use its overflow menu to allow restricted settings, then return to Accessibility and enable the service. This is a deliberate user-mediated system step. Do not use `adb shell settings put secure enabled_accessibility_services` or similar commands to bypass the confirmation flow.

Return to the lab app, tap **Update lab status**, and use the following commands to inspect the app-scoped diagnostic output:

```powershell
adb logcat -c
adb logcat -s A11yObserver:I
```

The log reports event type, the fixed lab package name, aggregate node counts, and whether the bounded traversal stopped early. It must not contain the contents of the sample input or other displayed text. If logs appear unexpectedly broad, disable the service immediately in Settings and verify that the XML's `android:packageNames` remains `edu.example.a11ylab`.

## Stop and remove

Disable the service in Android Settings before uninstalling. Then stop the app and remove the package:

```powershell
adb shell am force-stop edu.example.a11ylab
adb uninstall edu.example.a11ylab
```

## Files and safety properties

`app/src/main/res/xml/accessibility_service_config.xml` limits observed package events to the lab app and declares only window-state, window-content, click, and focus events. `AccessibilityObserverService.kt` bounds traversal at 100 nodes and depth 12 and emits no node content. `MainActivity.kt` supplies a synthetic screen with a dummy text field and controls. Keep the package filter intact and do not add text extraction, persistence, network transmission, automated actions, or tests against third-party applications.
