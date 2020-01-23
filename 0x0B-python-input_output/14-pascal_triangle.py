#!/usr/bin/python3
def coeff(n, k) : 
    r = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        r = r * (n - i) 
        r = r // (i + 1) 
      
    return r


def pascal_triangle(n):
    l = []
    if n <= 0:
        return l
    for i in range(0, n):
        l2 = []
        for j in range(0, i + 1):
            l2.append(coeff(i, j))
        l.append(l2)
    return l
