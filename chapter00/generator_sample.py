def mygenerator(n):
    for i in range(n):
        yield i

generator = mygenerator(3)
for i in generator:
    print(i)
