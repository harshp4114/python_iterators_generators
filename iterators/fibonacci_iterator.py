class Fibonacci_Iterator:

    def __init__(self,stop=10):
        self._index=0
        self._current=0
        self._next=1
        self._stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if(self._index<self._stop):
            self._index+=1
            fib_num=self._current
            self._current,self._next=(self._next,self._current+self._next)
            return fib_num
        else:
            raise StopIteration
