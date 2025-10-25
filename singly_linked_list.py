#This class implements a node for a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#This class implements a singly linked list with various methods
class SinglyLinkedList:
    #This exception is raised when attempting to operate on an empty list
    class EmptyListException(Exception):
        pass
    
    #This exception is raised when a specified node is not found
    class NodeNotFoundException(Exception):
        pass

    #This initializes an empty singly linked list
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    #This method builds a forward list from an iterable
    def build_forward_list(self, iterable):
        for item in iterable:
            self.__append(item)

    #This method builds a backward list from an iterable
    def build_backward_list(self, iterable):
        for item in iterable:
            self.__prepend(item)

    #This method appends a value to the end of the list
    def __append(self, value):
        new_node = Node(value)
        #This handles the case of an empty list
        if self.__head is None:
            self.__head = self.__tail = new_node
        #This handles the case of a non-empty list
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    #This method prepends a value to the start of the list
    def __prepend(self, value):
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        #This handles the case when the list was empty
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1

    #This method inserts a new value after the first occurrence of after_value
    def insert_after(self, after_value, new_value):
        #This handles the case of an empty list
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()

        current = self.__head
        #This searches for the node with after_value
        while current and current.data != after_value:
            current = current.next
        #This handles the case when after_value is not found
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        #This updates the tail if we inserted at the end
        if current == self.__tail:
            self.__tail = new_node
        self.__count += 1

    #This method removes the first occurrence of a value from the list
    def remove(self, value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()

        current = self.__head
        previous = None

        #This searches for the node to remove
        while current and current.data != value:
            previous = current
            current = current.next

        #This handles the case when the value is not found
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()

        #This removes the node
        if previous is None:
            self.__head = current.next
        #This handles removing from the middle or end
        else:
            previous.next = current.next

        #This updates the tail if we removed the last node
        if current == self.__tail:
            self.__tail = previous

        self.__count -= 1

    #This method removes all occurrences of a value from the list
    def remove_all(self, value):
        """Remove all nodes containing the given value."""
        current = self.__head
        previous = None

        #This traverses the list to remove all occurrences
        while current:
            #This checks if the current node needs to be removed
            if current.data == value:
                #This removes the current node
                if previous is None:
                    self.__head = current.next
                #This handles removing from the middle or end
                else:
                    previous.next = current.next

                #This updates the tail if we removed the last node
                if current == self.__tail:
                    self.__tail = previous

                self.__count -= 1
                current = current.next
                continue
            previous = current
            current = current.next

    #This method displays the list in reverse order non-recursively
    def display_reverse_nr(self):
        """Display the list in reverse order (non-recursive using stack)."""
        stack = []
        current = self.__head
        #This pushes all node data onto the stack
        while current:
            stack.append(current.data)
            current = current.next
        reversed_data = " <- ".join(map(str, reversed(stack)))
        print(f"None <- {reversed_data} <- Head")

    #This method displays the list in order
    def display(self):
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Head -> " + " -> ".join(elements) + " -> None")

    #This method displays the list in reverse order recursively
    def display_reverse(self):
        def _reverse_recursive(node):
            return _reverse_recursive(node.next) + [node.data] if node else []
        print("None <- " + " <- ".join(map(str, _reverse_recursive(self.__head))) + " <- Head")

    #This method allows iteration over the list
    def __iter__(self):
        current = self.__head
        #This yields each node's data in order
        while current:
            yield current.data
            current = current.next

    #This method returns the length of the list
    def __len__(self):
        return self.__count

