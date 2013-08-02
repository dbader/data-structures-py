import random
from arrays import *


def test_binary_search():
    assert binary_search([], 'a') is None
    assert binary_search(['a'], 'a') == 0
    assert binary_search(['a', 'b'], 'b') == 1
    assert binary_search(['a', 'b', 'c'], 'c') == 2
    assert binary_search_iterative(['a', 'b'], 'b') == 1
    # assert binary_search(['a', 'b', 'c'], 'e') is None
    xs = list(sorted("abcdefghijklmnopqrstuvwxyz0123456789"))
    for _ in range(10):
        it = random.choice(xs)
        assert binary_search(xs, it) == xs.index(it)
        assert binary_search_iterative(xs, it) == xs.index(it)


def test_bs_with_predicate():
    xs = list(sorted("0123456789"))

    def p_geq_3(i):
        return xs[i] >= '3'

    def p_le_5(i):
        return xs[i] < '5'

    assert (binary_search_predicate(0, len(xs) - 1, p_geq_3)
            == xs.index('3'))
    assert (binary_search_predicate(0, len(xs) - 1, p_le_5)
            == xs.index('0'))
