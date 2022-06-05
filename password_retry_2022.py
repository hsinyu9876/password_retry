psw = 'a123456'
x = 3
while x > 0:
    password = input('請輸入密碼:')
    if password == psw:
        print("登入成功!")
        break
    else:
        x = x - 1
        print("密碼錯誤!還有",x ,"次機會")
else:
    print("超過密碼輸入上限")