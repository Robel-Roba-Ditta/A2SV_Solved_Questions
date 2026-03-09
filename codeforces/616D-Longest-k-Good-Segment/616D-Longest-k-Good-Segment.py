import sys
input = sys.stdin.readline
from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
count = defaultdict(int)
l = 0
left = 0
right = 0
for r in range(n):
    count[a[r]] += 1
    while len(count) > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            del count[a[l]]
        l += 1
    if r - l > right - left:
        left = l
        right = r
print(left + 1, right + 1)