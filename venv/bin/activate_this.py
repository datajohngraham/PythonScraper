"""By using execfile(this_file, dict(__file__=this_file)) you will
activate this virtualenv environment.

######  documentation says  It is different from the import statement in that it does not use the module administration — it reads the file unconditionally and does not create a new module.
##### what does it mean 'not create a new module'
#####  in the execfile above, this_file means "activate_this.py"? 
######   is the dict() method above referring to the dictionary where the module namespace is saved?  
#######  __file__ is set the the full path and name of this 'activate_this.py' file?

This can be used when you must use an existing Python interpreter, not
the virtualenv bin/python
"""

try:
    __file__

except NameError:
    raise AssertionError(
        "You must run this like execfile('path/to/activate_this.py', dict(__file__='path/to/activate_this.py'))")
import sys
import os

old_os_path = os.environ['PATH']
#######   get's the path name of the home directory
os.environ['PATH'] = os.path.dirname(os.path.abspath(__file__)) + os.pathsep + old_os_path
########      gives you the asbolute path of the module, os.pathsep gives the way paths are separated in the OS,
######  for windows it's ;  and then the old_os_path from above
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#######   ?????   gets absolute path of the module, then get the directory of that absolute path.   why is it sent to dirname again?
if sys.platform == 'win32':
    site_packages = os.path.join(base, 'Lib', 'site-packages')
#######   os.path.join intelligently combines paths,  throwing away higher directories that would be redundant
else:
    site_packages = os.path.join(base, 'lib', 'python%s' % sys.version[:3], 'site-packages')
######  ??  seems to add on to end of string 'python' the first two element of sys.version.  why do this only if platform is not win32? 
######  would sys.version[:3] return the python version, like '2.7' 
prev_sys_path = list(sys.path)

import site
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = base
# Move the added items to the front of the path:
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path
