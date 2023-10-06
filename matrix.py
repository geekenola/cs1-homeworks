def matrix_transpose():
    A=[[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]] 
    B=[[0,0,0],
       [0,0,0],
       [0,0,0]]  
    for i in range(len(A)):
        for j in A[i]:
            B[i][j]=A[j][i]
    print(B)
matrix_transpose()

