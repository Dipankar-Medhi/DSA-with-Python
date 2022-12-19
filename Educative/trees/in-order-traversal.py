class InOrder:
    def __init__(self, root) -> None:
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    # check if there are any element inside stack
    def hasNext(self):
        if not self.stack:
            return False
        else:
            return True

    def getNext(self):
        if not self.stack:
            return None

        topVal = self.stack[-1]
        del self.stack[-1]

        # add the right node, if any
        temp = topVal.right
        while temp:
            self.stack.append(temp)
            temp = temp.left

        return topVal


def inorder_iterator(root):
    iter = InOrder(root)
    mystr = ""
    while iter.hasNext():
        ptr = iter.getNext()
        mystr += str(ptr.data) + " "

    return mystr
