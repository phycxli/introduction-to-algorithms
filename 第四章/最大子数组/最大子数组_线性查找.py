import numpy as np
import datetime

def find_max_array(a):
    sub_sum=a[0]
    left,right=0,0
    for i in range(1,len(a)):
        if sub_sum>0:
            sub_sum=sub_sum+a[i]
            left=left
            right=i
        else:
            sub_sum=a[i]
            left=i
            right=i
    return left,right,sub_sum

if __name__=='__main__':
    start_time=datetime.datetime.now().microsecond
    np.random.seed(40)
    a=np.random.randint(0,10,100)
    print(find_max_array(a))
    end_time=datetime.datetime.now().microsecond
    print('Running time: %s microseconds'%(end_time-start_time))