class MyObject:

    def __init__(self, num):
        self.num = num

    def add(self, x):
        self.num += x

    def show(self):
        print(self.num)

o = MyObject(3)
o.show()
o.add(2)
o.show()
o.add(5)
o.show()
