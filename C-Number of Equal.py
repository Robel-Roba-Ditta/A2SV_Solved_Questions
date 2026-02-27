from collections import Counter
n, k = map(int, input().split())
arr1 = Counter(list(map(int,input().split())))
arr2 = Counter(list(map(int,input().split())))
s = 0
for i,j in arr1.items():
    if i in arr2:
        s += (arr1[i] * arr2[i])
print(s)
