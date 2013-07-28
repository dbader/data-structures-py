import random
from sort import quicksort, mergesort, selectionsort

INPUT_ITEMS = [
    'a',
    'ab',
    'aa',
    'abc',
    'abcd',
    'abcde',
    '1234567890',
    'abcdefghijklmnopqrstuvw',
    'aaaaabcccccdefghijklmnopqrstuvw',
]


def run_checks(sort_func):
    def shuffled(l):
        l = list(l)
        random.shuffle(l)
        return l
    for _ in [shuffled(_) for _ in INPUT_ITEMS]:
        assert sorted(_) == sort_func(_)


def test_quicksort():
    run_checks(quicksort)


def test_mergesort():
    run_checks(mergesort)


def test_selectionsort():
    run_checks(selectionsort)
