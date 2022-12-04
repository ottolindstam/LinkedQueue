from array import array

class ArrayQ:
    """Queue data structure based on pythons array calss"""

    def __init__(self, type='i'):
        """Create ArrayQ object of int type"""
        self.__type=type
        self.__myQ=array(str(self.__type))

    def __str__(self):
        """String behaviour, returns string of the array representing the queue"""
        return str(__myQ)

    def enqueue(self, ele):
        """Add parameter element """
        self.__myQ.append(int(ele))

    def dequeue(self):
        """Remove and return the first element of the queue"""
        return self.__myQ.pop(0)

    def isEmpty(self):
        """Return True if queue is empty, otherwise False"""
        if len(self.__myQ==0):
            return True
        else:
            return False

    def size(self):
        """Retrun length of queue"""
        return len(self.__myQ)
