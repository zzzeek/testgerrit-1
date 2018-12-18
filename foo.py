# foo.py

from foo import bar
from foo import bat


def foo_one(x, y):
    """do foo one"""
    bar.do_x(x)
    bar.do_y(y)


def foo_two(z, q, x, y):
    """do foo two"""
    bat.do_z(z)
    bat.do_q(q)
    bar.do_x(x)
    bar.do_y(y)


def foo_three(a, g, h):
    """do foo three"""
    bat.do_a(a)
    bar.do_g_one(g)
    bat.do_h(h)


def foo_four(g, r):
    """do foo four"""
    bar.do_g(g)
    bar.do_r(r + 5)
