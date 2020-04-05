import sys
import os


class Hashmap(object):
    """ Class Hashmap implemented with the list. """

    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        """ This function calculates hash for the given key """
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.size

    def add(self, key, value):
        """
        This function adds or updates
        key-value pair into the hashmap
        """

        key_hash = self._get_hash(key)
        pair = [key, value]
        if not self.map[key_hash]:
            self.map[key_hash] = list([pair])
        else:
            for item in self.map[key_hash]:
                if item[0] == key:
                    item[1] = value
                    return True
                self.map[key_hash].append(pair)
                return True

    def get(self, key):
        """ This function returns an item by given key if it exists. """
        key_hash = self._get_hash(key)
        if self.map[key_hash]:
            for item in self.map[key_hash]:
                if item[0] == key:
                    return item[1]
        return None

    def delete(self, key):
        """ This function removes an item by the given key. """
        key_hash = self._get_hash(key)
        if not self.map[key_hash]:
            return False
        for item, val in enumerate(self.map[key_hash]):
            if self.map[key_hash][item][0] == key:
                self.map[key_hash][item].pop(1)
                return True

    def traverse(self):
        """ This function traverses and prints out the elements of the map. """
        for i in self.map:
            if i:
                print(str(i))


if __name__ == '__main__':
    hamo = Hashmap()
    print(hamo)
    hamo.add('a', 2)
    hamo.add('aa', 22)
    hamo.add('va', 32)
    hamo.add('av', 42)
    hamo.traverse()
    print()
    hamo.delete('vav')
    hamo.traverse()
    print(hamo.get('aaa'))




