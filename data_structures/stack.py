class Stack(object):
    """This class represents the stack."""

    def __init__(self, limit):
        self.limit = limit
        self.stack = [None] * limit
        # this variable shows the last added item position in the stack
        self.last_position = -1

    def push(self, item):
        """ Push an element to the top of the stack. """
        if self.is_full():
            raise IndexError('___the stack is full___')
        self.last_position += 1
        self.stack[self.last_position] = item

    def pop(self):
        """ Pop the top element and returns it. """
        if self.is_empty():
            raise IndexError('___the stack is empty___')
        item = self.stack[self.last_position]
        self.last_position -= 1
        return item

    def peak(self):
        """ Peek at the top-most element of the stack. """
        if self.is_empty():
            raise IndexError('___the stack is empty___')
        return self.stack[self.last_position]

    def size(self):
        """ Return the size of the stack. """
        return self.last_position + 1

    def is_empty(self):
        """ Check if the stack is empty. """
        return self.last_position == -1

    def is_full(self):
        """ Check if the stack is full. """
        return self.limit == self.last_position + 1


if __name__ == '__main__':
    import random
    stack_size = 5
    stack = Stack(stack_size)
    random_list = [random.randint(-100, 100) for x in range(stack_size)]
    print(random_list)

    print("\nCurrent size:", stack.size())
    print("Max size:", stack.limit)
    print("Is stack empty:", stack.is_empty())
    for i in random_list:
        print("push =>", i)
        stack.push(i)

    print("\nCurrent size:", stack.size())
    print("Max size:", stack.limit)
    print("Is stack empty:", stack.is_empty())
    print("Top element:", stack.peak())

    for _ in random_list:
        print("pop <=", stack.pop())

    print("\nCurrent size:", stack.size())
    print("Max size:", stack.limit)
    print("Is stack empty:", stack.is_empty())
