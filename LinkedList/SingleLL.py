
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

    def insert_at_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        len = 0
        temp = self.head
        while temp:
            len += 1
            temp = temp.next

        return len

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid idnex")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Indvalid index')
        if index == 0:
            self.insert_at_first(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                break
            temp = temp.next
            count += 1


class CLL:
    def __init__(self):
        self.head = None


l = SLL()

l.insert_at_first(0)
l.insert_at_first(65)
l.display()
print("\n")
l.insert_at_end(90)
l.insert_at_end(200)
l.insert_values([1, 2, 4, 6, 73])
l.display()
print("\n")
l.get_length()
l.remove_at_index(3)
l.insert_at_index(3, 9999)
l.display()
