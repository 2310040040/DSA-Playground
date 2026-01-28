"""
Problem: Two Sum

Description:
Check whether there exist two numbers in the array
whose sum is equal to the given target.

Input:
numbers separated by space, then semicolon, then target

Example:
2 9 10 4 8;12

Output:
Yes and the two numbers, or No
"""

import sys   # ← THIS WAS MISSING

if __name__=="__main__":
    if len(sys.argv)<2 or ";" not in sys.argv[1]:
        print("Invalid input format. Example: 2 9 10 4 8;12")
        sys.exit()

    try:
        data=sys.argv[1]
        arr,tar=data.split(";")
        nums=list(map(int,arr.split()))
        target=int(tar)
    except:
        print("Invalid input format. Example: 2 9 10 4 8;12")
        sys.exit()

    s=set()
    for x in nums:
        if target-x in s:
            print(f"Yes: {x} and {target-x}")
            sys.exit()
        s.add(x)

    print("No")
