###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################
from Algorithms import *

def readFile(fileName,splitSign=" ",x=0):
    """
       reading file name and converting it into list if x = 0
       or to string if x = 1
    :param fileName: name of file
           splitSign= sign to split at.
           x: to choose list or string

    :return: list of words or string depending on the value of x
    """
    file = open(fileName, 'r')
    text = file.read().lower()
    file.close()
    if x==0:
        return text.split(splitSign)
    else:
        return " ".join(text.split(splitSign) )

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

def symbolfree(content_with_punctuations):
    """
    removing puncs from the string
    :param content_with_punctuations: string neded to be cleared from punc
    :return: string clear of puncs
    """
    empty_txt=""
    puncs="!@#$%^*&()_+/-+><,—’?':;{.}\\"
    for i in content_with_punctuations:
        if i not in puncs:
            empty_txt += i
    return empty_txt

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

# eliminating unwanted words:
def remove_common(my_list): #Using linear search as common words are sorted
    """
    removing common words from the list of words 
    :param my_list: list neded to be cleared from common words
    :return: list clear of common words
    """

    x= readFile("common-english-words.txt",",") 
    alist=[]
    for i in range(len(my_list)):
        if search(x,my_list[i]) == False : 
            alist.append(my_list[i])
    return alist

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

def find_repeats(list_of_words):
    """
    find repeats in a list and change it into dictionary and put the number of repeating of each element
    list must contain only words

    :param list_of_words: list of words from user
    :return: dictionary of each word and number of repeats
    """
    # Change the list to file that have key '0' for each word
    dict_of_words = dict.fromkeys(list_of_words, 0)
    result=[]
    # Loop around whole words
    for i in range(len(list_of_words)):
        # Increase the number of repeating of word by one
        dict_of_words[list_of_words[i]] += 1
    # result = [[key, dict_of_words[key]] for key in dict_of_words]
    for key in dict_of_words:
        result.append([key,dict_of_words[key]])

    return result

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################

def most_repeated(sorted_list, number_of_words=4):
    """
    most repeated words
    :param sorted_list: given from user
    :param number_of_words: want to be out in the list
    :return: list of number of most repeated words
    """
    words = [None] * number_of_words
    for i in range(int(number_of_words)):
        words[i] = sorted_list[i][0]
    return words

###############################################################################################
##                                        TEAM 3                                             ##  
###############################################################################################


def searchMostWordsInFields(alist):
    """
    :param alist: list which have most repeated words in the article
    :return:the page topic
    """
    #reading the topic most commpn words
    politics = readFile('topic_words\politics.txt')
    sport = readFile('topic_words\sport.txt')
    cooking = readFile('topic_words\cooking.txt')
    astronomy = readFile('topic_words\\astronomy.txt')
   
    searchResult = {
        'politics': 0,
        'sport': 0,
        'cooking': 0,
        'astronomy': 0,
    }

    #searching for the most repeated words in the topic files
    for i in range(len(alist)):          
        if search(politics, alist[i]): searchResult['politics'] += 1
        if search(sport, alist[i]): searchResult['sport'] += 1
        if search(cooking, alist[i]): searchResult['cooking'] += 1
        if search(astronomy, alist[i]): searchResult['astronomy'] += 1
    field = ''
    maxNum = 0
   #return the topic which have the most repeated words
    for key in searchResult:                
        if searchResult[key] > maxNum:
            maxNum = searchResult[key]
            field = key

    return field