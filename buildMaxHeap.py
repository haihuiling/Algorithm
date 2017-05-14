# coding=utf-8
# the root is 0...ceil(n-2/2)


def buidMaxHeap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        maxHeapify(arr, i, len(arr))
    return arr

# i is the root,so it's left child is 2n+1,and it's right child is 2n+2


def maxHeapify(arr, i, length):
    maxpos = i
    left = 0
    right = 0
    if length <= 2 * i + 1:
        pass
    else:
        left = arr[2 * i + 1]
    if left > arr[i]:
        maxpos = 2 * i + 1
    if length <= 2 * i + 2:
        pass
    else:
        right = arr[2 * i + 2]
    if right > arr[maxpos]:
        maxpos = 2 * i + 2
    if i != maxpos:
        temp = arr[i]
        arr[i] = arr[maxpos]
        arr[maxpos] = temp
        maxHeapify(arr, maxpos, length)


# heap sort.it's genneral idea is:
# first build one maxheap,then the first is the  max,exchane the first with i,
# then maxheapify the rest
def heapSort(arr):
    buidMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        maxHeapify(arr, 0, i)


if __name__ == "__main__":
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    buidMaxHeap(arr)
    print(arr)
    heapSort(arr)
    print(arr)
