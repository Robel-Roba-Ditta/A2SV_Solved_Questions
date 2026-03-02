n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
cur = 0
ans = 0

for right in range(n):
    cur += arr[right]
    
    while cur > s:
        cur -= arr[left]
        left += 1
    
    ans += (right - left + 1)

print(ans)
