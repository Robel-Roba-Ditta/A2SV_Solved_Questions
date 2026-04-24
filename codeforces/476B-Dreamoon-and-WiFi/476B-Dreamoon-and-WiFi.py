s1 = input()
s2 = input()
target = 0
for c in s1:
    target += 1 if c == '+' else -1
q = 0
fixed = 0
for c in s2:
    if c == '?':
        q += 1
    else:
        fixed += 1 if c == '+' else -1
total = 1 << q
good = 0
for mask in range(total):
    pos = fixed
    for i in range(q):
        if mask & (1 << i):
            pos += 1
        else:
            pos -= 1
    if pos == target:
        good += 1
print(f"{good / total:.12f}")