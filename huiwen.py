# coding=utf-8
# 找出最大回文子串的长度


def findMaxHuiwen(originStr):
    # 将字符串abc处理成#a#b#这样的格式
    arr = [c for c in '#'.join([''] + [o for o in originStr] + [''])]
    p = []  # 此列表维护以arr[i]为中心的向右扩展的最大长度，包括arr[i]自身
    # 从左到右扫描arr,更新p
    length = len(arr)
    for i in range(0, length):
        p.append(0)
    id = 0  # 此变量维护目前最大回文子串的中心位置
    mx = 0  # 此数值维护目前回文子串的右边界，因此有mx = id+p[id],包括
    for index in range(0, length):
        p[index] = min(p[2 * id - index], mx - index) if (mx > index) else 1
        # 以index为中心向两边探测
        while (index - p[index] >= 0) and (index + p[index] < length) and (arr[index + p[index]] == arr[index - p[index]]):
            p[index] += 1
        # 更新mx
        if (index + p[index]) > mx:
            mx = index + p[index] - 1
            id = index
    return max(p) - 1

if __name__ == '__main__':
    print(findMaxHuiwen('abba'))
