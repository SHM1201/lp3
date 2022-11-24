def Knapsack(Wt, P, w, n):
    K = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                K[i][w] = 0
            elif Wt[i-1] <= j:
                K[i][j] = max(P[i-1] + K[i-1][j-Wt[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K[n][w]


P = [60, 100, 120]
Wt = [10, 20, 30]
w = 50
n = len(P)
print("Maximum total value : ", Knapsack(Wt, P, w, n))
