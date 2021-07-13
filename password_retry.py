# 密碼重設程式
password = 'a123456' 
trys = 3 # trys = 嘗試次數
while trys > 0:
	pwd = input('請輸入您的密碼： ') 
	if pwd == password:
		print('登入成功！')
		break
	else:
		trys = trys - 1
		print('密碼輸入錯誤！還有', trys, '次機會')