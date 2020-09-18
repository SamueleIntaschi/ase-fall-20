import math

def sum(m, n):
    for x in range(n):
        m = m + 1
    return m

def divide(m, n):
    cnt = 0
    while m >= 0:
        m = m - n
        cnt = cnt + 1
    return cnt