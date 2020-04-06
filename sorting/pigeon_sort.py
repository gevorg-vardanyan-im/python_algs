"""
    This is an implementation of Pigeon Hole Sort.
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
    random_list = random.sample(range(0, 100), 10)
    random.shuffle(random_list)
    print('Random list:', random_list)
    print('Sorted list:', pigeon_sort(random_list))
