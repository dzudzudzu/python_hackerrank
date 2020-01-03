#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxnumb = 0
    minnumb = arr[0]   
    i = 0 
    j = 0
    k = 0       
    while i < len(arr):
        if maxnumb <= arr[i]:
            maxnumb = arr[i]    
        i+=1
    while j < len(arr):
        if minnumb>=arr[j]:
            minnumb = arr[j]
        j+=1
    maxsum = 0
    minsum = 0
    
    while k < 5:
        maxsum += arr[k]
        minsum += arr[k]
        k += 1
    maxsum = maxsum - minnumb
    minsum = minsum - maxnumb    
    print(minsum, maxsum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
