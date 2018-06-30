"""

Author : Robin Phoeng
Date : 21/06/2018

"""

from Bar import *

"""
Creates templates of bars

Standard bar, 2 boxes of size 1 2

Consequence bar, 3 boxes of size 2 4 6
"""
def bar_default(name):
    """
    Returns a bar of size 1, 2
    :param name: the name of the bar
    :return:
    """
    b = Bar(name)
    b.add_box(Box(1))
    b.add_box(Box(2))
    return b

def bar_consequence(name):
    """
    Returns a bar of size 2, 4, 6
    :param name: the name of the bar
    :return:
    """
    b = Bar(name)
    b.add_box(Box(2))
    b.add_box(Box(4))
    b.add_box(Box(6))
    return b