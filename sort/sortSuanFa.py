#coding=utf-8
import random
import datetime,time

class sortSuanFa(object):
	origin_nums=[]
	output_nums=[]
	def __init__(self):
		self.origin_nums=random.sample(range(0,1000000),10000)
		#print('the origin nums',self.origin_nums)
	#冒泡排序，从头开始比较相邻的值，将较大的值往后顶，然后往后再比较相邻的值
	def popSort(self):
		length = len(self.origin_nums)
		for i in range(0,length):
			for j in range(0,length-i-1):
				if self.origin_nums[j]>self.origin_nums[j+1]:
					tmp = self.origin_nums[j]
					self.origin_nums[j]=self.origin_nums[j+1]
					self.origin_nums[j+1] = tmp
		
	#插入排序
	def insertSort(self):
		length = len(self.origin_nums)
		for i in range(1,length):
			j =i
			tmp = self.origin_nums[i]
			while j>0 and tmp<self.origin_nums[j-1]:
					#将i位置的值插入j的位置，并且将j位置的值往后移
					self.origin_nums[j] =self.origin_nums[j-1]
					j-=1
			self.origin_nums[j] = tmp
		
	#选择排序
	def selectSort(self):
		length = len(self.origin_nums)
		for i in range(0,length):
			for j in range(i+1,length):
				if self.origin_nums[i]>self.origin_nums[j]:
					tmp =self.origin_nums[i]
					self.origin_nums[i] = self.origin_nums[j]
					self.origin_nums[j] = tmp
			
	#快速排序
	def quickSort(self,arr):
		if len(arr)<2:
			return arr
		else:
			pivot = arr[len(arr)//2]
			less =[i for i in arr[1:] if i<=pivot]
			greater = [i for i in arr[1:] if i>pivot]
			return self.quickSort(less)+[pivot]+self.quickSort(greater)
	#希尔排序
	def shellSort(self):
		length = len(self.origin_nums)
		gap  =length//2  #步长
		#对于每个步长，进行插入排序
		while gap>0:
			for i in range(0,gap): #分成的段数
				j = i+gap
				while j<length:
					if self.origin_nums[j]<self.origin_nums[j-gap]:
						temp = self.origin_nums[j]
						k = j-gap
						while k>=0 and self.origin_nums[k]>temp:
							self.origin_nums[k+gap]=self.origin_nums[k]
							k-=gap
						self.origin_nums[k+gap] =temp
					j+=gap
			gap =gap//2
										
				
if __name__=='__main__':
	suanfa = sortSuanFa()
	start =time.time()
	#suanfa.insertSort()
	end =time.time()
	print('插入排序花的时间:%ss'%(end-start))
	start =time.time()
	suanfa.quickSort(suanfa.origin_nums)
	end = time.time()
	print('快速排序所花的时间%s'%(end-start))
	start = time.time()
	suanfa.shellSort()
	end = time.time()
	print('希尔排序所花的时间%s'%(end-start))
	start = time.time()
	suanfa.selectSort()
	end = time.time()
	print('选择排序所花的时间%s'%(end-start))
	start = time.time()
	suanfa.popSort()
	end = time.time()
	print('冒泡排序所花的时间%s'%(end-start))
	
	
		