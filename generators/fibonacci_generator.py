def Fibonacci_generator(stop=10):
    current=0
    next=1
    for i in range(0,stop):
        yield current
        current,next=(next,current+next)

for item in Fibonacci_generator(5):
    print(item)


