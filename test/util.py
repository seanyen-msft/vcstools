import os
import shutil
import stat
import urllib

def _touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def _on_rmtree_error(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def _rmtree(path):
    shutil.rmtree(path, onerror = _on_rmtree_error)

def _pathname2url(pathname):
    if (hasattr(urllib, 'pathname2url')):
        from urllib import pathname2url
    else:
        from urllib.request import pathname2url
    return pathname2url(pathname)