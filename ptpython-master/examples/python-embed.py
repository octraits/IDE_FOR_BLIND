#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals

from ptpython.repl import embed


def main():
    embed(globals(), locals(), vi_mode=False)


if __name__ == '__main__':
    main()
