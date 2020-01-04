#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    i = 0
    j = 0
    k = 0
    l = 0
    for i in range(len(apples)):
        if (apples[i]+a)>=s and(apples[i]+a)<=t:
            k+=1
    print(k)
    for j in range(len(oranges)):
        if (oranges[j]+b)>=s and (oranges[j]+b)<=t:
            l+=1
    print(l)

            

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
