from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

#This function demonstrates splitting a singly linked list into evens and odds
def main():
    print("---- Split Evens and Odds ----")
    #This creates a SplitEvensOdds instance and builds a list
    seo = SplitEvensOdds()
    seo.build_forward_list([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    print("Original list:")
    seo.display()

    #This splits the list into evens and odds
    evens_list, odds_list = seo.split_evens_odds()

    #This displays the resulting lists
    print("\nEvens list:")
    evens_list.display()

    print("Odds list:")
    odds_list.display()

    #This shows that the original list is now empty
    print("\nAfter splitting, the original list:")
    seo.display()
    
if __name__ == "__main__":
    main()

