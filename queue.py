class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        # if self is not None:
        return "{}".format(self.data)


class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_head = self.head
        while cur_head.next is not None:
            cur_head = cur_head.next
        cur_head.next = new_node

    def __str__(self):
        head=self.head
        while head is not None:
            print(head)
            head=head.next
        return ''


class queue(linked_list):
    def front(self):
        return self.head

    def enqueue(self, data):
        queue.add(self,data)

    def dequeue(self):
        if self.head is None: return
        tmp = self.head.next
        self.head = tmp
        return


a = linked_list()
a.add(7)
a.add(5)
a.add(6)
a.add(2)
a.add(10)
a.add(15)
a.add(23)
a.add(2)
# print(a)
b=queue()
b.add(7)
b.add(10)
b.add(2)
b.add(5)
b.add(76)
b.add(8)
b.add(1)
b.add(45)
print(b)
print(b.front())
b.enqueue(9)
print(b)
b.dequeue()
print(b)

