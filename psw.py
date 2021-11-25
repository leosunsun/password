#password app

password = 'a123456'
p = 3
while p > 0: 
	psw = input ('请您输入密码：')
	if psw == password: 
		print ('登录成功！')
		break
	else : 
		p = p - 1
		print ('密码错误，您还剩余', p , '次机会')
		if p == 0 : 
			print ('您已超出次数限制，请稍后再试。')
			break