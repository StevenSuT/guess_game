import random

ans = random.randint(1, 100)

while True:
	gus_num = input('0~100，請猜一個數字')
	gus_num = int(gus_num)
	if gus_num == ans:
		print('你猜對了')
		break
	elif gus_num > ans:
		print('你的數字比答案大')
	elif gus_num < ans:
		print('你的數字比答案小')