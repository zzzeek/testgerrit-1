# foo.py

from bar import bar
from bar import bat

name = None


def bar_one(x, y):
    bar.do_x(x)
    bar.do_y(y + 7)


def bar_two(z, q):
    bat.do_z(z)
    if name:
        bat.do_q(q)


def bar_two_five(z, q):
    bat.do_z(z)
    bat.do_q(q)


def bar_three(a, g, h):
    bat.do_a(a)
    bat.do_g(g)
    bat.do_h(h)

