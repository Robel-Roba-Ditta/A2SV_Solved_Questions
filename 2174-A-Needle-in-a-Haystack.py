from collections import Counter 
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    ct = Counter(t)
    cs = Counter(s)
    fl = True
    for k, v in cs.items(): 
        if ct[k]<v:
            print('Impossible')
            fl = False
            break
        else:
            ct[k]-=v
    if fl:
        ans = []
        p = 0
        p2 = ord('a')
        while p<len(s) and p2<=ord('z'):
            if p2 < ord(s[p]):
                if ct[chr(p2)]:
                    ans.extend([chr(p2)]* ct[chr(p2)])
                p2+=1
            else:
                ans.append(s[p])
                p+=1
        for i in range(p, len(s)):
            ans.append(s[i])
        for i in range(p2,ord('z')+1):
            if ct[chr(i)]:
                ans.extend([chr(i)]*ct[chr(i)])
        print(''.join(ans))

