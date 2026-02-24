n = int(input())
a = list(map(int, input().split()))

a.sort()
days = 0

for p in a:
    if p >= days + 1:
        days += 1

print(days)
