def quick_sort(items):
    if len(items) <=1:
        return items
    else:
        pivot = items.pop(0)
        lessers = []
        greaters = []
        for i in items:
            if i <= pivot:
                lessers.append(i)
            else:
                greaters.append(i)
        return quick_sort(lessers) + [pivot] + quick_sort(greaters)


if __name__ == '__main__':
    print(quick_sort([3, 5, 1, 7, 2]))
    print(quick_sort([3, -5, 1, 7, -2]))
