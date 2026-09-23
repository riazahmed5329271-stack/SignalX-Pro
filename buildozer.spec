[app]
title = SignalXPro
android.accept_sdk_license = True

# (str) Package name
package.name = signalxpro

# (str) Package domain (needed for android/ios packaging)
package.domain = org.signalxpro

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (leave empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main

# (list) Application requirements
requirements = python3,kivy,requests,pyjnius,charset-normalizer==3.3.2,urllib3==1.26.18

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#
osx.kivy_version = 2.2.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#android.presplash_color = #FFFFFF
#android.presplash_lottie = "path/to/lottie/file.json"
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
#android.permissions = android.permission.INTERNET

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

#android.ndk_path =
#android.sdk_path =
#android.ant_path =
# android.skip_update = False
# android.accept_sdk_license = False
#android.entrypoint = org.kivy.android.PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity
#android.extra_manifest_xml = ./src/android/extra_manifest.xml
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml
#android.service_class_name = org.kivy.android.PythonService
# android.apptheme = "@android:style/Theme.NoTitleBar"
#android.whitelist =
# android.home_app = False
#android.whitelist_src =
#android.blacklist_src =
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar
#android.add_src =
#android.add_aars =
#android.add_assets =
#android.add_resources =
#android.gradle_dependencies =
# android.enable_androidx = True
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"
#android.add_gradle_repositories =
#android.add_packaging_options =
#android.add_activities = com.example.ExampleActivity
#android.ouya.category = GAME
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png
#android.manifest.intent_filters =
#android.res_xml = PATH_TO_FILE,
#android.manifest.launch_mode = standard
#android.manifest.orientation = fullSensor
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so
#android.wakelock = False
#android.meta_data =
#android.library_references =
#android.uses_library =
#android.logcat_filters = *:S python:D
#android.logcat_pid_only = False
#android.adb_args = -H host.docker.internal
#android.copy_libs = 1

# (list) The Android archs to build for
android.archs = arm64-v8a

# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# android.backup_rules =
# android.manifest_placeholders = [:]
# android.no-byte-compile-python = False
# android.release_artifact = aab
# android.debug_artifact = apk
#android.display_cutout = never

#
# Python for android (p4a) specific
#
#p4a.url =
#p4a.fork = kivy
#p4a.branch = master
#p4a.commit = HEAD
#p4a.source_dir =
#p4a.local_recipes =
#p4a.hook =
# p4a.bootstrap = sdl2
#p4a.port =
#p4a.setup_py = false
#p4a.extra_args =


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
