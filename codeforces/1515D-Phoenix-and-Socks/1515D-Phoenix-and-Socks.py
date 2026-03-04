from collections import Counter
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    left = Counter(arr[:l])
    right = Counter(arr[l:])
    count = 0
    for c in list(left.keys()):
        matched = min(left[c], right[c])
        left[c] -= matched
        right[c] -= matched
        l -= matched
        r -= matched
    if l < r:
        left, right = right, left
        l, r = r, l
    diff = l - r
    for c in left:
        if diff <= 0:
            break
        pairs = left[c] // 2
        take = min(pairs * 2, diff)
        left[c] -= take
        diff -= take
        count += take // 2
    count += diff // 2
    remaining = sum(left.values()) + sum(right.values())
    count += remaining // 2
    print(count)