class node:

    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return "{}".format(self.data)

class singly_linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data_in_node):
        self.size += 1
        new_node = node(data_in_node)
        if self.head is None:
            self.head = new_node
            return
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = new_node

    def at(self, pos):
        if pos + 1 > self.size: return None
        head = self.head
        while pos > 0:
            head = head.next
            pos -= 1
        return head

    def insert_at(self, pos, new_data):
        if pos < 0:
            print('position must be non-negative integer')
            return
        self.size += 1
        new_node = node(new_data)
        if pos == 0:
            tmp_node = self.head
            self.head = new_node
            new_node.next = tmp_node
            return
        head = self.head
        while pos > 1 and head.next:
            head = head.next
            pos -= 1
        real_next_node = head.next
        head.next = new_node
        new_node.next = real_next_node

    def remove(self, pos):
        if self.size <= 0:
            print("linked list is currently empty")
            return
        if self.size < pos + 1:
            print("position needed to be deleted must be within {}".format(self.size - 1))
            return
        self.size -= 1
        if pos == 0:
            self.head = self.head.next
            return
        head = self.head
        while pos > 1:
            head = head.next
            pos -= 1
        next_node = head.next
        head.next = next_node.next

    def __str__(self):
        head = self.head
        while head is not None:
            print(head)
            head = head.next
        return ''


# a1=node(5)
a = singly_linked_list()
a.add(5)
a.add(6)
a.add(7)
a.add(45)
# a.add(63)
print(a)
a.insert_at(pos=9, new_data=8)
print(a)
print(a.size)
print(a.at(4))
print()
print(a.at(4))
print()
a.remove(9)
print(a)
