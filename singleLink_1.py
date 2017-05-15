#coding=utf-8

class node():
    def __init__(self,_data=None,_next=None):
        self._data=_data
        self._next = _next

    def getNext(self):
        return self._next

    def setNext(self,_next):
        self._next = _next

class  singleLink():
    def __init__(self,head=None):
        self._head=head
        self._size = 0

    def append(self,item):
        head = self._head
        while head.getNext() is not None:
            head = head.getNext()
        head.setNext(node(item))
        self._size +=1


if __name__=="__main__":
    singleLink = singleLink(node())
    singleLink.append(1)
    print(singleLink._head.getNext()._data)
