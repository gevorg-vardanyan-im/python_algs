import sys
import os


class Queue(object):
    """  This class represents the queue with no limit.  """

    def __init__(self):
        self.entries = []

    def push(self, item):
        """ Push an element to the end of the queue. """
        self.entries.append(item)

    def pop(self):
        """ Pop the first element and return it. """
        item = self.entries[0]
        self.entries = self.entries[1:]
        return item

    def peek(self):
        """ Peek at the first element of the queue. """
        return self.entries[0]

    def rotate(self, count):
        """
            Move items from the front to the end of the queue.
            e.g. count = 2
            before rotation:  5, 8, *, *, *, *
            after rotation:   *, *, *, *, 5, 8
        """
        for _ in range(count):
            self.push(self.pop())

    def size(self):
        """ Return the size of the queue. """
        return len(self.entries)


if __name__ == '__main__':
    import random
    queue = Queue()
    initial_elements = 5
    random_list = [random.randint(-100, 100) for x in range(initial_elements)]
    print(random_list)

    print("\nCurrent size:", queue.size())
    for i in random_list:
        print("push =>", i)
        queue.push(i)

    print("\nCurrent size:", queue.size())
    print("Before rotation:", queue.entries)
    queue.rotate(2)
    print("After rotation: ", queue.entries)
    print("Top element:", queue.peek())

    for _ in random_list:
        print("pop <=", queue.pop())

    print("\nCurrent size:", queue.size())
