import numpy as np

def matrix_block(a,i,j):
    mid=int(len(a)/2)
    if i==1 and j==1:
        return a[:mid,:mid]
    elif i==1 and j==2:
        return a[:mid,mid:]
    elif i==2 and j==1:
        return a[mid:,:mid]
    else:
        return a[mid:,mid:]

def merge_matrix(a11,a12,a21,a22):
    n=len(a11)+len(a21)
    a=[[0]*n for example in range(n)]
    a=np.array(a)
    a[:len(a11),:len(a11)]=a11
    a[:len(a11),len(a11):]=a12
    a[len(a11):,:len(a11)]=a21
    a[len(a22):,len(a22):]=a22
    return a
def square_matrix_multiply_recursive(a,b):
    n=len(a)
    c=[[0]*n for example in range(n)]
    c=np.array(c)
    if n==1:
        c[0,0]=a[0,0]*b[0,0]
    else:
        a11=matrix_block(a,1,1)
        a12=matrix_block(a,1,2)
        a21=matrix_block(a,2,1)
        a22=matrix_block(a,2,2)
        b11=matrix_block(b,1,1)
        b12=matrix_block(b,1,2)
        b21=matrix_block(b,2,1)
        b22=matrix_block(b,2,2)
        c11=square_matrix_multiply_recursive(a11,b11)+square_matrix_multiply_recursive(a12,b21)
        c12=square_matrix_multiply_recursive(a11,b12)+square_matrix_multiply_recursive(a12,b22)
        c21=square_matrix_multiply_recursive(a21,b11)+square_matrix_multiply_recursive(a22,b21)
        c22=square_matrix_multiply_recursive(a21,b12)+square_matrix_multiply_recursive(a22,b22)
        c=merge_matrix(c11,c12,c21,c22)
    return c
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
b=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
c=square_matrix_multiply_recursive(a,b)
print(c)