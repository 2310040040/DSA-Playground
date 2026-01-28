"""
Problem: Palindrome Check

Description:
Check whether a given string is a palindrome.
A palindrome reads the same forwards and backwards.

Input:
a single string

Example:
madam

Output:
Yes or No
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Invalid input. Example: madam")
        sys.exit()

    s=sys.argv[1].strip()

    if s==s[::-1]:
        print("Yes")
    else:
        print("No")
