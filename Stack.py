from LinkedList1 import LinkedList1
class Stack(object):

    def __init__(self):
        self.data = LinkedList1()

    def __str__(self):
        return str(self.data)

    def push(self, item):
        self.data.insert(item)

    def pop(self):
        toPush = self.data.head.getData()
        self.data.delete(toPush)
        return toPush
        

    def isEmpty(self):
        return self.data.head is None

    def size(self):
        return self.data.size()

if __name__ == "__main__":
    myStack = Stack()
    map(lambda x : myStack.push(x), xrange(10))
    print myStack
    print myStack.isEmpty()
    print myStack
    print myStack.pop()
    print myStack
