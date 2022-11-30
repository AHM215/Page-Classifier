
###############################################################################################
##                                        TEAM 3                                             ##
###############################################################################################

# 1) selection sort
def selection_sort(unsorted_list):
    """
    Sort unsorted list using selection sort
    :param unsorted_list: you want to sort given by the user
    """
    for i in range(len(unsorted_list)):
        # Initial value to the min index equal to i
        max_index = i
        for j in range(i + 1, len(unsorted_list)):
            # If number more than that we have its index take the other index
            if unsorted_list[max_index][1] < unsorted_list[j][1]:
                # Taking the index of the max value
                max_index = j
        # Putting the max number in the first of list
        unsorted_list[i], unsorted_list[max_index] = unsorted_list[max_index], unsorted_list[i]
    return unsorted_list

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

# 2) bubble sort
def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if alist[j][1] < alist[j + 1][1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

# 3) merge sort
def merge_sort(unsorted_list):
    helper_merge_sort(unsorted_list)
    return unsorted_list


def helper_merge_sort(unsorted_list):
    """
    Sorting a list using merge sort
    :param unsorted_list: unsorted list given by user
    """
    list_len = len(unsorted_list)
    # If number of items in list greater than 1
    if list_len > 1:
        # Mid of the list and getting the left of this list and right half
        mid = list_len // 2
        left_list = unsorted_list[mid:]
        helper_merge_sort(left_list)
        right_list = unsorted_list[:mid]
        helper_merge_sort(right_list)
        # Initialize the value of i, j and k to zero
        i = j = k = 0
        # While i and j are in ranges left and right list respectively
        while i < len(left_list) and j < len(right_list):
            # if the item in the left list more than that in the right one put it in the original list
            if left_list[i][1] > right_list[j][1]:
                unsorted_list[k] = left_list[i]
                i += 1
            else:
                # If the item in the right is the greater put it in the original list
                unsorted_list[k] = right_list[j]
                j += 1
            k += 1
        # Check if the left list ended and if not put its items in the original list
        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i += 1
            k += 1
        # Check if the right list ended and if not put its items in the original list
        while j < len(right_list):
            unsorted_list[k] = right_list[j]
            j += 1
            k += 1

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

# 4) quick sort

def quick_sort(unsorted_list):
    """
    Sorting a list using quick sort
    :param unsorted_list: unsorted list given by user
    :return: list of most repeated words
    """
    quick_sort_helper(unsorted_list, 0, len(unsorted_list) - 1)
    return unsorted_list


def quick_sort_helper(unsorted_list, first, last):
    """
    Helper function that takes the first and last value of the list wanted to sort
    :param unsorted_list: unsorted list given by user
    :param first: first value of list you want to sort
    :param last: last value of list you want to sort
    """
    # If the first pointer less than that of last
    if first < last:
        # Know the mid pointer of the list
        mid = partition(unsorted_list, first, last)
        # Make quick sort on each of the left list and the right
        quick_sort_helper(unsorted_list, first, mid - 1)
        quick_sort_helper(unsorted_list, mid + 1, last)


def partition(unsorted_list, first, last):
    """
    Know the mid value of the list that is in the mid which its left is greater than it and its right is less
    :param unsorted_list: unsorted list given by user
    :param first: first value
    :param last: last value
    :return: mid value of the list
    """
    # Take the first value as pivot
    pivot = unsorted_list[first][1]
    # Left pointer that moves from the left of the list and other one from the right
    left_pointer = first + 1
    right_pointer = last
    # Variable that if true the loop will out
    done = False

    # Moving the less right and the less values left
    while not done:
        while left_pointer <= right_pointer and unsorted_list[left_pointer][1] >= pivot:
            left_pointer += 1
        while left_pointer <= right_pointer and unsorted_list[right_pointer][1] <= pivot:
            right_pointer -= 1
        # If the left pointer exceed the right one quit
        if left_pointer > right_pointer:
            done = True
        else:
            # If not swap between the left and right values
            unsorted_list[left_pointer], unsorted_list[right_pointer] = unsorted_list[right_pointer], unsorted_list[
                left_pointer]
    # Swap between the first value and that at the right
    unsorted_list[first], unsorted_list[right_pointer] = unsorted_list[right_pointer], unsorted_list[first]

    return right_pointer

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################


# 5) insertion sort
def insertion(unsorted_list):
    for i in range(1, len(unsorted_list)):
        current_value = unsorted_list[i]
        while i > 0 and unsorted_list[i - 1][1] < current_value[1]:
            unsorted_list[i] = unsorted_list[i - 1]
            i -= 1
        unsorted_list[i] = current_value
    return unsorted_list


###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

def search(ls,target):
   for i in range(len(ls)):
      if ls[i] == target:
         return True
   return False

