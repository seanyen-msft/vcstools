import os
import shutil
import stat
import urllib

def _touch(path):
    """
    a portable way to create a file for test code.
    """
    with open(path, 'a'):
        os.utime(path, None)

def _on_rmtree_error(func, path, exc_info):
    """
    path contains the path of the file that couldn't be removed
    let's just assume that it's read-only and unlink it.
    """
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def _rmtree(path):
    """
    In some platforms, for example, in Winodws, the shutil.rmtree is not
    able to delete the read-only files. So when it hits this, try the best
    effort to remove the read-only attribute and delete it again.
    """
    shutil.rmtree(path, onerror = _on_rmtree_error)

def _pathname2url(pathname):
    """
    pathname2url shim helper for Python2\3
    """
    if (hasattr(urllib, 'pathname2url')):
        from urllib import pathname2url
    else:
        from urllib.request import pathname2url
    return pathname2url(pathname)

def _urljoin(base, url):
    """
    urljoin shim helper for Python2\3
    """
    if (hasattr(urllib, 'parse')):
        from urllib.parse import urljoin
    else:
        import urlparse
        from urlparse import urljoin
    return urljoin(base, url)

def _get_file_uri(pathname):
    """
    return a normalized file: procotol uri by an absolute local file path
    """
    return _urljoin('file:', _pathname2url(pathname))