#!/usr/bin/python36
import sys
print("Python version")
print (sys.version)

A = [3,2,7,15,77]
target = 80
x = 0
y = 0
sol_x = -1
sol_y = -1
for x in range(len(A)): 
    for y in range(len(A)):
        print("x:%d" % (x))
        print("y:%d" % (y))
        sum=A[x] + A[y]
        print (sum)
        if (x!=y):
            if (A[x] + A[y]==target):
                sol_x=x
                sol_y=y
            else:
                y=y+1
    x=x+1
print(sol_x)
print(sol_y)
        
    
    