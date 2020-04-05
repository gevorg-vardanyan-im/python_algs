class Node(object):
    """
    This class represents the node element of the tree.
    The node can be either root or a leaf element.
    """

    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


class AvlTree(object):
    from math import log2

    def __init__(self):
        self.root = None
        self.size = 0

    def __add(self, parent, node):
        if node.val > parent.val:
            # we go to right
            if not parent.right:
                parent.right = node
                node.parent = parent
                self.size += 1
            else:
                self.__add(parent.right, node)
        else:
            # we go to left
            if not parent.left:
                parent.left = node
                node.parent = parent
                self.size += 1
            else:
                self.__add(parent.left, node)
        self.__check_balance(node)

    def __check_balance(self, node):
        if abs(self.height(node.left) - self.height(node.right)) > 1:
            self.__rebalance(node)
            if not node.parent:
                return
            self.__check_balance(node.parent)

    def __rebalance(self, node):
        if (self.height(node.left) - self.height(node.right)) > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotation(node)
            else:
                node = self.left_right_rotation(node)
        else:
            if self.height(node.right.left) > self.height(node.right.right):
                node = self.right_rotation(node)
            else:
                node = self.left_right_rotation(node)
        if not node.parent:
            self.root = node

    def __height(self):
        return int(self.log2(self.size))

    def __in_order_traverse(self, node):
        if node.left:
            self.__in_order_traverse(node.left)

        if node.val < self.root.val:
            print("on root left    > ", node.val, end="")
            if node.parent:
                print('  parent > {}'.format(node.parent.val))
            else:
                print()
        elif node.val > self.root.val:
            print("on root right   < ", node.val, end="")
            if node.parent:
                print('  parent > {}'.format(node.parent.val))
            else:
                print()
        else:
            # we allow an elements' duplication
            # see insert() method
            print("root element(s) _ ", node.val)

        if node.right:
            self.__in_order_traverse(node.right)

    @staticmethod
    def left_rotation(node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        return tmp

    @staticmethod
    def right_rotation(node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        return tmp

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            self.size += 1
            return
        self.__add(self.root, node)

    def left_right_rotation(self, node):
        """
        node is thr grandparent node
        left rotation should be around parent
        right rotation should be around grandparent
        """
        node.left = self.left_rotation(node.left)
        return self.right_rotation(node)

    def right_left_rotation(self, node):
        """
        node is thr grandparent node
        right rotation should be around parent
        left rotation should be around grandparent
        """
        node.right = self.right_rotation(node.right)
        return self.left_rotation(node)

    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left) + 1
        right_height = self.height(node.right) + 1
        return max(left_height, right_height)

    def print_level_order(self):
        for i in range(1, self.__height() + 2):
            self.print_given_level(self.root, i)
            print()

    def print_given_level(self, root, level):
        if root is None:
            return root
        if level == 1:
            print(root.val, end=' _ ')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    def in_order_traverse(self):
        if self.root.val:
            print('---------- in order traverse ----------')
            self.__in_order_traverse(self.root)


if __name__ == '__main__':
    # import random
    # random_list = list(range(20))
    # random.shuffle(random_list)
    random_list = [5, 8, 6, 4, 2, 9, 7, 1, 3, 0, 20, 15, 25, 24, 23, 22, 30, 12]
    tree = AvlTree()
    print(random_list)
    for i in random_list:
        tree.add(i)
    print('size:', tree.size)
    tree.print_level_order()
    tree.in_order_traverse()
