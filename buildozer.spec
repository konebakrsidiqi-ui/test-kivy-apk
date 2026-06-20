[app]

title = Test Kivy

package.name = testkivy
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21

android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]

log_level = 2

warn_on_root = 0
