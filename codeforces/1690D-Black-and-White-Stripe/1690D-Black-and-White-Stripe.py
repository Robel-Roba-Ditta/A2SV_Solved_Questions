# count whites in first window
    cur = 0
    for i in range(k):
        if s[i] == 'W':
            cur += 1
    
    ans = cur
    
    left = 0
    for right in range(k, n):
        # remove left character
        if s[left] == 'W':
            cur -= 1
        left += 1
        
        # add new right character
        if s[right] == 'W':
            cur += 1
        
        ans = min(ans, cur)
    
    print(ans)