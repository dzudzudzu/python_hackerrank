#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    biggest = 0
    biggest = ar[0]
    i = 0
    while i<len(ar):
            if biggest <= ar[i]:
                biggest = ar[i]
            i+=1
      
    i = 0
    result = 0
    while i<len(ar):
        if ar[i]==biggest:
            result+=1
        i+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()