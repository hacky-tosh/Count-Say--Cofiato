def countAndSay(n):
    if n==1:
        return 1 
    if n==2:
        return 11 
    
    st = "11"
    for i in range(3,n+1):
        temp_st = ""
        st = st + '&'
        c = 1
        for j in range(1,len(st)):
            if st[j]!=st[j-1]:
                temp_st = temp_st + str(c)
                temp_st = temp_st + st[j-1]
                c = 1 
            else: 
                c += 1 
        st = temp_st 
    # print(st)
    return st

print(countAndSay(4))























