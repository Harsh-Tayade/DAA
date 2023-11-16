def knapsack(wt, val, W, n, t):
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    
    return t[n][W]

if __name__ == '__main__':
    num_items = int(input("Enter the number of items: "))
    profit = []
    weight = []
    for i in range(num_items):
        p = int(input(f"\nEnter profit for item {i + 1}: "))
        w = int(input(f"Enter weight for item {i + 1}: "))
        profit.append(p)
        weight.append(w)
    
    W = int(input("\nEnter the knapsack capacity: "))
    n = len(profit)
    t = [[0 for i in range(W + 1)] for j in range(n + 1)]
    result = knapsack(weight, profit, W, n, t)
    print(f"\nThe maximum profit possible is: {result}")
