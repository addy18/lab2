class Node(object):
    def __init__(self, data="", count=1, next=None):
        self.data = data
        self.count = count
        self.next = next

    def print_data(self):
        print("Password: ", self.data, " count: ", self.count)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        curr = self.head
        while curr is not None:
            if curr.data == x:
                curr.count += 1
                return True
            curr = curr.next
        return False

    def list_length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def bubble(self):
        end = None
        while end != self.head:
            start = self.head
            while start.next != end:
                pointer = start.next
                if start.count < pointer.count:
                    start.data, pointer.data = pointer.data, start.data
                    start.count, pointer.count = pointer.count, start.count
                start = start.next
            end = start

    def print_list(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                temp.print_data()
                temp = temp.next

    def merge_sort(self):
        start = self.head
        if start is None or start.next is None:
            return start
        # left = start.splitting()
        left, right = start.spliting()
        left = left.merge_sort()
        right = right.merge_sort()
        return start.merge(left, right)

    def splitting(self):
        curr = self.head
        if curr is None or curr.next is None:
            left = curr
            right = None
            return left, right
        else:
            mid = curr
            temp = curr.next
            while temp is not None:
                temp = temp.next
                if temp is not None:
                    temp = temp.next
                    mid = mid.next
        left = curr
        right = mid.next
        mid.next = None
        return left, right

    def merge(self, left, right):
        result = self.head
        curr = result
        while left and right:
            if left.count > right.count:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left is None:
            curr.next = right
        if right is None:
            curr.next = left
        return result.next

l_list = LinkedList()

stuff = {}
with open(file = "10-million-combos.txt", encoding = "utf-8", errors='ignore') as text:
# with open("pass.txt") as text:
# text = open("test2.txt", "r")
    read = text.readlines()
for line in read:
    password = line.split("  ")
    if l_list.search(password[-1]) == False:
        l_list.append(password[-1])

print("Unsorted :)")
l_list.print_list()
print("-----------------")
print("Bubble :)")
l_list.bubble()
l_list.print_list()
print("-----------------")
print("Merge :)")
# l_list.merge_sort()

# SOLUTION B!!!!!!!!
print("-----------------")
print("dictionary :)")
dict = {}
file = open("test.txt", "r")
second_list = file.readlines()
for elem in second_list:
    row = elem.split("  ")
    if row[-1] in dict:
        dict[row[-1]] = dict[row[-1]] + 1
    else:
        dict[row[-1]] = 1
for i in dict:
    print(dict[i])

