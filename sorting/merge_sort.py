def merge_sort(items):
    def merge_items(left, right):
        result = []
        counter = 0
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left_from_mid = merge_sort(items[:mid])
    right_from_mid = merge_sort(items[mid:])
    return merge_items(left_from_mid, right_from_mid)


if __name__ == '__main__':
    print(merge_sort([2, 4, 1, 3, -9]))