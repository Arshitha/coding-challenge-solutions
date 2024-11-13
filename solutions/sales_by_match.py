#!/bin/python3

"""

@Author: Arshitha Basavaraj
@Modified date: 2024-11-11

Problem_URL: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
Problem statement: There is a large pile of socks that must be paired by color.
 Given an array of integers representing the color of each sock, 
 determine how many pairs of socks with matching colors there are.
Passed submission?: Yes.
"""
import math
from collections import defaultdict


def sockMerchant(n, ar):

    sock_dict = defaultdict(lambda: 0)
    for s in ar:
        sock_dict[s] += 1

    pairs = 0
    for k, v in sock_dict.items():
        if math.floor(v / 2) != 0:
            print(k, v)
            pairs += math.floor(v / 2)

    return pairs


if __name__ == "__main__":
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]

    result = sockMerchant(n, ar)
    print(result)
