def binary_search(xs, it):
    if not xs:
        return None
    mid = len(xs) // 2
    if xs[mid] == it:
        return mid
    if xs[mid] > it:
        return binary_search(xs[:mid], it)
    else:
        return mid + binary_search(xs[mid:], it)


def binary_search_iterative(xs, it):
    start = 0
    end = len(xs)
    while start != end:
        mid = start + (end - start) // 2
        if xs[mid] == it:
            return mid
        elif xs[mid] > it:
            end = mid
        else:
            start = mid


def binary_search_predicate(start, end, pred):
    while start != end:
        mid = start + (end - start) // 2
        if pred(mid):
            end = mid
        else:
            start = mid + 1

    if not pred(start):
        return None

    return start
