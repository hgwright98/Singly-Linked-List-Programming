from singly_linked_list import SinglyLinkedList, Node

#This class extends SinglyLinkedList to add a method for splitting evens and odds
class SplitEvensOdds(SinglyLinkedList):
    #This method splits the list into two lists: one with even numbers and one with odd numbers
    def split_evens_odds(self):
        """Split the list into two lists: evens and odds, by reassigning pointers."""
        #This handles the case of an empty list
        if self._SinglyLinkedList__head is None:
            raise SinglyLinkedList.EmptyListException("List is empty")

        #This initializes heads and tails for the new lists
        evens_head = evens_tail = None
        odds_head = odds_tail = None

        #This traverses the original list and separates nodes into evens and odds
        current = self._SinglyLinkedList__head
        while current:
            next_node = current.next
            current.next = None 

            #This checks if the current node's data is even or odd
            if current.data % 2 == 0:
                #This appends to evens list
                if evens_head is None:
                    evens_head = evens_tail = current
                #This handles appending to a non-empty evens list
                else:
                    evens_tail.next = current
                    evens_tail = current
            #This handles the odd case
            else:
                #This appends to odds list
                if odds_head is None:
                    odds_head = odds_tail = current
                #This handles appending to a non-empty odds list
                else:
                    odds_tail.next = current
                    odds_tail = current

            #This moves to the next node in the original list
            current = next_node

        #This clears the original list
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        #This creates new SinglyLinkedList instances for evens and odds
        evens_list = SinglyLinkedList()
        odds_list = SinglyLinkedList()

        #This assigns heads and tails to the new lists
        evens_list._SinglyLinkedList__head = evens_head
        evens_list._SinglyLinkedList__tail = evens_tail
        odds_list._SinglyLinkedList__head = odds_head
        odds_list._SinglyLinkedList__tail = odds_tail

        #This counts the number of nodes in each new list
        count_evens = count_odds = 0
        temp = evens_head
        #This counts nodes in evens list
        while temp:
            count_evens += 1
            temp = temp.next
        temp = odds_head
        #This counts nodes in odds list
        while temp:
            count_odds += 1
            temp = temp.next

        #This sets the counts for the new lists
        evens_list._SinglyLinkedList__count = count_evens
        odds_list._SinglyLinkedList__count = count_odds

        #This returns the two new lists
        return evens_list, odds_list
