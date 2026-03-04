n , m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
tot = 0
left = 0
for right in range(len(arr)):
    tot += arr[right]
    while tot >= m:
        count += n - right
        tot -= arr[left]
        left += 1  
print(count)
