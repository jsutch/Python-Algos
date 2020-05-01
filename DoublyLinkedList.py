class Node(object):
    """
    initialize node
    """
    def __init__(self, data):
        self.head = data
        self.next = None
        self.prev = None


class Stack(object):
    """
    initiaize head
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode

    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self):
        return self.head.data

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printstack(self):
        print("Stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end=">>")
            temp = temp.next


n [269]: stack = Stack()

In [270]: [stack.push(random.randint(1,100)) for x in range(10)]
Out[270]: [None, None, None, None, None, None, None, None, None, None]

In [271]: [stack.push(random.randint(1,100)) for x in range(10)]
Out[271]: [None, None, None, None, None, None, None, None, None, None]

In [272]: stack.printstack()
Stack elements are:
47>>56>>89>>57>>35>>96>>37>>1>>81>>18>>84>>15>>59>>1>>6>>57>>63>>68>>82>>68>>
In [273]: stack.pop()
Out[273]: 47

In [274]: stack.printstack()
Stack elements are:
56>>89>>57>>35>>96>>37>>1>>81>>18>>84>>15>>59>>1>>6>>57>>63>>68>>82>>68>>
In [275]: stack.top()
Out[275]: 56

In [276]: stack.size()
Out[276]: 19

In [277]: stack.pop()
Out[277]: 56

In [278]: stack.size()
Out[278]: 18


