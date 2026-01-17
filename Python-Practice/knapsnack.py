# Dynamin Programming
# 1,0 Knapsanck

profit = [10,6,4]
weight = [4,3,2]
bag_weight = 6
size = len(profit) - 1

# Simple Recursive Appraoch
# def knapsnack(pft,wht,bag_wt,n) -> int:
#     if n == 0 or bag_wt == 0:
#         return 0
    
#     if wht[n] > bag_wt:
#         return knapsnack(pft,wht,bag_wt,n-1)
#     else:
#         return max((knapsnack(pft,wht,bag_wt,n-1) + pft[n]), knapsnack(pft,wht,bag_wt - wht[n],n-1))


def knapsack(pft,wht,bag_wt,n, memo= {}) -> int :
    if (bag_wt,n) in memo:
        return memo[(bag_wt,n)]
    if n== 0 or bag_wt == 0:
        return 0
    
    if wht[n] > bag_wt:
        return knapsack(pft, wht, bag_wt , n-1)
    else:
        return max(knapsack(pft,wht,bag_wt,n-1), ( pft[n] +knapsack(pft,wht,bag_wt - wht[n],n-1)))
    

