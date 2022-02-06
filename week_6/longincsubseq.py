"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Longest Increasing Subsequence

Link: https://open.kattis.com/contests/pe4egm/problems/longincsubseq

@author Leonard Hußke

@version 1.0, 05.12.2021

Method : Ad-Hoc

Status : Not Accepted

Explanation : Time Limit Exceeded

Runtime: > 2.00 s

"""

def calc_all_increasing_subsequences(nums, N):
    # always looking back that is why subseqs for nums[0] is value of nums[0]
    indexes[0].append(0)

    # for every nums[i] > 1
    for i in range(1, N):

        for j in range(i):
            if j >= i:
                break

            # for every j smaller than i
            if nums[i] > nums[j] and len(indexes[i]) < len(indexes[j]) + 1:
                indexes[i] = indexes[j].copy()

        # append nums[i] value to subsequence
        indexes[i].append(i)


# find longest subseq of index array
def find_longest_subseq():
    longest_subseq = indexes[0]
    for subseq in indexes:
        if len(subseq) > len(longest_subseq):
            longest_subseq = subseq
    return longest_subseq


def format_output(subseq):
    print(len(subseq))
    for x in subseq:
        print(x, end=" ")


while True:
    try:
        N = int(input())
        nums = [int(x) for x in input().split()]

        # 2d array to store indexes of every value of longest increasing subsequence
        indexes = [[] for _ in range(N)]

        calc_all_increasing_subsequences(nums, N)
        longest_subseq = find_longest_subseq()
        format_output(longest_subseq)

    except EOFError:
        break