[app]
title = KivyMD App
package.name = kivymdapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,kivymd

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.gradle_dependencies = 

# Optimization flags
android.release_artifact = apk
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
