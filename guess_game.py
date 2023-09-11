import random

ans = random.randint(1, 100)

count = 0

while True:
	count += 1
	gus_num = input('0~100，請猜一個數字')
	gus_num = int(gus_num)
	if gus_num == ans:
		print('你猜對了')
		print('這是你猜的第', count, '次')
		break
	elif gus_num > ans:
		print('你的數字比答案大')
	elif gus_num < ans:
		print('你的數字比答案小')
	print('這是你猜的第', count, '次')