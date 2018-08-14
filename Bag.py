from LinkedList1 import LinkedList1
class Bag(object):

    def __init__(self):
        self.data = LinkedList1()

    def __str__(self):
        return str(self.data)

    def add(self, item):
        self.data.insert(item)

    def isEmpty(self):
        return self.data.head is None

    def size(self):
        return self.data.size()

if __name__ == "__main__":
    myBag = Bag()
    map(lambda x : myBag.add(x), xrange(10))
    print myBag
    print myBag.isEmpty()
    print myBag.size()
