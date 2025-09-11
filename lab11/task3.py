# 🚀 Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

# 🔗 Singly Linked List class with core operations
class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next:
                current = current.next
            # Link the last node to the new node
            current.next = new_node

    def delete_value(self, value):
        if self.head is None:
            return  # List is empty, nothing to delete

        # If the value is at the head
        if self.head.data == value:
            # Move head to the next node, effectively removing the first node
            self.head = self.head.next
            return

        # Traverse to find the node before the one to delete
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            # Skip the node with the matching value by updating the pointer
            current.next = current.next.next

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# 🧪 Test Cases
if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After insertions:", ll.traverse())  # [10, 20, 30]

    # Delete middle value
    ll.delete_value(20)
    print("After deleting 20:", ll.traverse())  # [10, 30]

    # Delete head
    ll.delete_value(10)
    print("After deleting 10:", ll.traverse())  # [30]

    # Delete non-existent value
    ll.delete_value(100)
    print("After trying to delete 100:", ll.traverse())  # [30]

    # Delete last remaining node
    ll.delete_value(30)
    print("After deleting 30:", ll.traverse())  # []

    # Insert after deletion
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    print("After re-inserting:", ll.traverse())  # [40, 50]