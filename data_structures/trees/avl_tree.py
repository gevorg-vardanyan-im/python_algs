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
        left_sub_height = self.height(node.left)
        right_sub_height = self.height(node.right)
        if abs(left_sub_height - right_sub_height) > 1:
            self.__rebalance(node, left_sub_height, right_sub_height)
        if not node.parent:
            return
        self.__check_balance(node.parent)

    def __rebalance(self, node, left_sub_height, right_sub_height):
        parent_node = node.parent
        if (left_sub_height - right_sub_height) > 1:
            # left subtree is bigger than the right subtree
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotation(node)
                if parent_node is not None:
                    parent_node.right = node
            else:
                node = self.left_right_rotation(node)
                if parent_node is not None:
                    parent_node.left = node
        else:
            # right subtree is bigger than the left subtree
            if self.height(node.right.left) < self.height(node.right.right):
                node = self.left_rotation(node)
                if parent_node is not None:
                    parent_node.left = node
            else:
                node = self.right_left_rotation(node)
                if parent_node is not None:
                    parent_node.right = node
        node.parent = parent_node
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
        if tmp.left is not None:
            tmp.left.parent = node

        tmp.left = node
        node.parent = tmp
        return tmp

    @staticmethod
    def right_rotation(node):
        tmp = node.left
        node.left = tmp.right
        if tmp.right is not None:
            tmp.right.parent = node

        tmp.right = node
        node.parent = tmp
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
        node is the grandparent node
        left rotation should be around parent
        right rotation should be around grandparent
        """
        node.left = self.left_rotation(node.left)
        node.left.parent = node
        return self.right_rotation(node)

    def right_left_rotation(self, node):
        """
        node is thr grandparent node
        right rotation should be around parent
        left rotation should be around grandparent
        """
        node.right = self.right_rotation(node.right)
        node.right.parent = node
        return self.left_rotation(node)

    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left) + 1
        right_height = self.height(node.right) + 1
        return max(left_height, right_height)

    def level_order_traverse(self):
        if self.root.val:
            print('\n---------- level order traverse ----------')
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
            print('\n---------- in order traverse ----------')
            self.__in_order_traverse(self.root)


if __name__ == '__main__':
    # the elements below will involve all 4 rotations
    tree = AvlTree()

    tree.add(43)
    tree.add(18)
    tree.add(22)  # left_right rotation on 43
    tree.add(9)
    tree.add(21)
    tree.add(6)  # right rotation on 22 around 18
    tree.add(8)  # left_right rotation on 9
    tree.add(20)
    tree.add(63)
    tree.add(50)  # right_left_rotation on 43
    tree.add(62)  # left rotation on 18 around 22
    tree.add(51)  # right_rotation on 63

    tree.in_order_traverse()
    tree.level_order_traverse()