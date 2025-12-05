from sequence_iterator import Sequence_Iterator

print("BEFORE FOR LOOP")
nums=Sequence_Iterator([1,2,3,4,5])
for a in nums:
    print("item is : ",a)

print("AFTER FOR LOOP")

print("BEFORE While LOOP")
it=Sequence_Iterator([1,2,3,4,5])
print(it)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("ITERATION COMPLETE")
        break        

print("AFTER WHILE LOOP")
