class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def add_begin(self, node):
        node.next = self.head
        self.head = node

    def get_size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # def add_after(self, node):   # Treverse needed
    # def add_at_end(self, node):   # Treverse needed

    # for deleting set the next value to None
    # for delete at beginning set self.head -> self.head.next
    # for delete at end, traverse to second last element and set to it's next to None.


l_list = LinkedList()
one = Node(1)
l_list.head = one

second = Node(5)
third = Node(0)
fourth = Node(99)
fifth = Node(4)

l_list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

new_node = Node(69)
l_list.add_begin(new_node)


l_list.display_list()
print("\nSize: ", l_list.get_size())
