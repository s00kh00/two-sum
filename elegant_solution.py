#!/usr/bin/python36
import sys
print("Python version")
print (sys.version)

A = [2,5,7,15]
target = 22
for x in range(len(A)):
    diff = target - A[x]
    if diff > 0:
        try:
            value_index = A.index(diff)
        except:
            value_index = -1
    if value_index > 1:
        print(x)
        print(value_index)