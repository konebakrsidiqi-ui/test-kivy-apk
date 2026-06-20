[app]

# (string) Title of your application
title = Test Kivy

# (string) Package name
package.name = testkivy

# (string) Package domain (needed for android packaging)
package.domain = org.test

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# (string) Application version
version = 0.1

# (list) Application requirements
# On laisse Kivy s'installer de manière stable avec le Cython configuré plus haut
requirements = python3, kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Accept SDK license without prompting
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
