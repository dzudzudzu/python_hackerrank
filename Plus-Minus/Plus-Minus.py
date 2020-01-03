#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x = len(arr)
    p = 0
    n = 0
    z = 0
    for i in range(0, len(arr)):
        if (arr[i]<0):
            n+=1
        elif (arr[i]>0):
            p+=1
        else:
            z+=1

    print( "{:.6f}".format(p/x),"\n",round(n/x,6),"\n", round(z/x,6))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)