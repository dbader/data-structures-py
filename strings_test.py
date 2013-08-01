from strings import *


def test_reverse_string():
    assert reverse_string('turbo') == 'obrut'
    assert reverse_string('o') == 'o'
    assert reverse_string('one') == 'eno'
    assert reverse_string('fone') == 'enof'
    assert reverse_string('not,') == ',ton'


def test_first_non_repeated():
    assert first_non_repeated_character('total') == 'o'
    assert first_non_repeated_character('teeter') == 'r'


def test_remove_chars():
    input_str = 'Battle of the Vowels:'
    expected = 'Bttl f th Vwls:'
    assert remove_chars(input_str, 'aeiou') == expected
    assert remove_chars_fast(input_str, 'aeiou') == expected


def test_reverse_words():
    input_str = 'Do or do not, there is no try.'
    expected = 'try. no is there not, do or Do'
    assert reverse_words(input_str) == expected
    assert reverse_words_array(input_str) == expected
    assert reverse_words_inplace(input_str) == expected
