

def OptimalBinaryTree(keys, weights):

    N = len(keys)

    A = [[0 for _ in range(N)] for _ in range(N)]

    # loop from the subproblem lengths, from small subproblem to big 
    for s in range(N):
        # loop from the start point
        for i in range(N):
            
            if i+s < N:
                tmp = []
                # loop from the position of root node
                for r in range(i, i+s+1):

                    if r-1 < 0:
                        tmp.append(sum(weights[i:i+s+1]) + A[r+1][i+s])
                    elif r + 1 > N-1:
                        tmp.append(sum(weights[i:i+s+1]) + A[i][r-1])
                    else:
                        tmp.append(sum(weights[i:i+s+1]) + A[i][r-1] + A[r+1][i+s])
                    
                minVal = min(tmp)

                A[i][i+s] = minVal

    # from 0 to the end node, the optimal solution of original problem
    return A[0][-1]




if __name__ == "__main__":
    
    #### ex1
    # keys = list(range(1,8))
    # weights = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]

    #### ex2
    keys = [10, 12, 20]
    weights = [34, 8, 50]

    A = OptimalBinaryTree(keys,weights)

    print(A)












