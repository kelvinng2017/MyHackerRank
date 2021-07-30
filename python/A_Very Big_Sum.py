from array import array
import math
import os
import random
import re
import sys
from random import randrange

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER. #陣列值只能是int
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    if isinstance(ar, list):  # 判斷變數是否為對應形態
        total = 0
        for sum_index in range(len(ar)):
            total = total + ar[sum_index]
        return total
    else:
        return "不是陣列"


ar_count = int(input().strip())
ar = []
for ar_index in range(ar_count):
    b = random.randrange(0, 10*10)
    ar.append(b)
result = aVeryBigSum(5)
print(ar)
print(result)
