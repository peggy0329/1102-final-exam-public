def p08(n=12):
    output=None
    # ↓程式區域↓
    while n%4==0:
        n//=4
    if n%8==7:   #因为7 最少由  1,2,4  三个数组成
        return 4

    for i in range(n+1):
        temp=i*i
        if temp<=n:
            if int((n-temp)**0.5)**2 +temp==n:
                return 1 +(0 if temp ==0 else 1)
        else:
            break
    return 3
    # ↑程式區域↑
    return output
