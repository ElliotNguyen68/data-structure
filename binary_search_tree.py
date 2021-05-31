import sys

sys.setrecursionlimit(1500)


class bst:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

    def add(self, val):
        if self.data is None:
            self.data = val
            return
        if val <= self.data:
            if self.left:
                self.left.add(val)
            else:
                new_tree = bst(val)
                self.left = new_tree
        if val > self.data:
            if self.right:
                self.right.add(val)
            else:
                new_tree = bst(val)
                self.right = new_tree
        return

    def find(self, val):
        if self.data == val: return True
        if val < self.data:
            if self.left:
                return self.left.find(val)
        if val > self.data:
            if self.right:
                return self.right.find(val)
        return False

    def find_node(self, val):
        if self.data == val: return self
        if val < self.data:
            if self.left:
                return self.left.find_node(val)
        if val > self.data:
            if self.right:
                return self.right.find_node(val)
        return bst()

    def find_father_of(self, father, val):
        if self.data == val:
            return father
        if self.data > val:
            if self.left:
                return self.left.find_father_of(self, val)
        if self.data < val:
            if self.right:
                return self.right.find_father_of(self, val)
        return bst()

    def find_minimum(self):
        tmp = self
        while tmp.left is not None:
            # print(tmp)
            tmp = tmp.left
        return tmp

    def get_height(self):
        if self.left is None and self.right is None:
            return 0
        if self.left is None and self.right is not None:
            return self.right.get_height() + 1
        if self.right is None and self.left is not None:
            return self.left.get_height() + 1
        return max(self.left.get_height() + 1, self.right.get_height() + 1)

    def remove(self, father, val):
        if self.data == val:
            # print(self)
            if self.left is None and self.right is None:
                # print(father)
                if father.left is not None and father.left.data == val:
                    # print("asd")
                    father.left = None
                    return

                if father.right is not None and father.right.data == val:
                    # print("sd")
                    father.right = None
                    return
                # print("dmdjfm")

            if self.left and not self.right:
                tmp = self.left
                self.data = tmp.data
                self.left = tmp.left
                self.right = tmp.right
                return
            if self.right and not self.left:
                tmp = self.right
                self.data = tmp.data
                self.right = tmp.right
                self.left = tmp.left
                return

            if self.left and self.right:
                mini_right = self.right.find_minimum()
                self.right = mini_right.right
                mni_right = None
                return
                # minimum_right=None
            # print(val)
        else:
            if val < self.data:
                if self.left:
                    self.left.remove(self, val)
            if val > self.data:
                if self.right:
                    self.right.remove(self, val)
        return

    def __str__(self):
        if self.data is None: return "None"
        if self.left is None and self.right is not None:
            return "{} ,right:{}".format(self.data, self.right.data)
        if self.left is not None and self.right is None:
            return "{} ,left:{}".format(self.data, self.left.data)
        if self.left is not None and self.right is not None:
            return "{} ,left: {}, right: {}".format(self.data, self.left.data, self.right.data)
        return "{}".format(self.data)


heap = bst(99999999999999999999999999)
heap.add(99999999999999999999999779)
heap.add(9999999999999998999999999)
heap.add(999999999999999999999998)
#
# heap.add(28)
# heap.add(25)
# heap.add(27)
# heap.add(49)
# print(heap.find_father_of(bst(),49))
# print(heap.find_node(49))
# heap.remove(bst(),49)
# print(heap.find_node(28))

# print(heap.find_node(49))
# print(heap.find_minimum())
# heap.remove(25)
# print(heap.find_node(28))
# print(heap.find_node(27))
# print(heap.find_node(49))
# print(heap.find_node(25))
# heap.remove(28)
# print(heap.find_node(28))
# print(heap.find_node(27))
# print(heap.find_node(49))
# print(heap.find_node(25))


# print(heap.find_minimum())
# heap.add(4)
# heap.add(9)
# heap.remove(4)
# print(heap.find_node(4))
# print(heap.find_minimum().data)
# heap.add(9)
# heap.add(12)
# heap.add(1)
# heap.add(3)
# heap.add(4)
# heap.add(6)
# heap.add(7)
# heap.add(1)
# heap.add(2)
# heap.add(3)
# heap.add(3)
# heap.add(10)
# heap.add(12)
# heap.add(11)
# heap.add(5)
# heap.add(7)
# heap.add(13)
# heap.add(15)
# heap.add(16)
# heap.add(14)
# heap.add(15)
# heap.remove(16)
# heap.remove(9)
# print(heap.find_node(13))
# print(heap.find_node(15))
# print(heap.find_node(10))
# print(heap.find_node(52))
# print(heap)
# print(heap.find(32))
# print(heap.find(3))
# print(heap.find(22))
# print(heap.find(9))
# node=heap.find_node(1)
# print(node)
# print(heap.find_node(3))
# print(node.left.data,node.right.data)
# print(heap.find_father_of(bst(),3))
# heap.remove(13)
# heap.remove(14)
# heap.remove(6)
# print(heap.find_node(7))
# print(heap.find_node(12))
# print(heap.find_node(15))
# print(heap.find_node(7))
# print(heap.find_minimum())
# print(heap.get_height())
# print(5)
# print(5)


