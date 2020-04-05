"""
This is quick sort algorithm which considers the duplications.
"""


def quick_sort(items):
    """ docstring for function """
    if len(items) <= 1:
        return items

    pivot = items.pop()
    lessers, equallers, greaters = [], [], []

    for i in items:
        if i < pivot:
            lessers.append(i)
        elif i == pivot:
            equallers.append(i)
        else:
            greaters.append(i)
    equallers.append(pivot)

    return quick_sort(lessers) + equallers + quick_sort(greaters)


print(quick_sort([3, 5, 1, 2, 3, 6, 9, 0, 7]))
