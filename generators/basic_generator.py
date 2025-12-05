# generator function 
def Basic_Generator(sequence):
    for item in sequence:
        yield item

for item in Basic_Generator([1,2,3,4,5,6,7,8]):
    print(item)

print("\n",50*'/',"\n")

# generator expression equivalent to the generator function
generator_expression=(item for item in [1,2,3,4,5,6,7,8])

for item in generator_expression:
    print(item)