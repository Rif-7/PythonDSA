class Node(): 
    def __init__(self, value, after, before):
        self.value = value
        self._after = after
        self._before = before


    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

class DoublyLinkedList():
    def __init(self):
        self._size = 0
        self._head = Node(None, None, None)
        self._tail = Node(None, None, None)
        self._head._after = self._tail
        self._tail._before = self._head

    def add_last(self, new):
        self._insert_between(self._tail, self._tail._before, new)
        self._size += 1
        return new
    
    def add_first(self, new):
        self._insert_between(self._head, self._head._after, new)
        self._size += 1
        return new
    
    def remove_last(self):
        last = self._tail._before

        self._tail._before = last._before
        last._before._after = self._tail
        size -= 1
        return None

    def _insert_between(self, first, second, new):
        new._before = first
        new._after = second

        first._after = new
        second.before = new
