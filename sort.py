def quicksort(xs):
    if len(xs) <= 1:
        return xs

    pivot_index = len(xs) // 2
    pivot = xs[pivot_index]
    del xs[pivot_index]

    smaller = [_ for _ in xs if _ <= pivot]
    larger = [_ for _ in xs if _ > pivot]

    return quicksort(smaller) + [pivot] + quicksort(larger)


def mergesort(xs):
    def merge(xs, ys):
        zs = []
        while xs or ys:
            if xs and ys:
                x = xs[0]
                y = ys[0]
                if x <= y:
                    zs += [x]
                    xs = xs[1:]
                else:
                    zs += [y]
                    ys = ys[1:]
            elif xs:
                zs += xs
                break
            elif ys:
                zs += ys
                break
        return zs

    if len(xs) <= 1:
        return xs

    middle_index = len(xs) // 2
    left = xs[:middle_index]
    right = xs[middle_index:]

    return merge(mergesort(left), mergesort(right))


def selectionsort(xs):
    def swap(i, j):
        tmp = xs[i]
        xs[i] = xs[j]
        xs[j] = tmp

    def find_min_index(start_index):
        min_index = start_index
        for i in range(sorted_index, len(xs)):
            if xs[i] < xs[min_index]:
                min_index = i
        return min_index

    for sorted_index in range(len(xs)):
        # Ensure that all xs before `sorted_index` are sorted.
        assert xs[:sorted_index] == sorted(xs[:sorted_index])
        min_index = find_min_index(sorted_index)
        if min_index != sorted_index:
            swap(sorted_index, min_index)

    return xs
