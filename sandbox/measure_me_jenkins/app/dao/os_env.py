import os


def os_environ(key, *, default=None):
    if key not in os.environ:
        return default
    return os.environ[key]
