from os import *
from sys import *
from collections import *
from math import *


def merge(arr, l, mid, r):
    b = []
    i = l
    j = mid + 1
    count = 0
    while (i <= mid) and (j <= r):
        if arr[i] <= arr[j]:
            b.append(arr[i])
            i = i + 1
        else:
            b.append(arr[j])
            j = j + 1
            count = count + (mid - i+1)

    while i <= mid:
        b.append(arr[i])
        i = i + 1
    while j <= r:
        b.append(arr[j])
        j = j + 1
    sid = 0
    for k in range(l, r+1):
        arr[k] = b[sid]
        sid += 1
    return count


def mergersort(arr, l, r):
    count = 0
    if l < r:
        mid = (l + r) // 2
        count = count + mergersort(arr, l, mid)
        count = count + mergersort(arr, mid + 1, r)
        count = count + merge(arr, l, mid, r)
    return count




def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(mergersort(arr,0, n-1))
