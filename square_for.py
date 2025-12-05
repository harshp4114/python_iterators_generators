from square_iterator import Square_Iterator

print("before for loop")
iterable=Square_Iterator([1,2,3,4,5])
print(iterable)
try:
    for it in iterable:
        print(it)
except StopIteration:
    print("after for loop")
    
print("before while loop")
iterable=Square_Iterator([1,2,3,45,5])

while True:
    try:
        print(next(iterable))
    except StopIteration:
        print(" after while loop")
        break