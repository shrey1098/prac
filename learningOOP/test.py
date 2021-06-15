import random


class Arr:

    def __init__(self):
        self.arr = []
        for i in range(100):
            self.arr.append(int(i))

    def rem(self, num):
        self.arr.remove(num)

    def sort(self):
        self.arr.sort()

    def last_number(self):
        last_num = self.arr[-1]
        return last_num

    def missing_num(self):
        n = self.last_number()
        x = n * (n + 1) / 2
        y = sum(self.arr)
        missing_num = x - y

        return int(missing_num)


ar = Arr()
ar.rem(num=random.randrange(1, 100))
ar.sort()
print(ar.missing_num())

