#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    # a = arr[n-1]

    # for i in range(len(arr) - 1, 0, -1):
    #     if a < arr[i-1]:
    #         arr[i] = arr[i-1]
    #         print(*arr)
    #     elif a > arr[i - 1]:
    #         arr[i] = a
    #         print(*arr)
    i = n - 1
    a = arr[i]
    while i > 0 and a < arr[i-1]:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = a
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
