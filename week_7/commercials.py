"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Radio Commercials

Link: https://open.kattis.com/contests/pe4egm/problems/commercials

@author Leonard Hußke

@version 1.0, 03.12.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.07s

"""

cost = int(input().split()[1])
inputs = [int(x) for x in input().split()]
N = len(inputs)

# Subtract cost for every commercial
nums = [x - cost for x in inputs]

# Constant for minimal value
MIN = float('-inf')

def max_revenue(nums):
    # maximum ending here: largest sum continous subsequences from beginning until current element
    meh = 0

    # maximum so far: largest continous subsequence so far which not includes current element
    msf = MIN
    for i in range(N):
        meh = meh + nums[i]

        # If current value is greater than maximum ending until here then meh is current value now
        if meh < nums[i]:
            meh = nums[i]

        # If maximum ending until here is greater than maximum so far, msf is now meh
        if msf < meh:
            msf = meh
    return msf

print(max_revenue(nums))