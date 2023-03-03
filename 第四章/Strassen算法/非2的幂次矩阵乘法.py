import numpy as np
def standard(a):
    if len(a)%2==0:
        return a
    else:
        k=int(np.log2(len(a)))+1
        m=2**k
        a=np.concatenate([a,np.zeros((len(a),m-len(a)))],axis=1)
        a=np.concatenate([a,np.zeros((m-len(a),m))],axis=0)
    return a
def unstandard(a,n):
    return a[:len(a)-n+1,:len(a)-n+1]

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
def strassen(a,b):
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
        s1=b12-b22
        s2=a11+a12
        s3=a21+a22
        s4=b21-b11
        s5=a11+a22
        s6=b11+b22
        s7=a12-a22
        s8=b21+b22
        s9=a11-a21
        s10=b11+b12
        p1=strassen(a11,s1)
        p2=strassen(s2,b22)
        p3=strassen(s3,b11)
        p4=strassen(a22,s4)
        p5=strassen(s5,s6)
        p6=strassen(s7,s8)
        p7=strassen(s9,s10)
        c11=p5+p4-p2+p6
        c12=p1+p2
        c21=p3+p4
        c22=p5+p1-p3-p7
        c=merge_matrix(c11,c12,c21,c22)
    return c

def multiply(a,b):
    n=len(a)
    if len(a)==2:
        c=strassen(a,b)
        return c
    else:
        a=standard(a)
        b=standard(b)
        c=strassen(a,b)
        c=unstandard(c,len(c)-n+1)
        return c
if __name__=='__main__':
    a=np.array([[1,2,3],[1,2,3],[1,2,3]])
    b=np.array([[1,2,3],[1,2,3],[1,2,3]])
    c=multiply(a,b)
    print(c)
