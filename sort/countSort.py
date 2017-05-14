# coding=utf-8
def countSort(arr):
    # 确定里面所有的数是属于[0,k]的数
    k = 0
    result = []
    for o in arr:
        if k < o:
            k = o
        result.append(0)
    c = []
    for i in range(0, k + 1):
        c.append(0)
    for j in range(0, len(arr)):
        c[arr[j]] = c[arr[j]] + 1
    # c[i] now contains the number of element equal to i
    for n in range(1, k + 1):
        c[n] = c[n] + c[n - 1]
    # c[n] now contains the number of element less than or equal to n
    for m in range(0, len(arr)):
        result[c[arr[m]] - 1] = arr[m]
        c[arr[m]] -= 1
    return result


# 每个数的位数都是一样的
def radixSort(arr):
    first = arr[0]
    d = len(str(first))
    # 从最低位开始比较，采用计数排序
    for i in range(d - 1, -1, -1):
        arrDict = {}
        newArr = []
        for o in arr:
            s = str(o)[i:i + 1]
            if s in arrDict.keys():
                arrDict[s] += [o]
            else:
                arrDict[s] = [o]
            newArr.append(int(s))
        tempArr = countSort(newArr)
        newArr2 = []
        existDict = {}
        for s in tempArr:
            if str(s) not in existDict.keys():
                newArr2 += arrDict[str(s)]
                existDict[str(s)] = 1
        arr = newArr2
    return arr

if __name__ == '__main__':
    arr = [329, 457, 657, 839, 436, 720, 355]
    result = radixSort(arr)
    print(result)
