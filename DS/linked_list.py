class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    """Linked list implementation with common insert and remove methods"""

    def __init__(self, nodes=None):
        self.head = None
        self.length = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.length += 1
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                self.length += 1

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.length

    def insert(self, index, node):
        """Insert at a given index"""
        if index - 1 > self.length:
            raise Exception("Given index is larger than the length of LL")

        if index == 0 or self.head == None:
            self.add_first(node)
        elif index == self.length - 1:
            self.add_last(node)
        else:
            prev_node = self.head
            for i in range(1, index - 1):
                if prev_node != None:
                    prev_node = prev_node.next
            if prev_node != None:
                node.next = prev_node.next
                prev_node.next = node
                self.length += 1

    def add_first(self, node):
        """
        Insert at the begining
        """
        node.next = self.head
        self.head = node
        self.length += 1

    def add_last(self, node):
        """
        Insert at end
        """
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        self.length += 1

    def add_after(self, target_node_data, new_node):
        """Adds a new node after the specified node"""
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                return

        raise Exception(f"Node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_node):
        """Adds a new node before the specified node"""
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                self.length += 1
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        """Deletes a specified node"""
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_first(self):
        """Removes first node"""
        if self.head is None:
            raise Exception("List is empty")

        current_node = self.head

        self.head = self.head.next
        current_node = None
        self.length -= 1

    def remove_last(self):
        """Removes last node"""
        if self.head is None:
            raise Exception("List is empty")

        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        self.length -= 1


class FIFO_LL(LinkedList):
    """
    First In First Out Linked List
    """

    def __init__(self, nodes=None):
        super().__init__(nodes)

    def insert(self, val: Node):
        LinkedList.add_last(self, val)

    def remove(self):
        LinkedList.remove_first(self)


class LIFO_LL(LinkedList):
    """
    Last in First Out Linked List
    """

    def __init__(self, nodes=None):
        super().__init__(nodes)

    def insert(self, val: Node):
        LinkedList.add_first(self, val)

    def remove(self):
        LinkedList.remove_first(self)
