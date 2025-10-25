from singly_linked_list import SinglyLinkedList

#This main program tests the SinglyLinkedList class
def main():
    #This code tests building a forward list, deleting nodes, building a backward list deleting nodes, non-recursive reverse print, and removing all occurrences of a value
    print("---- Build a forward list ----")
    sll = SinglyLinkedList()
    sll.build_forward_list([10, 20, 30, 40, 50])
    sll.display()

    #This code tests deleting the first, last, and interior nodes
    sll.remove(10)
    print("Delete the first node:", end=" ")
    sll.display()

    #This code tests deleting the last node
    sll.remove(50)
    print("Delete the last node:", end=" ")
    sll.display()

    #This code tests deleting an interior node
    sll.remove(30)
    print("Delete the interior node:", end=" ")
    sll.display()

    #This code tests building a backward list and deleting nodes
    print("---- Build a backward list ----")
    sll2 = SinglyLinkedList()
    sll2.build_backward_list([10, 20, 30, 40, 50])
    sll2.display()

    #This code tests deleting the first, last, and interior nodes
    sll2.remove(50)
    print("Delete the first node:", end=" ")
    sll2.display()

    #This code tests deleting the last node
    sll2.remove(10)
    print("Delete the last node:", end=" ")
    sll2.display()

    #This code tests deleting an interior node
    sll2.remove(30)
    print("Delete the interior node:", end=" ")
    sll2.display()

    #This code tests non-recursive reverse print
    print("---- Non-recursive reverse print test ----")
    sll3 = SinglyLinkedList()
    sll3.build_forward_list([10, 20, 30, 40, 50])
    print("Insertion order:", end=" ")
    sll3.display()
    print("Reverse order (recursive):", end=" ")
    sll3.display_reverse()
    print("Reverse order (non-recursive):", end=" ")
    sll3.display_reverse_nr()

    #This code tests removing all occurrences of a value
    print("---- Remove all test ----")
    sll4 = SinglyLinkedList()
    sll4.build_forward_list([1, 2, 4, 6, 1, 3, 6])
    sll4.display()

    #This code tests removing all occurrences of a value
    print("Removing 1 and all duplicates:", end=" ")
    sll4.remove_all(1)
    sll4.display()

    #This code tests removing all occurrences of a value
    print("Removing 6 and all duplicates:", end=" ")
    sll4.remove_all(6)
    sll4.display()

if __name__ == "__main__":
    main()

