# Singly Linked List

class Node:
    def __init__(self, element):
        self.data = element
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert

    def insert_end(self, element):
        if not self.head:
            self.head = Node(element)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(element)

    def insert_begin(self, element):
        current = self.head
        self.head = Node(element)
        self.head.next = current

    def insert_middle(self, element, position):
        new_node = Node(element)
        current = self.head
        index = 0
        while current.next:
            if index == position:
                swap = current.data
                current.data = new_node.data
                current.next.data = swap
                return
            current = current.next
            index += 1
        current.next = new_node

    def insert_sorted(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            return
        if element < self.head.data:
            swap = self.head
            self.head = new_node
            self.head.next = swap
            return
        current = self.head
        while current.next:
            if element < current.data:
                swap = current.data
                current.data = new_node.data
                current.next.data = swap
                return
            current = current.next
        current.next = new_node

    # Sort

    def sort_list(self):
        current = self.head
        index = None
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    swap = current.data
                    current.data = index.data
                    index.data = swap
                index = index.next
            current = current.next

    # Remove

    def remove_end(self):
        current = self.head
        if current.next:
            while current.next.next:
                current = current.next
            current.next = None
        else:
            self.head = None

    def remove_begin(self):
        self.head = self.head.next

    def remove_element(self, element):
        current = self.head
        if current == None:
            return
        if current.data == element:
            self.head = current.next
        else:
            previous = current
            current = current.next
            while current:
                if current.data == element:
                    previous.next = current.next
                    return
                previous = current
                current = current.next

    # Display

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Search

    def search_position(self, position):
        current = self.head
        index = 0
        while current:
            if index == position:
                print(current.data)
                return
            current = current.next
            index += 1

    def search_element(self, element):
        current = self.head
        index = 0
        while current:
            if current.data == element:
                print(index)
                return
            current = current.next
            index += 1

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def unique_values(self):
        current = self.head
        if not current:
            return
        while current.next:
            if current.data == current.next.data:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next
        return self.head

def merge_lists(nodeA, nodeB):
    new_node = Node(-1)
    merged = new_node
    while(nodeA or nodeB):
        if not nodeA:
            merged.next = nodeB
            break
        if not nodeB:
            merged.next = nodeA
            break
        if(nodeA.data < nodeB.data):
            merged.next = nodeA
            nodeA = nodeA.next
        else:
            merged.next = nodeB
            nodeB = nodeB.next
        merged = merged.next
    if(nodeA):
        merged.next = nodeA
    else:
        merged.next = nodeB
    return new_node.next
