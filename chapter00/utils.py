def add(x, y):
    return x + y

def retrieve_even_number(nums):
    even_numbers = []
    for i in nums:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
