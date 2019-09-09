x = [[1,3],[2,4]]
y = [[5,2],[1,0]]
result =[[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]
print(result)