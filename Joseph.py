#coding=utf-8
def Joseph(n,m):
    #模拟包含n个元素的环,未出局的标志位为1，出局的标志位为0
    circle = [1 for i in range(0,n)]
    last = -1 #保存上一次循环的位置
    aim = 0 #保存出局的位置
    for i in range(0,n-1):
        j=0
        while j<m:
            last+=1
            if last<=n-1:
                if circle[last]==1:
                    j+=1
                    aim = last
            else:
                last = -1
        circle[aim]=0
    index =0
    for k in circle:
        index+=1
        if k==1:
            return index
    #return circle

if __name__=='__main__':
    print(Joseph(12,4))
