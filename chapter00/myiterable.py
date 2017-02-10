class MyIterable:

    def __init__(self, max_num):
        self.max_num = max_num
        self.current_num = 0

    def __iter__(self):
       return self

    def __next__(self):
        num = self.current_num
        if self.current_num < self.max_num:
            self.current_num += 1
            return num
        else:
            raise StopIteration()

iterable = MyIterable(3)
for i in iterable:
    print(i)
