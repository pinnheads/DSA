class List:
    """List implementation"""

    def __init__(self, data):
        self.elements = []
        if data is not None:
            self.elements.append(data)
        self.length = len(self.elements)

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length

    def __repr__(self):
        if self.length > 0:
            return "->".join(list(map(str, self.elements)))
        else:
            return "Empty List"

    def add_last(self, value):
        self.elements.append(value)
        self.length += 1

    def add_first(self, value):
        self.elements.insert(0, value)
        self.length += 1

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty List")
        else:
            self.length -= 1
            return self.elements.pop()

    def remove_front(self):
        if self.is_empty():
            raise Exception("Empty List")
        else:
            self.length -= 1
            return self.elements.pop(0)


class FIFO_List(List):
    """First In First Out implementation with List"""

    def insert(self, value):
        List.add_last(self, value)

    def remove(self):
        return List.remove_front(self)


class LIFO_List(List):
    """Last In First Out implementation with List"""

    def insert(self, value):
        List.add_last(self, value)

    def remove(self):
        return List.remove_last(self)
