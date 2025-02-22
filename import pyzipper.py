import pyzipper
zip_file = 'test.zip'
passwords = []
for i in range(11):
    for k in range(11):
        for j in range(11):
            for q in range(11):
                password = f"{i}{k}{j}{q}"
                passwords.append(password)
for password in passwords:
    try:
        with pyzipper.AESZipFile(zip_file) as file:
            file.extractall(pwd=password.encode('utf-8'))
        print(f"尝试密码{password}成功，密码就是它！{password}")
        break
    except Exception as e:
        print(f"尝试密码{password}失败，原因：{str(e)}")


