def halving_sum(n): 
    ans = 0
    while n > 0:
        ans += n
        n = int(n/2)
    return ans
        
