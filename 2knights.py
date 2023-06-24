def solver(n): 
     sq_n = n * n 
     ways = sq_n * (sq_n - 1) // 2 
     # ways to attack = distinct 2x3s x2 
     attack = (n - 2) * (n - 1) * 4 
     return ways - attack



n = int(input())
for i in range(n): 
    print(solver(i + 1))