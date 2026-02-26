	t = int(input())
for _ in range(t):
    a = input()
    n = len(a)
    sset = set()
    i = 0
    while i < n :
        if i < n-1 and a[i]==a[i+1]:
            i += 2
        else:
            sset.add(a[i])
            i += 1
    print("".join(sorted(sset)))
