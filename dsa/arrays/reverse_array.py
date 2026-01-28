"""
Problem: Reverse Array

Description:
Given an array of integers, reverse the array
and print the reversed array.

Input:
numbers separated by space

Example:
2 9 10 4 8

Output:
Reversed array
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Invalid input format. Example: 2 9 10 4 8")
        sys.exit()

    try:
        nums=list(map(int,sys.argv[1].split()))
    except:
        print("Invalid input format. Example: 2 9 10 4 8")
        sys.exit()

    nums.reverse()
    print(nums)
