import sys 
sys.setrecursionlimit(9999)
 
 
 
def solver(arr): 
    n = len(arr) 
    dp = []
 
 
 
def solver1(arr): 
    # recur function return new l anr r pointers, value 
 
    memo = {} 
    # return left_taken, score
    def recur(left, right):
        if left == right:
            return (True, arr[right])
        elif left > right: 
            return (True , 0)
        
        elif (left, right) in memo: 
            return memo[(left, right)] 
        # opp score 
        opp_left = recur(left + 1, right) 
        opp_right = recur(left, right - 1)
 
        if opp_left[-1] < opp_right[-1]: 
            # choose left now way to go 
            if right - left == 1: 
                res = (False, arr[left])
            elif opp_left[0]: 
                res = (False , arr[left] + recur(left + 1, right - 1)[-1])
            else: 
                res = (False, arr[left] + recur(left + 2, right)[-1] )
        else: 
            if right - left == 1: 
                res =  (True, arr[right])
            elif opp_right[0]: 
                res = (True, arr[right] + recur(left, right - 2)[-1])
            else: 
                res = (True, arr[right] + recur(left + 1, right - 1)[-1])
        memo[(left, right)] = res 
        return res
    res = recur(0, len(arr) - 1)
    return res[-1]
 
n = input() 
arr = [int(_) for _ in input().split(" ")]
print(solver1(arr)