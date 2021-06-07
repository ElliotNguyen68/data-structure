class node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __str__(self):
        res = "{}".format(self.data)
        return res


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, val):
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node

    def add(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            return
        if self.tail is None:
            self.tail = new_node
            self.head.next = self.tail
            return
        self.tail.next = new_node
        self.tail = new_node

    def __str__(self):
        tmp = self.head
        res = ""
        print(tmp)
        while tmp.next:
            print(tmp.next)
            tmp = tmp.next
        return res


a = linked_list()
a.add(8)
a.add(5)
a.add(3)
a.add(1)
a.add(7)
a.add(32)
a.add(1)
a.add(8)
a.add(5)
a.add(3)
a.add(1)
a.add(7)
a.add(32)
a.add(1)

print(a)

# print(node(9))