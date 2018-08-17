# for x in enumerate([1,2,3,4,5]):
# 	print(x[0])


# generator 生成器
# List = [x * x for x in range(1,10)]
# print(List)
# Gen = (x * x for x in range(1,10))
# for n in Gen:
# 	print(n)

# fibonacci
# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		print(b)
# 		a, b = b, a + b
# 		n += 1
# 	print("ojbk") 

# fib(8)

def triangles(max):
	n = 0
	N = [1]
	while n < max :
		yield N
		N = [1] + [N[i] + N[i+1] for i in range(len(N) - 1)] + [1]
		n +=1
	print("ojbk")

for x in triangles(10) :
	print(x)