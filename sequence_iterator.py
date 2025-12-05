class Sequence_Iterator():
    def __init__(self,sequence):
        print("INIT CALLED ")
        self._sequence=sequence
        self._index=0

    def __iter__(self):
        print("ITER CALLED",self)
        return self
    
    def __next__(self):
        print("NEXT CALLED")
        if(self._index < len(self._sequence)):
            item=self._sequence[self._index]
            self._index+=1
            return item
        else:
            raise StopIteration
        
        