# Test SEPARATOR block marker  regex for jupyter extension for vs code

from py2nb.py2nb import SEPARATOR


def test_match():
    """jupyter for vs SEPARATOR convention"""
    assert(SEPARATOR.match('#%%'))   # As documented
    assert(SEPARATOR.match('# %%'))
    assert(SEPARATOR.match('#  %%'))


def test_nomatch():
    assert(SEPARATOR.match(' #%%') is None)
    assert(SEPARATOR.match('#% %') is None)
    assert(SEPARATOR.match('# % %') is None)
