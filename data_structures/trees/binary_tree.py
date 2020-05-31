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


class Tree(object):
    """
    This class represents the Binary tree.
    It allows to insert, get, get min and max elements,
    calculate the height of the tree and traverse it.
    """

    from math import log2

    def __init__(self):
        self.root = None
        self.count = 0

    def __add(self, parent, node):
        if node.val > parent.val:
            # we go to right
            if not parent.right:
                parent.right = node
                node.parent = parent
                self.count += 1
            else:
                self.__add(parent.right, node)
        else:
            # we go to left
            if not parent.left:
                parent.left = node
                node.parent = parent
                self.count += 1
            else:
                self.__add(parent.left, node)

    def __get_min(self, node=None):
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

    def __get_max(self, node=None):
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

    def __predecessor(self, node):
        return self.__get_max(node.left)

    def __in_order_traverse(self, node):
        if node.left:
            self.__in_order_traverse(node.left)

        if node.val < self.root.val:
            print("on root left    >  ", node.val, end="")
            if node.parent:
                print('    parent  >  {}'.format(node.parent.val))
            else:
                print()
        elif node.val > self.root.val:
            print("on root right   <  ", node.val, end="")
            if node.parent:
                print('    parent  >  {}'.format(node.parent.val))
            else:
                print()
        else:
            # we allow an elements' duplication
            # see insert() method
            print("root element(s) _  ", node.val)

        if node.right:
            self.__in_order_traverse(node.right)

    # def __level_order_traverse(self, node, recursion=0, elements=None):
    #     if elements is None:
    #         elements = {
    #             "0": [self.root.val],
    #             "1": [],
    #             "2": [],
    #             "3": [],
    #             "4": []
    #         }
    #     recursion += 1
    #     if node.left:
    #         self.__level_order_traverse(node.left, recursion, elements)
    #     if node.val < self.root.val:
    #         try:
    #             elements[str(recursion - 1)].append(node.val)
    #         except Exception:
    #             pass
    #     elif node.val > self.root.val:
    #         try:
    #             elements[str(recursion - 1)].append(node.val)
    #         except Exception:
    #             pass
    #     if node.right:
    #         self.__level_order_traverse(node.right, recursion, elements)
    #     return elements

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

    def __get_nodes_as_list(self):
        elements = [self.root]
        start = 0
        end = len(elements)
        counter = 0
        while counter < self.count:
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

    @staticmethod
    def __remove_node_with_no_child(node):
        if node.val > node.parent.val:
            node.parent.right = None
        else:
            node.parent.left = None

    @staticmethod
    def __remove_node_with_one_child(node):
        last_node = node.left if node.left else node.right
        if node.val > node.parent.val:
            node.parent.right = last_node
        else:
            node.parent.left = last_node
        last_node.parent = node.parent

    @staticmethod
    def __remove_predecessor_with_child(node):
        last_node = node.left
        node.parent.left = last_node
        last_node.parent = node.parent

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            self.count += 1
            return
        self.__add(self.root, node)

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

    def get_min(self):
        return self.__get_min()

    def get_max(self):
        return self.__get_max()

    def remove(self, node_val):
        node = self.get(node_val)
        if not node:
            return

        if not node.left and not node.right:
            # remove leaf node
            self.__remove_node_with_no_child(node)
        elif node.left and node.right:
            # remove node with 2 children
            self.__remove_node_with_two_children(node, node_val)
        else:
            # remove node with 1 child
            self.__remove_node_with_one_child(node)
        self.count -= 1

    def height(self):
        return int(self.log2(self.count))

    def in_order_traverse(self):
        if self.root.val:
            print('---------- in order traverse ----------')
            self.__in_order_traverse(self.root)

    def print_given_level(self, root, level):
        if root is None:
            return root
        if level == 1:
            print(root.val, end='   ')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)


if __name__ == '__main__':
    # import random
    # random_list = list(range(10))
    # random.shuffle(random_list)
    tree = Tree()
    random_list = [4, 0, 8, 1, 7, 6, 9, 2, 5, 3]
    print(random_list)
    for i in random_list:
        tree.add(i)

    print("root:", tree .root.val)
    print("min val:", tree.get_min().val)
    print("max val:", tree.get_max().val)
    print("count:", tree.count)
    print("height:", tree.height())
    tree.in_order_traverse()
