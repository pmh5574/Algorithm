#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    q = 0
    w = 0
    e = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            q += 1
        elif arr[i] == 0:
            w += 1
        else:
            e += 1
            
    q = round(q/len(arr), 6)
    w = round(w/len(arr), 6)
    e = round(e/len(arr), 6)

    while len(str(q)) < 8:
        q = str(q) + '0'
    
    while len(str(w)) < 8:
        w = str(w) + '0'

    while len(str(e)) < 8:
        e = str(e) + '0'

    print(q)
    print(e)
    print(w)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
