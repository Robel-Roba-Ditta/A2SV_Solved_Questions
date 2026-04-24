import sys
from bisect import bisect_left
input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1
for _ in range(t):
    n = int(data[index])
    m = int(data[index+1])
    index += 2
    a = [int(data[index + i]) for i in range(n)]
    index += n
    b = [int(data[index + i]) for i in range(m)]
    index += m
    b.sort()
    prev = -(10**18 + 5)
    ok = True
    for x in a:
        cand1 = x
        cand2 = 10**18 + 5
        if m > 0:
            need = prev + x
            pos = bisect_left(b, need)
            if pos < m:
                cand2 = b[pos] - x   
        chosen = 10**18 + 5
        if cand1 >= prev:
            chosen = cand1
        if cand2 < 10**18 + 5 and cand2 >= prev:
            chosen = min(chosen, cand2)
        
        if chosen == 10**18 + 5:
            ok = False
            break
        prev = chosen   
    
    print("YES" if ok else "NO")