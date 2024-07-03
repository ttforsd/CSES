def solver(coins): 
    res = set() 
    res.add(0) 
    for coin in coins: 
        tmp = res.copy() 
        for val in tmp: 
            res.add(val + coin)
    res = list(res) 
    res.sort() 
    res = res[1:]
    return len(res), res 


input() 
coins = input().split(" ")
coins = [int(coin) for coin in coins] 
l, arr = solver(coins) 
arr = [str(_) for _ in arr]
print(l)
print(" ".join(arr))



