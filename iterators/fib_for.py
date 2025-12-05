from fibonacci_iterator import Fibonacci_Iterator

print("before for loop")

for it in Fibonacci_Iterator(5):
    print(it)

print("after for loop")

print("before while looop")

iterable=Fibonacci_Iterator(5)

while True:
    try:
        print(next(iterable))
    except StopIteration:
        print("after while loop")
        break
