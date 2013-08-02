import collections
import array


def reverse_string(s):
    s = array.array('u', s)
    for i in range(len(s) // 2):
        tmp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = tmp
    return s.tounicode()


def first_non_repeated_character(s):
    """O(2n) == O(n)"""
    char_count_map = collections.defaultdict(lambda: 0)
    for ch in s:  # O(n)
        char_count_map[ch] += 1
    for ch in s:  # O(n)
        if char_count_map[ch] == 1:
            return ch
    return None


def remove_chars(s, remove):
    remove_set = set(remove)  # O(m)
    # n * (O(1) + O(1) == O(n)
    # n times: check for set inclusion and do list.append
    result = [ch for ch in s if not ch in remove_set]
    return ''.join(result)  # O(n)


def remove_chars_fast(s, remove):
    s = list(s)  # Make `s` mutable
    remove_set = set(remove)  # O(m)
    read_index = 0
    write_index = 0
    for read_index in range(len(s)):
        if s[read_index] not in remove_set:
            s[write_index] = s[read_index]
            write_index += 1
    # slice: O(1)
    # join: O(n)
    return ''.join(s[:write_index])


def reverse_words(s):
    words = s.split()  # O(n)
    # reversed: O(1) per Element
    # join: O(n)
    return ' '.join(reversed(words))


def reverse_words_array(s):
    s = array.array('u', s)
    result = array.array('u', ' ' * len(s))
    word_start = None
    word_end = None
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s) - 1:
            word_end = i
            if i == len(s) - 1:
                word_end += 1
        elif word_start is None:
            word_start = i
        if (not word_start is None) and (not word_end is None):
            # We've found a full word at s[word_start:word_end].
            # Now copy it over.
            write_index = len(s) - word_end
            for j in range(word_start, word_end):
                result[write_index] = s[j]
                write_index += 1
            word_start, word_end = None, None
    return result.tounicode()


def reverse_words_inplace(s):
    def reverse_inplace(s, start_index, end_index):
        assert end_index >= start_index
        word_len = end_index - start_index
        for i in range(word_len // 2):
            tmp = s[start_index + i]
            s[start_index + i] = s[start_index + word_len - i - 1]
            s[start_index + word_len - i - 1] = tmp

    s = array.array('u', reversed(s))
    word_start = None
    word_end = None
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s) - 1:
            word_end = i
            if i == len(s) - 1:
                word_end += 1
        elif word_start is None:
            word_start = i
        if (not word_start is None) and (not word_end is None):
            # We've found a full word at s[word_start:word_end].
            # Now reverse it in place it over.
            reverse_inplace(s, word_start, word_end)
            word_start, word_end = None, None
    return s.tounicode()
