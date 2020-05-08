from data_structures.stacks_and_queues.stack import Stack


class QueueViaStack():
    """
        This class represents the queue implementation via stacks.
        It consists of two stacks.
        One of them should be responsible for pushing an elements to the queue,
        other one for the elements' popping.
    """

    def __init__(self):
        # self.limit = limit
        # hardcoded the limit as of now
        self.push_stack = Stack(5)
        self.pop_stack = Stack(5)

    def push(self, item):
        """ Push an element to the end of the queue. """
        self.push_stack.push(item)

    def pop(self):
        """ Pop the first element and return it. """
        if self.pop_stack.is_empty():
            while self.push_stack.size() > 1:
                self.pop_stack.push(self.push_stack.pop())
            return self.push_stack.pop()
        else:
            return self.pop_stack.pop()

    def peek(self):
        """ Peek at the first element of the queue. """
        if not self.pop_stack.is_empty():
            return self.pop_stack.peek()
        elif not self.push_stack.is_empty():
            return self.push_stack.entries[0]
        else:
            raise IndexError('___the queue is empty___')

    def size(self):
        """ Return the size of the queue. """
        return self.push_stack.size() + self.pop_stack.size()


if __name__ == '__main__':
    import random
    queue = QueueViaStack()
    # initial_elements = 5
    # random_list = [random.randint(-100, 100) for x in range(initial_elements)]
    random_list = [-16, -100, -49, 32, -97]
    print(random_list)

    for i in random_list:
        print("\npush =>", i)
        queue.push(i)
        print("size:", queue.size(), " top:", queue.peek())

    # pop first two items
    for _ in range(2):
        print("\npop <=", queue.pop())
        print("size:", queue.size(), " top:", queue.peek())

    # push new items
    for i in [55, 88]:
        print("\npush =>", i)
        queue.push(i)
        print("size:", queue.size(), " top:", queue.peek())

    # pop remaining items
    for _ in range(8):
        print("\npop <=", queue.pop())
        size = queue.size()
        print(f'size: {size}', end='  ')
        if size == 0:
            print('\nThe queue is empty.')
            break
        print("top:", queue.peek())
