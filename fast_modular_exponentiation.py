def power(x:int, y:int, z:int):
    y = str(bin(y)[::-1])
    l = set()
    n = 1
    for i in y:
        if i == "1":
            l.add(n)
        n *= 2
    res = 1
    counter = 1
    temp_res = x % z
    m = max(l)
    while counter <= m:
        if counter in l:
            res = res * temp_res % z
        temp_res = temp_res * temp_res % z
        counter *= 2
    return res


#example: print(power(123, 11111111111, 3333))
#this function works like pow(x, y, z)
#this function returns the result of (x**y)%z
