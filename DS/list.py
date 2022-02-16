class List:
    """List implementation"""

    def __init__(self, data):
        self.elements = []
        if data is not None:
            self.elements.append(data)
        self.length = len(self.elements)

    def is_empty(self):
        if self.length == 0:
            raise Exception("Empty List")

    def __len__(self):
        return self.length

    def __repr__(self):
        if self.length > 0:
            return " -> ".join(list(map(str, self.elements)))
        else:
            return "Empty List"

    def add_last(self, value):
        """Add element at the end"""
        self.elements.append(value)
        self.length += 1

    def add_first(self, value):
        """Add element at the start"""
        self.elements.insert(0, value)
        self.length += 1

    def remove_last(self):
        """Remove the last element"""
        self.is_empty()
        self.length -= 1
        return self.elements.pop()

    def remove_front(self):
        """Remove the first element"""
        self.is_empty()
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
