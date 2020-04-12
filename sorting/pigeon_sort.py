"""
    Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists
    of elements where the number of elements (n) and the length of the
    range of possible key values (N) are approximately the same.
    Worst-case performance	O ( N + n ) ,
        where N is the range of key values and n is the input size.

    The pigeonhole algorithm works as follows:
    1.  Given an array of values to be sorted, set up an auxiliary array of
        initially empty "pigeonholes," one pigeonhole for each key through
        the range of the original array.
    2.  Going over the original array, put each value into the pigeonhole
        corresponding to its key, such that each pigeonhole eventually
         contains a list of all values with that key.
    3.  Iterate over the pigeonhole array in order, and put elements from
        non-empty pigeonholes back into the original array.
"""


def pigeon_sort(array):
    minimum = min(array)
    maximum = max(array)

    # Compute the variables
    holes_range = maximum - minimum + 1
    holes = [0 for _ in range(holes_range)]
    holes_repeat = [0 for _ in range(holes_range)]

    # Make the sorting.
    for i in range(len(array)):
        index = array[i] - minimum
        if holes[index] != array[i]:
            holes[index] = array[i]
            holes_repeat[index] += 1
        else:
            holes_repeat[index] += 1

    # Makes the array back by replacing the numbers.
    index = 0
    for i in range(holes_range):
        while holes_repeat[i] > 0:
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1
    return array


if __name__ == '__main__':
    import random

    random_list = [random.randint(14,20) for x in range(20)]
    print('Random list:', random_list)
    print('Sorted list:', pigeon_sort(random_list))
