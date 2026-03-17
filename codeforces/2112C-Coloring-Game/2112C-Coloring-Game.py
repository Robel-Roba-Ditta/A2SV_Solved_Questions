from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
num = lambda: int(sys.stdin.readline().strip())
nums = lambda: list(map(int, sys.stdin.readline().strip().split()))
word = lambda: sys.stdin.readline().strip().split()
words = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: num() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
prefix_sum = lambda arr: list(itertools.accumulate(arr))
def solve():
 n=num()
 a=nums()
 def cp(p,t):
  l=0
  r=p-1
  c=0
  while l<r:
   if a[l]+a[r]>t:
    c+=r-l
    r-=1
   else:
    l+=1
  return c
 ta=cp(n-1,a[n-1])
 ab=0
 for k in range(2,n-1):
  t=max(a[k],a[n-1]-a[k])
  ab+=cp(k,t)
 print(ta+ab)
for _ in range(test_cases()):
 solve()