import math
import sys
import os
import heapq


class Minheap():
    """docstring for MinHeap"""

    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.items = [None] * self.capacity

    def __get_left_child_index(self, parent_index):
        """ docstring for function
        :type parent_index: int
        """
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index):
        """ docstring for function
        :type parent_index: int
        """
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index):
        """ docstring for function
        :type child_index: int
        """
        return int((child_index - 1) / 2)

    def __has_left_child(self, index):
        """ docstring for function
        :type index: int
        """
        return self.__get_left_child_index(index) < self.size

    def __has_right_child(self, index):
        """ docstring for function
        :type index: int
        """
        return self.__get_right_child_index(index) < self.size

    def __has_parent(self, index):
        """ docstring for function
        :type index: int
        """
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index):
        """ docstring for function """
        return self.items[self.__get_left_child_index(index)]

    def __right_child(self, index):
        """ docstring for function """
        return self.items[self.__get_right_child_index(index)]

    def parent(self, index):
        """ docstring for function
        :type index: int
        """
        return self.items[self.__get_parent_index(index)]

    def __extra_capacity(self):
        """ docstring for function """
        if self.size == self.capacity:
            self.items.extend([None] * self.capacity)
            self.capacity *= 2

    def peek(self):
        """ docstring for function """
        if self.size == 0:
            raise ValueError
        return self.items[0]

    def poll(self):
        """ docstring for function """
        if self.size == 0:
            raise ValueError
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.size -= 1
        self.heapify_down()
        return item

    def heapify_down(self):
        """ docstring for function """
        index = 0
        while self.__has_left_child(index):
            smaller_child_index = self.__get_left_child_index(index)
            if (self.__has_right_child(index) and
                self.__right_child(index) < self.__left_child(index)):
                smaller_child_index = self.__get_right_child_index(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.items[index], self.items[smaller_child_index] =\
                    self.items[smaller_child_index], self.items[index]
            index = smaller_child_index

    def heapify_up(self):
        """ docstring for function """
        index = self.size - 1
        while (self.__has_parent(index) and
               self.parent(index) > self.items[index]):
            swap_cand = self.__get_parent_index(index)
            self.items[swap_cand], self.items[index] =\
                self.items[index], self.items[swap_cand]
            index = self.__get_parent_index(index)

    def add(self, item):
        """ docstring for function """
        self.__extra_capacity()
        self.items[self.size] = item
        self.size += 1
        print("=> ", item, self.items)
        self.heapify_up()
        print("   ", item, self.items)

    def traverser(self, index):
        """ docstring for function """
        depth_indent = "  "
        template = "{line_indent}{parent}\n{left}{line_indent} {right}"
        # template = "left: {left} -> parent: {parent} -> right: {right}"
        if self.items[index]:
            left = self.__left_child(index) or "x"
            parent = self.parent(index) or "x"
            right = self.__right_child(index) or "x"
            print(template.format(
                line_indent=depth_indent,
                left=left,
                parent=parent,
                right=right))

    def get_last_item_index(self):
        """ docstring for function """
        for key, val in enumerate(self.items):
            if not val:
                break
        if key > 0:
            key -= 1
        return key

    def get_levels(self):
        """ docstring for function """
        return int(math.log(len(self.items) + 1, 2) - 1)


if __name__ == '__main__':
    min_heap = Minheap()
    min_heap.add(2)
    min_heap.add(4)
    min_heap.add(6)
    min_heap.add(1)
    min_heap.add(5)
    min_heap.add(3)
    min_heap.add(9)
    min_heap.add(11)
    min_heap.add(12)
    min_heap.add(13)
    min_heap.add(14)
    min_heap.add(15)
    min_heap.add(16)

    for i in range(7):
        print("parent: {", i, min_heap.items[i], "} ^", min_heap.parent(i))

    print(min_heap.items)
    last_index = min_heap.get_last_item_index()
    levels = min_heap.get_levels()
    print(last_index)
    print(levels)

    # todo determine start and end indexes for each level
    traversal_str = ""
    bottom_bound = pow(2, levels) - 1
    top_bound = pow(2, levels +1) - 1
    for i in range(bottom_bound, top_bound):
        traversal_str += ((str(min_heap.items[i]) or ".") + "     ")
        # print("\t", i, min_heap.items[i])

    traversal_str += "\n    "
    bottom_bound = pow(2, levels - 1) - 1
    top_bound = pow(2, levels - 1 +1) - 1
    for i in range(bottom_bound, top_bound):
        traversal_str += ((str(min_heap.items[i]) or ".") + "             ")
        # print("\t", i, min_heap.items[i])
    traversal_str += "\n"

    traversal_str += "\n          "
    bottom_bound = pow(2, levels - 2) - 1
    top_bound = pow(2, levels - 2 +1) - 1
    for i in range(bottom_bound, top_bound):
        traversal_str += (str(min_heap.items[i]) + "                          ")
        # print("\t", i, min_heap.items[i])
    traversal_str += "\n"

    print(traversal_str)
