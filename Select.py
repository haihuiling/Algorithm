# coding=utf-8
import random
import math
# 从一组数中找出第k小的数，这一组数互异
# p表示开始位置，r表示结束位置，i表示第i小


def randomSelect(arr, p, r, i):
    if p == r:
        return arr[p]
    q, arr = randomPartion(arr, p, r)
    # print(q,arr)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomSelect(arr, p, q - 1, i)
    else:
        return randomSelect(arr, q + 1, r, i - k)


def select(arr, p, r, i):
    if p == r:
        return arr[p]
    length = len(arr[p:r])
    groups = math.ceil(length / 5)
    index = 0
    medians = []  # 获取所有中位数
    while index < groups:
        # 采用插入排序对[5*index,5*(index+1)-1]的数进行排序
        arrtemp = insertSort(
            arr[(p + 5 * index):(5 * (index + 1) + p if index + 1 != groups else length + p)])
        medians.append(arrtemp[len(arrtemp) // 2])
        index += 1
    # 找出medians的中位数
    medians = insertSort(medians)
    # 获取中位数的中位数
    median = medians[math.floor((len(medians) - 1) / 2)]
    tempArrL = []
    tempArrR = []
    for o in arr:
        if o < median:
            tempArrL.append(o)
        elif o > median:
            tempArrR.append(o)
    medianPos = len(tempArrL)  # 中位数所在的位置，即主元
    arr = tempArrL + [median] + tempArrR
    k = medianPos - p + 1
    if i == k:
        return arr[medianPos]
    elif i < k:
        return select(arr, p, medianPos - 1, i)
    else:
        return select(arr, medianPos + 1, r, i - k)

# 在[p,r]区间随机地产生q,并使左边的所有数小于等于arr[q],右边的所有数大于arr[p]


def randomPartion(arr, p, r):
    q = random.randint(p, r)
    qq = arr[q]
    tempArrL = []
    tempArrR = []
    index = -1
    for o in arr:
        if o < qq:
            tempArrL.append(o)
            index += 1
        elif o > qq:
            tempArrR.append(o)
    return index + 1, tempArrL + [qq] + tempArrR

# 插入排序


def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i
        tmp = arr[i]
        while j > 0 and tmp < arr[j - 1]:
            # 将i位置的值插入j的位置，并且将j位置的值往后移
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp
    return arr

if __name__ == "__main__":
    arr = [10, 9, 8, 7, 123, 6, 5, 4, 3, 2, 11, 1]
    print(select(arr, 0, 10, 12))
