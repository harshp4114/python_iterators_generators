class Square_Iterator:
    def __init__(self,sequence):
        self._sequence=sequence
        self._index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self._index < len(self._sequence)):
            item=self._sequence[self._index]
            square=item**2
            self._index+=1
            return square
        else:
            raise StopIteration