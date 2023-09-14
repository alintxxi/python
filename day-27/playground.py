def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 6, 7, 52, 8, 9, 18, 41))