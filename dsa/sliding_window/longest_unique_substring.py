"""
Problem: Longest Substring Without Repeating Characters

Description:
Given a string, find the length of the longest substring
without repeating characters.

Input:
a single string

Example:
abcabcbb

Output:
Length of longest substring
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Invalid input. Example: abcabcbb")
        sys.exit()

    s=sys.argv[1]
    seen={}
    l=0
    ans=0

    for r in range(len(s)):
        if s[r] in seen and seen[s[r]]>=l:
            l=seen[s[r]]+1
        seen[s[r]]=r
        ans=max(ans,r-l+1)

    print(ans)
