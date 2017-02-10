def get_counter():
    i = 0
    def increment_counter():
        nonlocal i
        i += 1
        return i
    return increment_counter

counter = get_counter()
print(counter())  # => 1
print(counter())  # => 2
print(counter())  # => 3
