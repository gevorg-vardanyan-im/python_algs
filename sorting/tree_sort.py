"""
    A tree sort is a sort algorithm that builds a binary search tree
    from the elements to be sorted, and then traverses the tree (in-order)
    so that the elements come out in sorted order.
    Its typical use is sorting elements online:
        after each insertion,
        the set of elements seen so far is available in sorted order.

    Worst-case performance:	O(n²) (unbalanced)
                            O(n log n) (balanced)
    Best-case performance:	O(n log n)
    Average performance:	O(n log n)
    Worst-case space complexity:	Θ(n)
"""


class Node:
    """
    This class represents the node element of the tree.
    The node can be either root or a leaf element.
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                # we go to the left side
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val >= self.val:
                # we go to the right side
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def in_order_traverse(node, met_elements):
    """
    Traverse the tree in order - i.e. left -> parent -> right
    :param node: current node element
    :param met_elements: already met elements list
    :return: does not return any list as it works directly on the received list
    """
    if node:
        in_order_traverse(node.left, met_elements)
        met_elements.append(node.val)
        in_order_traverse(node.right, met_elements)


def tree_sort(unsorted_list):
    """
    Creates a 'binary search tree',
    insert received list into the tree,
    traverse the tree in order and so that creates list of sorted elements
    """

    if len(unsorted_list) == 0:
        return unsorted_list
    root = Node(unsorted_list[0])
    for i in range(1, len(unsorted_list)):
        root.insert(unsorted_list[i])

    traversed_list = []
    in_order_traverse(root, traversed_list)
    return traversed_list


if __name__ == '__main__':
    import random

    random_list = [random.randint(-10, 10) for x in range(20)]
    print('Random list:', random_list)
    print('Sorted list:', tree_sort(random_list))
