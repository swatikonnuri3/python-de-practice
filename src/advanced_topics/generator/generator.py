def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
for num in numbers():
    print(num)
#generator with loop
def even_numbers(n):
    for i in range(2,n+1,2):
        yield i
for even in even_numbers(10):
    print(even)