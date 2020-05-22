# Making Anagrams - https://www.hackerrank.com/challenges/making-anagrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    frequency_char = {}
    deletions = 0
    for char in s1:
        frequency_char[char] = frequency_char.get(char, 0) + 1
    for char in s2:
        if char in frequency_char:
            if frequency_char[char] > 0:
                frequency_char[char] -= 1
            else:
                deletions += 1
        else:
            deletions += 1
    for item in frequency_char.values():
        deletions += item
    return deletions

    # deletions = 0
    # temp_j = 0
    # for i, ch1 in enumerate(s1):
    #     if temp_j >= len(s2)-1:
    #         deletions += len(s1) - i
    #         return deletions
    #     for j, ch2 in enumerate(s2[::-1]):
    #         if ch1 != ch2:
    #             deletions += 1
    #         temp_j = j + 1
    # return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
