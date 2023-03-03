import numpy as np
import datetime
#首先定义一个计算交叉子数组的函数
def cross_subarray(a,left,mid,right):
    sum_left=float('-inf')
    sum=0
    left_index=right_index=None
    i=mid
    while i>=left:
        sum+=a[i]
        if sum>sum_left:
            sum_left=sum
            left_index=i
        i-=1
    sum_right=float('-inf')
    sum=0
    j=mid+1
    while j<=right:
        sum+=a[j]
        if sum>sum_right:
            sum_right=sum
            right_index=j
        j+=1
    return left_index,right_index,(sum_left+sum_right)
#求解最大子数组
def find_max_subarray(a,low,high):
    if high==low:
        return (low,high,a[low])
    else:
        mid=int((low+high)/2)
        left_low,left_high,left_sum=find_max_subarray(a,low,mid)
        right_low,right_high,right_sum=find_max_subarray(a,mid+1,high)
        cross_low,cross_high,cross_sum=cross_subarray(a,low,mid,high)
        if left_sum>right_sum and left_sum>cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>left_sum and right_sum>cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)


if __name__=='__main__':
    start_time=datetime.datetime.now().microsecond
    np.random.seed(40)
    a=np.random.randint(0,10,100)
    l,r,s=find_max_subarray(a,0,len(a)-1)
    print(l,r,s)
    end_time=datetime.datetime.now().microsecond
    print('Running time: %s microseconds'%(end_time-start_time))