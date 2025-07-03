[app]
# App metadata
title = Dot Column Game
package.name = dotcolumn
package.domain = org.yourname
version = 0.1

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py

# Requirements - add anything your app uses here
requirements = python3,kivy,cython

# Orientation and fullscreen
orientation = portrait
fullscreen = 1

# iOS specific options
ios.codesign.allowed = False
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Logging level: debug, info, warning, error
log_level = info

# Permissions (add if needed)
# android.permissions = INTERNET

# Icon (set your own icon file if you have one)
# icon.filename = %(source.dir)s/icon.png

# Preset app categories (optional)
# android.category = GAME

# Whether to include source code in the package (0 or 1)
# source.include_patterns =

# Other Buildozer options can go here as needed
