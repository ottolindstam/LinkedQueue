class Node():
    """Node class"""
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

    def __str__(self):
        return str(self.value)


class LinkedQ():
    """Linked queue class"""

    def __init__(self):
        """Create empty linked queue object"""
        self.__first=None
        self.__last=None
        self.__size=0

    def __str__(self):
        """String behaviour, returns string of first node's value"""
        return str(self.__first)

    def enqueue(self, ele):
        """Enqueue behaviour, adds node conatining parameter value to the back
        of the queue"""
        self.new=Node(ele,None)
        self.__size+=1
        if self.isEmpty():
            self.__first=self.new
            self.__last=self.new
        else:
            self.__last.next=self.new
            self.__last=self.__last.next

    def dequeue(self):
        """Returns the value of the first node in the queue and removes the node"""
        if self.isEmpty()==False:
            self.__size-=1
            self.__poped=self.__first.value
            self.__first=self.__first.next
            return self.__poped
        else:
            if self.__last != None:
                return self.__last.value
                self.__last = None
                self.__size=0

    def isEmpty(self):
        """Returns True if queue is empty, otherwise False"""
        if self.__first == None:
            return True
        else:
            return False

    def size(self):
        """Returns number of nodes/elements in queue"""
        return self.__size
