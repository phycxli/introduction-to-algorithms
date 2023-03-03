import datetime
import numpy as np
def find_max_subarray(a):
    sum_result=float('-inf')
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            sum=0
            k=i
            while k<=j:
                sum+=a[k]
                k+=1
            if sum>sum_result:
                sum_result=sum
                left_ind=i
                right_ind=j
    return left_ind,right_ind,sum_result

if __name__=='__main__':
    start_time=datetime.datetime.now().microsecond
    np.random.seed(40)
    a=np.random.randint(0,10,40)
    l,r,s=find_max_subarray(a)
    print(l,r,s)
    end_time=datetime.datetime.now().microsecond
    print('Running time: %s microseconds'%(end_time-start_time))