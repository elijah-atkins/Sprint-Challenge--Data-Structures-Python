class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #if node is empty or only has one item and it doesn't link to another node return and do nothing
        if self.head is None or self.head.next_node is None:
            return
        #start at the head
        current = self.head
        #reset prev to NONE for first item
        prev = None
        #as long as something is in the head reverse elements
        while current:
            #set head as current value
            self.head = current
            #save the next node in the next_elemement value
            next_element = current.next_node
            #reverse the next_node to be the current nodes previous node
            current.next_node = prev
            #save current value as prev for next element
            prev = current
            #cycle current to next element until current is empty and breaks the loop
            current = next_element


#testing
# thisList = LinkedList()

# thisList.add_to_head(6)
# thisList.add_to_head(5)
# thisList.add_to_head(3)
# thisList.add_to_head(2)

# print(thisList.head.value)
# print(thisList.head.get_next().value)
# print(thisList.head.get_next().get_next().value)
# print(thisList.head.get_next().get_next().get_next().value)

# thisList.reverse_list(thisList.head, None)

# print(thisList.head.value)
# print(thisList.head.get_next().value)
# print(thisList.head.get_next().get_next().value)
# print(thisList.head.get_next().get_next().get_next().value)
