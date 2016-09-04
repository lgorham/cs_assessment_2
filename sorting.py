from collections import deque
#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    
    for i in xrange(len(lst) - 1):
        # Len - 1 because when we get to the last item, we already know it is in place

        # Optimize so won't have to continue iterating through if list is already ordered
        made_swap = False

        for item in xrange(len(lst) - (1 + i)):

            # Uses how many items we've already checked in order to optimize by not recomparing those
            if lst[item] > lst[item + 1]:

                # Pair out of order, swap
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
                made_swap = True

        if not made_swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    sorted_list = []

    # If both lists still have items to be sorted
    while list1 and list2:
        first_1 = list1[0]
        first_2 = list2[0]
        if first_1 < first_2:
            sorted_list.append(first_1)
            list1.pop(0)
            # Using pop from index 0 - inefficent runtime and should be improved

        if first_2 < first_1:
            sorted_list.append(first_2)
            list2.pop(0)

    # To address case where one list is empty, while the other list has items left
    while list1:
        first1 = list1.pop(0)
        sorted_list.append(first1)

    while list2:
        first2 = list2.pop(0)
        sorted_list.append(first_2)

    return sorted_list

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    # Base case - list of length 1 is sorted
    if len(lst) == 1:
        return lst

    # Splitting in half to eventually reduce down to base case
    split = int(len(lst) / 2)

    right = merge_sort(lst[split:])
    left = merge_sort(lst[:split])

    sorted_list = []

    # While both lists remain
    while right and left:
        if right[0] < left[0]:
            sorted_list.append(right.pop(0))

        elif left[0] < right[0]:
            sorted_list.append(left.pop(0))

    # When one list remains
    while right:
        sorted_list.append(right.pop(0))

    while left:
        sorted_list.append(left.pop(0))

    return sorted_list




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print