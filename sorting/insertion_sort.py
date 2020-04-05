def insertion_sort(items):
    """ docstring for function """
    for i in range(1, len(items)):
        insertion_index = i
        while (insertion_index > 0 and
                items[insertion_index - 1] > items[insertion_index]):
            items[insertion_index], items[insertion_index - 1] =\
                items[insertion_index - 1], items[insertion_index]
            insertion_index -= 1
    return items


if __name__ == '__main__':
    print(insertion_sort([4, 7, 3, 2, 9]))