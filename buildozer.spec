[app]
# (App metadata)
title = Dot Column Game
package.name = dotcolumn
package.domain = org.yourname
version = 0.1

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# The main Python file to run (change if your main file has a different name)
source.main = main.py

# List your requirements here (Kivy, Python 3, Cython for build)
requirements = python3,kivy,cython

# Orientation and fullscreen
orientation = portrait
fullscreen = 1

# iOS specific options
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Icon files (optional, update paths if you have icons)
# icon.filename = %(source.dir)s/icon.png

# Permissions (if you need any, leave empty if none)
# android.permissions = INTERNET

# Logging level (debug, info, warning, error)
log_level = info

# Whether to include source code in the final package (0 or 1)
# (set to 0 to reduce package size)
source.include_patterns =

# Additional options can be added as needed
