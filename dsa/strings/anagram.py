"""
Problem: Valid Anagram

Description:
Check whether two strings are anagrams of each other.
Two strings are anagrams if they contain the same characters
with the same frequencies.

Input:
two strings separated by semicolon

Example:
listen;silent

Output:
Yes or No
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2 or ";" not in sys.argv[1]:
        print("Invalid input. Example: listen;silent")
        sys.exit()

    try:
        a,b=sys.argv[1].split(";")
    except:
        print("Invalid input. Example: listen;silent")
        sys.exit()

    if sorted(a)==sorted(b):
        print("Yes")
    else:
        print("No")
