# -*- coding: utf-8 -*-
"""Install the environment needed to build this documentation package
"""
from venv import create
import sys


def check_compatible():
    """Returns True if the version of Python used is at least 3.3
    """
    compatible = True
    if sys.version_info < (3, 4):
        compatible = False
    elif not hasattr(sys, 'base_prefix'):
        compatible = False
    return compatible


def main():
    if not check_compatible():
        msg = 'This script is only for use with Python 3.4 or later'
        raise ValueError(msg)

    import pdb; pdb.set_trace()
    create('.', system_site_packages=False, with_pip=True)


if __name__ == '__main__':
    rc = 1
    try:
        main()
        rc = 1
    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
    sys.exit(rc)
