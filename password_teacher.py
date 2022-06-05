#答案跟使用者輸入的要分開存2個password
#==
#str拆開用,分開
#vex後面要tab，有框框架構

password = 'a123456'
x = 3
while True:
	pwd = input ('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		x = x - 1
		print('密碼錯誤!還有', x,'次機會')
		if x == 0:
			break
#進階
#i = 3
#while i > 0:
	#i = i - 1
	#pwd = input ('請輸入密碼:')
	#if pwd == password:
		#print('登入成功!')
		#break
	#else:
		#print('密碼錯誤!')
		#if i > 0:
			#print('還有', i,'次機會')
		#else:
			#print('沒機會了啦!')