"""
Problem: Maximum Sum Subarray of Size K

Description:
Given an array of integers and a number K,
find the maximum sum of any contiguous subarray of size K.

Input:
numbers separated by space;K

Example:
2 1 5 1 3 2;3

Output:
Maximum sum
"""

import sys

if __name__=="__main__":
    if len(sys.argv)<2 or ";" not in sys.argv[1]:
        print("Invalid input. Example: 2 1 5 1 3 2;3")
        sys.exit()

    try:
        arr,k=sys.argv[1].split(";")
        nums=list(map(int,arr.split()))
        k=int(k)
    except:
        print("Invalid input. Example: 2 1 5 1 3 2;3")
        sys.exit()

    if k>len(nums) or k<=0:
        print("Invalid window size")
        sys.exit()

    s=sum(nums[:k])
    mx=s

    for i in range(k,len(nums)):
        s+=nums[i]-nums[i-k]
        if s>mx:
            mx=s

    print(mx)
