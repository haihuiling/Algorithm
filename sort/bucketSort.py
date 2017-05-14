#coding=utf-8
#桶排序 线性时间完成 ,只要所有桶的大小的平方和与总的元素呈线性关系
import math

def bucketSort(arr):
    #将所有元素按n*arr[i]分到不同的桶中
    bucketArr=[]
    orderList=[]
    n = len(arr)
    for i in range(0,n):
        bucketArr.append([])
    for o in arr:
        bucket=bucketArr[math.floor(o*n)]
        bucket.append(o)
        # bucketArr[math.floor(o*n)]=bucket
    #对所有的bukect进行插入排序
    for bucket in bucketArr:
        if len(bucket)>0:
            insertSort(bucket)
            orderList+=bucket
    return orderList

def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        tmp = arr[i]
        j = i
        while j>0 and tmp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j] =tmp
    return arr


if __name__=="__main__":
    import random
    arr=[]
    for i in range(0,5):
        arr.append(random.random())
    print(arr)
    #arr=[.78,.17,.39,.26,.72,.94,.21,.12,.23,.68]
    print(bucketSort(arr))
