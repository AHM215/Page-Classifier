###############################################################################################
##                                        TEAM 3                                             ##
###############################################################################################

from Functions import *
from Algorithms import *
from time import *
#reading file and storing it as a string because x=1
a = readFile("article.txt"," ",1)
#CLearing it from sympols
page = symbolfree(a)
#converting it into list
page=page.split()
#removing common words
page= remove_common(page)
#counting the repeats of each word
unsorted_list = find_repeats(page)


### Using different type of sorting and calc the wxcution time ###

#Quick Sort
beginning = time()
sorted_list = quick_sort(unsorted_list)
t = (time()-beginning)*1000
sorted_list = most_repeated(sorted_list,6)
print(f"Results for quick_sort: {sorted_list}\nExecution time for quick_sort: {round(t,5)} ms")
print('-'*100)
#############################################################################################################################
#Insertion Sort
beginning = time()
sorted_list = insertion(unsorted_list)
t = (time()-beginning)*1000
sorted_list = most_repeated(sorted_list,6)
print(f"Results for insertion sort: {sorted_list}\nExecution time for insertion sort: {round(t,5)} ms")
print('-'*100)
#############################################################################################################################

#Merge Sort
beginning = time()
sorted_list = merge_sort(unsorted_list)
t = (time()-beginning)*1000
sorted_list = most_repeated(sorted_list,6)
print(f"Results for merge_sort: {sorted_list}\nExecution time for merge_sort: {round(t,5)} ms")
print('-'*100)
#############################################################################################################################

#Selection Sort
beginning = time()
sorted_list = selection_sort(unsorted_list)
t = (time()-beginning)*1000
sorted_list = most_repeated(sorted_list,6)
print(f"Results for selection_sort: {sorted_list}\nExecution time for selection_sort: {round(t,5)} ms")
print('-'*100)
#############################################################################################################################

#Bubble Sort
print('-'*100)
beginning = time()
sorted_list = bubble_sort(unsorted_list)
t = (time()-beginning)*1000
sorted_list = most_repeated(sorted_list,6)
print(f"Results for bubble_sort: {sorted_list}\nExecution time for bubble_sort: {round(t,5)} ms")
print('-'*100)
#############################################################################################################################
#printing the topic of the page
print(f"Results for Clissifying is : {searchMostWordsInFields(sorted_list)}")