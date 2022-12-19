def bt_to_DLL(root):
    prev, head = None, None

    def convertToDLL(root):

        if root is None:
            return None

        convertToDLL(root.left)
        if prev == None:
            head = root
        # moving prev forward
        else:
            root.left = prev
            prev.right = root

        prev = root
        convertToDLL(root.right)


# ---------------
# merge(fuse) two sorted linked lists
def concatenate_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # use left for previous.
    # use right for next.
    tail1 = head1.left
    tail2 = head2.left

    tail1.right = head2
    head2.left = tail1

    head1.left = tail2
    tail2.right = head1
    return head1


def convert_to_linked_list_rec(root):
    if root is None:
        return None

    list1 = convert_to_linked_list_rec(root.left)
    list2 = convert_to_linked_list_rec(root.right)

    root.left = root.right = root
    result = concatenate_lists(list1, root)
    result = concatenate_lists(result, list2)

    return result


def convert_to_linked_list(root):
    head = convert_to_linked_list_rec(root)
    if head.left is not None:
        head.left.right = None
        head.left = None
    return head


def get_list(head):
    r = []
    if head is None:
        return r

    temp = head
    while True:
        r.append(temp.data)
        temp = temp.right
        if temp is None:
            break

    return r


data = [100, 50, 200, 25, 75, 350, 30, 60]
root = create_BST(data)
head = convert_to_linked_list(root)
v = get_list(head)
print_list(v)
