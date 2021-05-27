class my_set:
    def __init__(self, a):
        my_map = {}
        res = []
        for x in a:
            my_map[x] = 1
        for x in my_map:
            res.append(x)
        self.list = sorted(res)

    def __str__(self) -> str:
        tmp = '{ '
        for x in self.list:
            tmp += str(x) + ' '
        tmp += '}'
        return "{}".format(tmp)

    def find(self, x):
        a = self.list
        right = len(self.list)
        left = -1
        mid = int((right + left) / 2)
        while left != mid and mid != right:
            if a[mid] == x:
                return True, mid
            if a[mid] > x:
                right = mid
            else:
                left = mid
            mid = int((left + right) / 2)
        return False, mid

    def add(self, num):
        bool, pos = self.find(num)
        if bool == True: return
        self.list.insert(pos + 1, num)

    def size(self):
        return len(self.list)

    def intersection(self, set_b):
        res = []
        for x in self.list:
            if set_b.find(x)[0]:
                res.append(x)
                print(x)
        return res

    def sym_dif(self, set_b):
        res = []
        tmp_set = my_set(self.list)
        for x in set_b.list:
            tmp_set.add(x)
        in_common = self.intersection(set_b)
        for x in tmp_set.list:
            if not my_set(in_common).find(x)[0]:
                res.append(x)
        return res

    def union(self, set_b):
        res = []
        a = self.intersection(set_b)
        b = self.sym_dif(set_b)
        res.extend(a)
        res.extend(b)
        return res

    def minus(self, set_b):
        res = []
        for x in self.list:
            if not set_b.find(x)[0]:
                res.append(x)

    def complement(self):
        res = []
        universe = my_set([i for i in range(101)])
        for x in universe.list:
            if not self.find(x)[0]:
                res.append(x)
        return res


a = my_set([23, 46, 82, 2, 1, 65, 89, 65, 31, 6, 3])
# print(a)
a.add(4)
# print(a)
a.add(3)
# print(a)
a.add(19)
# print(a)
a.add(44)
# print(a)
# print(a.find(1524))
print(a)
b = my_set([5, 6, 3, 21, 78, 54, 1, 2, 36])
print(b)
print(a.intersection(b))
print(a.sym_dif(b))
print(a.union(b))
print(a.complement())