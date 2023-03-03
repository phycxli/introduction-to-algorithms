#include<stdio.h>
int main()
{
    int a[]={5,4,3,2,1};
    //void merge_sort(int a[],int p,int r);
    //merge_sort(a,0,4);
    int i;
    int n=sizeof(a)/sizeof(a[0]);
    for(i=0;i<n;i++)
    {
        printf("%d,",a[i]);
    }
    return 0;
}

void merge(int a[],int p,int q,int r)
{
    int n1=q-p+1;
    int n2=r-q;
    int left[n1+1];
    int right[n2+1];
    int i,j,k;
    for(i=0;i<n1;i++)
    {
        left[i]=a[p+i];
    }
    for(i=0;i<n2;i++)
    {
        right[i]=a[q+i+1];
    }
    left[n1]=100;
    right[n2]=100;
    i=0;j=0;
    for(k=p;k<=r;k++)
    {
        if (left[i]<right[i])
        {
            a[k]=left[i];
            i=i+1;
        }
        else
        {
            a[k]=right[j];
            j=j+1;
        }
    }
}
void merge_sort(int a[],int p,int r)
{
    void merge(int a[],int p,int q,int r);
    if (p<r)
    {
        int q=(p+r)/2;
        merge_sort(a,p,q);
        merge_sort(a,q+1,r);
        merge(a,p,q,r);
    }
}