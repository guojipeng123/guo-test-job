# -*- coding: utf-8 -*-

import sys


def in_test():
    return sys.argv[1:2] == ['test']
