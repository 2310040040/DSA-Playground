"""
Problem: Maximum Subarray (Kadane’s Algorithm)

Description:
Find the contiguous subarray with the maximum sum
and print that sum.

Input:
numbers separated by space

Example:
-2 1 -3 4 -1 2 1 -5 4

Output:
Maximum subarray sum
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Invalid input format. Example: -2 1 -3 4 -1 2 1 -5 4")
        sys.exit()

    try:
        nums=list(map(int,sys.argv[1].split()))
    except:
        print("Invalid input format. Example: -2 1 -3 4 -1 2 1 -5 4")
        sys.exit()

    cur=best=nums[0]
    for x in nums[1:]:
        cur=max(x,cur+x)
        best=max(best,cur)

    print(best)
