n = int(input())
for _ in range(0,n):
	x,y = map(int, input().split())
	area = (x * y) / 2
	print("%d cm2"% area)