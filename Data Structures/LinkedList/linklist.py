# Linked list example


# The Node class
# Stores data field, named val
# Single next field; singly linked list
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# Linked list class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0  # Count keeps track of number of nodes in the list

    def get_count(self):
        return self.count

    def insert(self, data):
        # Insert items at the head of the list
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node  # head points to new node
        self.count += 1  # Update count

    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()  # otherwise check next node
        return None

    def deleteAt(self, index):
        if index > self.count - 1:  # Check if index is within the number of existing nodes in the list
            return
        if index == 0:  # If deleting the head node, set the new head node to what the current head node is pointing at
            self.head = self.head.get_next()
        else:
            tempIndex = 0
            node = self.head
            # Want the node right before the one that's being deleted, since the next pointer must be fixed
            while tempIndex < index - 1:
                node = node.get_next()
                tempIndex += 1

            # For the node right before the one that needs to be deleted, set the next field to point to the node that's after the one that will be deleted
            node.set_next(node.get_next().get_next())
            self.count -= 1  # Decrement counter

    def dump_list(self):  # prints contents of the list
        tempNode = self.head
        while(tempNode != None):
            print("Node ", tempNode.get_data())
            tempNode = tempNode.get_next()


# Create a linked list
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)

itemList.dump_list()

# Exercise the list
print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(13))
print("Finding item: ", itemList.find(78))

# Delete an item
itemList.deleteAt(3)
print("Item count: ", itemList.get_count())
print("Finding items: ", itemList.find(38))
itemList.dump_list()
