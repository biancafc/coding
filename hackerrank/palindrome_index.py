# Palindrome Index - https://www.hackerrank.com/challenges/palindrome-index/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def check_palindrome(s):
    last_index = len(s)-1
    half_index = int(len(s)/2)
    for index, item in enumerate(s[:half_index]):
        if item != s[last_index]:
            return False
        last_index -= 1
    return True

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    last_index = len(s)-1
    half_index = int(len(s)/2)
    for index, item in enumerate(s[:half_index]):
        if item != s[last_index]:
            if check_palindrome(s[index:last_index]):
                return last_index
            if check_palindrome(s[index+1:last_index+1]):
                return index
            return -1
        last_index -= 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
