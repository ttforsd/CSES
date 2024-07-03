def solver(arr): 
    reach = 0 
    arr.sort() 
    for n in arr: 
        if n > reach + 1: 
            return reach + 1 
        else: 
            reach += n

    return reach + 1 


n = input() 
arr = [int(_) for _ in input().split(" ")]
print(solver(arr))