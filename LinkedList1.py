class Node(object):

    def __init__(self, data=None, nextVal=None):
        self.data = data
        self.nextVal = nextVal

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextVal

    def setNext(self, newNext):
        self.nextVal = newNext

class LinkedList1(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        acc = ""
        pointer = self.head
        while(pointer is not None):
            acc += str(pointer.data) + " -> "
            newPointer = pointer.getNext()
            pointer= newPointer
        return acc[:-4]  #trim the last arrow

    def insert(self, data):
        newNode = Node(data,self.head)
        self.head = newNode

    def size(self):
        count = 0
        pointer = self.head
        while(pointer is not None):
            newPointer = pointer.getNext()
            pointer= newPointer
            count += 1
        return count

    def search(self, toFind):
        count = 0
        pointer = self.head
        while(pointer is not None):
            if (pointer.data == toFind):
                return count
            newPointer = pointer.getNext()
            pointer= newPointer
            count += 1
        raise ValueError("Data not in list")

    def delete(self,toDelete):
        pointer = self.head
        lastPointer = None
        while(pointer is not None):
            if (pointer.data == toDelete):
                if pointer is self.head:
                    newHead= self.head.getNext()
                    self.head = newHead
                    return
                else:
                    lastPointer.setNext(pointer.getNext())
                    return
            newPointer = pointer.getNext()
            lastPointer = pointer
            pointer= newPointer
if __name__ == "__main__":

    myList = LinkedList1()
    for i in map(lambda x:x**2, range(10)):
        myList.insert(i)

    print myList

    myList.delete(36)

    print myList

    myList.delete(81)

    print myList
    print myList.size()

    

        
