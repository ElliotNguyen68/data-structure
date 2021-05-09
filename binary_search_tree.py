class BST:
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None

    def insert_right(self, value):
        new_node = BST(value)
        self.right = new_node

    def insert_left(self, value):
        new_node = BST(value)
        self.left = new_node

    def travel_right(self, node):
        return node.right

    def travel_left(self, node):
        return node.left

    def insert(self, value):
        if self.data==None:
            self.data=value
            return
        if value > self.data:
            if self.right is None:
                self.insert_right(value)
                return
            else:
                self.right.insert(value)
                return
        if value <= self.data:
            if self.left is None:
                self.insert_left(value)
                return
            else:
                self.left.insert(value)
                return

    def __str__(self):
        return "{}".format(self.data)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self)
        if self.right is not None:
            self.right.inorder()

    def inorder_traverse(self):
        res=[]
        if self.left is not None :
            res=self.left.inorder_traverse()
        res.append(self.data)
        if self.right is not None:
            res+=self.right.inorder_traverse()
        return res

    def find(self, value):
        if value == self.data: return True
        # if self.right is None and self.left is None:return False
        if value < self.data and self.left is not None:
            return self.left.find(value)
        if value > self.data and self.right is not None:
            return self.right.find(value)
        return False

    def get_height(self):
        if self.right is None and self.left is None:
            return 0
        if self.right is None:return self.left.get_height()+1
        if self.left is None: return self.right.get_height()+1
        return max(self.left.get_height()+1,self.right.get_height()+1)

bst = BST(9)
bst.insert(3)
bst.insert(2)
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(7)
bst.insert(9)
bst.insert(8)
bst.insert(11)
bst.insert(13)
bst.insert(12)
bst.insert(10)
bst.insert(15)
bst.insert(14)
# bst.inorder()
print(bst.find(9))
print(bst.get_height())
print(bst.inorder_traverse())

