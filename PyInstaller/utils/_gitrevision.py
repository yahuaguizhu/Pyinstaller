#
# The content of this file will be filled in with meaningful data
# when creating an archive using `git archive` or by downloading an
# archive from github, e.g. from github.com/.../archive/develop.zip
#
rev = "14b6e6564"     # abbreviated commit hash
commit = "14b6e65642e4b07a4358bab278019a48dedf7460"  # commit hash
date = "2018-12-31 01:05:54 -0600"   # commit date
author = "Loran425 <Loran425@gmail.com>"
ref_names = ""  # incl. current branch
commit_message = """depend: Allow pylib detection when not a dependency of python.exe

If libpython is not detected uses the dependency checker to look for a
dll matching the pattern pythonXY.dll using the same method as
automated detection.

Checks after automated detection and only on windows systems.

Fixes #3942
"""
