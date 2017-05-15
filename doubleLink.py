#coding=utf-8

class node():
    def __init__(self,data,_prev=None,_next=None):
        self._prev = _prev
        self._next = _next
        self.data = data

    def getNext(self):
        return self._next

    def setNext(self,_next=None):
        self._next = _next

    def getPrev(self):
        return self._prev

    def setPrev(self,_prev=None):
        self._prev = _prev


class doubleLink():
    def __init__(self,head=None):
        self._head = head
        self._size = 0
    def getSize(self):
        return self._size

    def __getitem__(self,n):
        head = self._head
        for i in range(0,n):
            if head._next is None:
                return None
            head = head._next
        return head.data

    #添加到最后
    def append(self,item):
        if self.isEmpty():
            self._head._next = node(item)
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()
            temp = node(item,current,None)
            current.setNext(temp)
        self._size+=1
    #检查k的值是否存在
    def searchValue(self,k):
        x = self._head
        result = []
        index=0
        while x is not None:
            if x.data==k:
                result.append(index)
            x = x._next
            index+=1
        return result
    #将k插入链表的前端
    def insertValue(self,k):
        head = self._head
        next = head.getNext()
        item = node(k,head,next)
        head._next = item
        next.setPrev(item)
        self._size+=1

    #判断链表是否为空
    def isEmpty(self):
        if self._head==None:
            return True
        return False

if __name__=="__main__":
    doubleLink = doubleLink(node(None))
    for i in range(0,10):
        doubleLink.append(i)
    for i in range(0,10):
        doubleLink.append(i)
    print(doubleLink._head._next._next._next.getPrev().data)
    doubleLink.insertValue(0)
    print(doubleLink.searchValue(0))
    print(doubleLink[2])
