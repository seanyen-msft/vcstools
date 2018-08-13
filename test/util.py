import os
import urllib

def _touch(path):
    """
    a portable way to create a file for test code.
    """
    with open(path, 'a'):
        os.utime(path, None)


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
