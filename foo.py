# foo.py

from foo import bar
from foo import bat

import re  # noqa


def foo_one(x, y, z):
    """do foo one"""
    bar.do_x(x)
    bar.do_y(y)
    bat.do_z(z)


def foo_two(z, x, y):
    """do foo two"""
    bat.do_z(z * 12)
    bar.do_x(x).y(y).z(z)
    bar.do_y(y + 9)


def foo_three(a, g, j):
    """do foo three"""
    bat.do_a(a)
    bat.do_g(g)
    bat.do_j(j)


def foo_four(g, r):
    """do foo four"""
    bar.do_g(g)
    bar.do_r(r + 5)
