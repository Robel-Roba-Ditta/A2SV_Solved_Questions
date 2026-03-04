from collections import defaultdict
n , k=map(int, input().split())
arr = list(map(int, input().split()))
table = defaultdict(int)

ans = 0
left = 0
tot_sum = 0

for right in range(n):
    if table[arr[right]] == 0:
        ans += 1
    table[arr[right]] += 1
    
    while ans > k:
        table[arr[left]] -= 1
        if table[arr[left]] == 0:
            ans -= 1
        left += 1

    tot_sum += (right - left) + 1

print(tot_sum)
