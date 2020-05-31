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

    def __predecessor(self, node):
        return self.get_max(node.left)

    def __get_nodes_as_list(self):
        elements = [self.root]
        start = 0
        end = len(elements)
        counter = 0
        while counter < self.size:
            for i in range(start, len(elements)):
                left = None
                right = None
                if elements[i]:
                    counter += 1
                    left = elements[i].left
                    right = elements[i].right
                elements.append(left)
                elements.append(right)
            start = end
            end = len(elements)
            counter += 1
        return self.__generate_values_list(elements)

    def __remove_node_with_two_children(self, node, target_val):
        """
        We swap the target element value with its predecessor's value.
        At this point we need to remove the target element's predecessor
        but because we have swapped the values and by which have created the
        violation we cannot rely on the get() method to get the node by val
        due to it works with a tree with no violation.
        Thus need to detect the corresponding removal method here
        considering that the predecessor does not have right leaf.
        """
        predecessor = self.__predecessor(node)
        print(f'predecessor: {predecessor.val}')
        if predecessor.parent is node:
            node.val = node.left.val
            # node.left.val = target_val
            node.left = node.left.left
            return
        node.val = predecessor.val
        predecessor.val = target_val
        if not predecessor.left:
            self.__remove_node_with_no_child(predecessor)
        else:
            self.__remove_predecessor_with_child(predecessor)

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
    def __generate_values_list(elements):
        """ docstring for __generate_elements_list """
        for key, val in enumerate(elements):
            if val:
                # print(f'key, val: {key, val.val}')
                elements[key] = val.val
            else:
                # print(f'key, val: {key, "____"}')
                elements[key] = '____'
        return elements

    @staticmethod
    def __remove_node_with_no_child(node):
        print('__remove_node_with_no_child')
        if node.val > node.parent.val:
            node.parent.right = None
        else:
            node.parent.left = None
        print('node.parent', node.parent.val)
        print('node.parent.left', node.parent.left)

    @staticmethod
    def __remove_node_with_one_child(node):
        print('__remove_node_with_one_child')
        last_node = node.left if node.left else node.right
        if node.val > node.parent.val:
            node.parent.right = last_node
        else:
            node.parent.left = last_node
        last_node.parent = node.parent

    @staticmethod
    def __remove_predecessor_with_child(node):
        print('__remove_predecessor_with_child')
        last_node = node.left
        node.parent.left = last_node
        last_node.parent = node.parent

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

    def get(self, val):
        current = self.root
        while current:
            if val == current.val:
                return current
            if val > current.val:
                # we go to the right
                if current.right:
                    current = current.right
                else:
                    return None
            else:
                # we go to the left
                if current.left:
                    current = current.left
                else:
                    return None
        else:
            return None

    def get_min(self, node=None):
        if not node:
            node = self.root
        if node:
            while node:
                if not node.left:
                    break
                node = node.left
            return node
        else:
            return None

    def get_max(self, node=None):
        if not node:
            node = self.root
        if node:
            while node:
                if not node.right:
                    break
                node = node.right
            return node
        else:
            return None

    def remove(self, node_val):
        node = self.get(node_val)
        if not node:
            return
        rebalancing_node = self.get_min()
        if rebalancing_node == node:
            print('node is min element')
            rebalancing_node = self.get_max()
        print('rebalancing_node', rebalancing_node.val)

        if not node.left and not node.right:
            # remove leaf node
            self.__remove_node_with_no_child(node)
        elif node.left and node.right:
            # remove node with 2 children
            self.__remove_node_with_two_children(node, node_val)
        else:
            # remove node with 1 child
            self.__remove_node_with_one_child(node)
        self.size -= 1

        self.__check_balance(rebalancing_node)

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

    tree.level_order_traverse()
    tree.in_order_traverse()

    print("\nMinimum value is", tree.get_min().val)
    print("Maximum value is", tree.get_max().val)

    print("Get node with value 21:", tree.get(21))
