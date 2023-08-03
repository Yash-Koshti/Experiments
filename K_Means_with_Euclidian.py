import numpy as np

# Initial Cluster Centroids

# Centroids for data-1
c1 = (0, 0)
c2 = (5, 5)
c3 = (10, 10)

# Centroids for data-2
# c1 = (2, 10)
# c2 = (5, 8)
# c3 = (1, 2)

#Data Point
# Data-1
dp = [[1,2], [2,2], [6,7], [8,6], [12,11], [10,13]]
# Data-2
# dp = [[2, 10], [2, 5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]]

clusters = ["C1", "C2", "C3"]

cnt = 0
while cnt != 4:
    print('Current Clusters :', c1, c2, c3, '\n')
    print("X\t|\tY\t|\tC1\t|\tC2\t|\tC3\t|\tCentroid")
    print("----------------------------------------------------------------------------------------")
    assigned_clusters = {}
    for i in range(len(dp)):
        dc1 = np.sqrt(np.square(dp[i][0] - c1[0]) + np.square(dp[i][1] - c1[1]))
        dc2 = np.sqrt(np.square(dp[i][0] - c2[0]) + np.square(dp[i][1] - c2[1]))
        dc3 = np.sqrt(np.square(dp[i][0] - c3[0]) + np.square(dp[i][1] - c3[1]))

        cur_dist = [dc1, dc2, dc3]
        cur_cluster = clusters[cur_dist.index(min(cur_dist))] #string
        assigned_clusters[i] = cur_cluster

        print(str(dp[i][0]) + "\t|\t" + str(dp[i][1]) + "\t|\t" + str(round(dc1, 2)) + "\t|\t" + str(round(dc2, 2)) + "\t|\t" + str(round(dc3, 2)) + "\t|\t" + cur_cluster)
    
    for c in clusters:
        x, y = [], []
        for k in assigned_clusters:
            if assigned_clusters[k] == c:
                x.append(dp[k][0])
                y.append(dp[k][1])
        if c == 'C1':
            c1 = (np.mean(x), np.mean(y))
        elif c == 'C2':
            c2 = (np.mean(x), np.mean(y))
        elif c == 'C3':
            c3 = (np.mean(x), np.mean(y))

    print("\n\n")
    cnt += 1