def square_matrix_multiply(a,b):
    n=len(a)
    c=[[0]*n for example in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c
if __name__=='__main__':
    a=[[3,3],[2,2]]
    b=[[1,2],[3,4]]
    c=square_matrix_multiply(a,b)
    print(c)