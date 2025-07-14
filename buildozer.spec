[app]

# (str) Title of your application
title = NFC Reader & Writer PRO2

# (str) Package name
package.name = nfcwriterpro2

# (str) Package domain (needed for android/ios packaging)
package.domain = org.nfctools

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 2.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==master, https://github.com/kivymd/KivyMD/archive/master.zip,pyjnius==1.6.1,android

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,pyc

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .buildozer, .git, __pycache__, .vscode, buildozer_env, buildozer-env

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.jpg,*.log,build_*.bat,build_*.sh,*.md

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]*)['"]\nversion.filename = %(source.dir)s/main.py

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) python-for-android specific python version to use
python.version = 3.9

# (str) Android SDK version to use
android.sdk = 33

# (str) Android build-tools version to use (compatible with API 33)
android.build_tools = 33.0.2

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Python Service
android.service_main_class = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
android.theme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
android.whitelist = 

# (str) Path to a custom whitelist file
android.whitelist_src = 

# (str) Path to a custom blacklist file
android.blacklist_src = 

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
android.add_jars = 

# (list) List of Java files to add to the project (can be java or a
# directory containing the files)
android.add_src = 

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
android.add_aars = 

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
android.gradle_dependencies = 

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
android.add_compile_options = 

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
android.gradle_repositories = 

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
android.add_packaging_options = 

# (list) Java classes to add as activities to the manifest.
android.add_activities = 

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
android.ouya.category = APP

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
android.manifest.intent_filters = templates/AndroidManifest.tmpl.xml

# (str) launchMode to set for the main activity
android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
android.add_libs_armeabi = 

# (list) Android additional libraries to copy into libs/armeabi-v7a
android.add_libs_armeabi_v7a = 

# (list) Android additional libraries to copy into libs/arm64-v8a
android.add_libs_arm64_v8a = 

# (list) Android additional libraries to copy into libs/x86
android.add_libs_x86 = 

# (list) Android additional libraries to copy into libs/x86_64
android.add_libs_x86_64 = 

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
android.backup_rules = 

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
android.manifest_placeholders = 

# (bool) Skip byte compile for .py files
android.no_byte_compile_python = False

# (str) The format used to package the app for release mode (aab or apk).
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aab).
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
