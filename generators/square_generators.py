def Square_generators(sequence):
    for item in sequence:
        yield item**2

for item in Square_generators([1,2,3,4,5,6,7]):
    print(item)        

print("\n",50*'/',"\n")

sqr_generator_exp=(x**2 for x in [1,2,3,4,5,6,7])
for item in sqr_generator_exp:
    print(item)