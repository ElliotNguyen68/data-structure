class heap:
    def __init__(self):
        self.arr = [None]

    def upward(self, pos):
        if pos > 1:
            if self.arr[pos] < self.arr[pos // 2]:
                self.arr[pos], self.arr[pos // 2] = self.arr[pos // 2], self.arr[pos]
                self.upward(pos // 2)

    def toward(self, pos):
        if 2 * pos >= self.size(): return
        if 2*pos+1<self.size():
            if self.arr[2*pos]<self.arr[2*pos+1]:
                if self.arr[pos]>self.arr[2*pos]:
                    self.arr[2 * pos], self.arr[pos] = self.arr[pos ], self.arr[2 * pos]
                    self.toward(2*pos)
            else:
                if self.arr[pos]>self.arr[2*pos+1]:
                    self.arr[2 * pos+1], self.arr[pos] = self.arr[pos ], self.arr[2 * pos+1]
                    self.toward(2*pos+1)
        else:
            if self.arr[pos] > self.arr[2 * pos]:
                self.arr[2 * pos], self.arr[pos] = self.arr[pos], self.arr[2 * pos]
                self.toward(2 * pos)

    def top(self):
        return self.arr[1]

    def pop(self):
        res = self.arr[1]
        self.arr[1] = self.arr[-1]
        self.arr.pop()
        self.toward(1)
        return res

    def add(self, val):
        self.arr.append(val)
        self.upward(self.size() - 1)

    def size(self):
        return len(self.arr)

    def show_me(self):
        for i,x in enumerate(self.arr):
            try:
                print(x,self.arr[2*i],self.arr[2*i+1])
            except:
                print("eror")


    def __str__(self):
        return "{}".format(self.arr)


my_h = heap()
my_h.add(6)
my_h.add(52)
my_h.add(2)
my_h.add(-15)
my_h.add(-5)
my_h.add(32)
my_h.add(56)
my_h.add(36)
my_h.add(22)
my_h.add(5)
my_h.add(15)

my_h.add(15)
my_h.add(322)
my_h.add(12)

print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
print(my_h.pop())
# print(my_h.pop())
# print(my_h.pop())
# print(my_h.pop())
# print(my_h.pop())


