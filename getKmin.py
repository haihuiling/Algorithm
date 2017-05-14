#coding=utf-8
def getKmin(arr,k):
	length = len(arr)
	mink=[] #存储前k个数
	for i in range(0,k):
		mink.append(arr[i])
	j = k
	while j<length:
		kmax = mink[0]
		index = 0
		#找出k个数中的最大值和其在数组中的位置
		for m in range(0,k):
			if mink[m]>kmax:
				index=m
				kmax = mink[m]
		if arr[j]<=kmax:
			mink[index]=arr[j]
		j+=1
	return mink

if __name__=="__main__":
	print(getKmin([1,2,2,3,5,6,7,10,3,4], 5))	#[1, 2, 2, 3, 3]
