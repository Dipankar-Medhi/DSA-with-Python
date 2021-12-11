
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




def mergeLL(firstLL, secondLL):
    f = firstLL.head
    s = secondLL.head

    ans = SLL()
    while( f != None and s != None):
        if f.data < s.data:
            ans.insert_at_end(f.data)
            f = f.next
        else:
            ans.insert_at_end(s.data)
            s = s.next

    while f != None:
        ans.insert_at_end(f.data)
        f = f.next
    
    while s != None:
        ans.insert_at_end(s.data)
        s = s.next

    return ans

firstLL = SLL()
secondLL = SLL()
firstLL.insert_values([1,3,5])
secondLL.insert_values([1,2,3,4,14])
ans = mergeLL(firstLL, secondLL)
ans.display()