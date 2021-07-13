# 密碼重設程式
password = 'a123456' 
trys = 3 # trys = 剩餘機會
while trys > 0:
	trys = trys - 1
	pwd = input('請輸入您的密碼： ') 
	if pwd == password:
		print('登入成功！')
		break
	else:
		print('密碼輸入錯誤！')
		if trys > 0:
			print('還有', trys, '次機會')
		else:
			print('沒有機會了，要鎖帳號了拉！')
