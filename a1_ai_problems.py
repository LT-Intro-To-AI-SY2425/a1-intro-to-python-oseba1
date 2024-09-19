

#1. K-Closest Points to Origin
#Problem Statement:
#
#Given a list of points on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points is the Euclidean distance.
#
#Requirements:
#
#Implement a solution that efficiently computes the k closest points using a heap.



import math
def KpointsToOrigin(lst: list, count: int) -> list:

    distanceList = []
    sortedList = []
    for i in range(len(lst)):
        x = lst[i][0]
        y = lst[i][1]

        distance = math.sqrt((x ** 2) + (y ** 2))
        distanceList.append(distance)

    sortedList = sorted(distanceList)

    result = []
    for i in range(count):
        result.append(lst[distanceList.index(sortedList[i])])

    return result

assert KpointsToOrigin([[100,2], [3,4], [5,6]], 2) == [[3,4], [5,6]]




#Problem 10: Find Missing Number
#Given an array of integers from 1 to n with one number missing, write a function to find the missing number.

def findMissingNumber(arr, n):
    return n * (n + 1) // 2 - sum(arr)

assert findMissingNumber([1,2,3,4,5,6,8,9,10], 10)

#Problem 14: Reverse Words in a String
#Write a function to reverse the words in a given string. 
#For example, given "the sky is blue", the function should return "blue is sky the".

def reverse_words(s):

    lst = s.split()
    lst.reverse()
    return(" ".join(lst))

assert reverse_words("the sky is blue") == "blue is sky the"


#Problem: Find the Longest Substring with Unique Characters
#Given a string, write a function that finds the length of the longest substring with all unique characters. 
#You need to solve it efficiently, and the solution should fit within 10 lines of Python code.

def longestUniqueSubstring(s: str) -> int:
    charIndex = {}
    start = maxLen = 0

    for end, char in enumerate(s):
        if char in charIndex:

            start = max(start, charIndex[char] + 1)

        charIndex[char] = end
        maxLen = max(maxLen, end - start + 1)


    return maxLen

assert longestUniqueSubstring("abcdefghijklmnopqraaaa") == 18

print("Tests Passed!")


# I made a tic tac toe in rock_paper_siccors.py
