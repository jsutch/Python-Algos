class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self,value):
        """
        Somethis is borked in which self.head has no value
        """
        if self.head is None:
            self.head = Node(value)
            print(value)
            return True
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = Node(value)
            print(value)
            return True

    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            cursor = self.head.value
            self.head = None
            return cursor
        else:
            cursor = self.head.value
            self.head = self.head.next
            return cursor

    def print(self):
        if self.head is None:
            print('No stack head, quitting')
            return False
        print("stack elements are")
        cursor = self.head
        while cursor.next is not None:
            print(cursor.value, end=">>")
            cursor = cursor.next
        print(cursor.value, end="<<")

    def top(self):
        return self.head

    def size(self):
        cursor = self.head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def find(self, key):
        if self.head is not None:
            cursor = self.head
            while cursor.next.value != key:
                cursor = cursor.next
                if cursor.next ==  None:
                    print(f'{key} not found in list')
                    return False
            print(f'found {key}')
            return True
        else:
            print('List is empty')
            return False

    def remove(self, key):
        if self.head is not None:
            cursor = self.head
            while cursor.next.value != key:
                cursor = cursor.next
                if cursor.next ==  None:
                    print(f'{key} not found in list')
                    return False
            cursor.next = cursor.next.next
            return key
        else:
            print('List is empty')
            return False

    def prepend(self,value):
        if self.head is not None:
            new = Node(value)
            cursor = self.head
            new.next = cursor
            self.head = new
            return value
        else:
            print('list is empty')
            return False

    def append(self, value):
        if self.head is not None:
            new = Node(value)
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = Node(value)
            print(value)
            return True
        else:
            self.head = Node(value)
            return value

    def replace(self, key, value):
        if self.head is not None:
            cursor = self.head
            while cursor.next.value != key:
                cursor = cursor.next
                if cursor.next == None:
                    print(f'{key} not found in list')
                    return False
            new = Node(value)
            cursor.next.value = value
            return value

    def insertbefore(self,key, value):
        if self.head is not None:
            cursor = self.head
            while cursor.next.value != key:
                cursor = cursor.next
                if cursor.next ==  None:
                    print(f'{key} not found in list')
                    return False
            new = Node(value)
            new.next = cursor.next
            cursor.next = new
            return value

    def insertafter(self, key, value):
        if self.head is not None:
            cursor = self.head
            while cursor.next.value != key:
                cursor = cursor.next
                if cursor.next ==  None:
                    print(f'{key} not found in list')
                    return False
            new = Node(value)
            new.next = cursor.next.next
            cursor.next.next = new
            return value

    def printreverse(self):
        reverse = []
        cursor = self.head
        while cursor.next is not None:
            reverse.append(cursor.value)
            cursor = cursor.next
        reverse.append(cursor.value)
        return reverse[::-1]

