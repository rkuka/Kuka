import os
import random
import pyzipper
ordernery_file = 'test.txt'
zip_file = 'test.zip'

i = random.randint(1,10)
k = random.randint(1,10)
j = random.randint(1,10)
q = random.randint(1,10)
password = f"{i}{k}{j}{q}"
with pyzipper.AESZipFile(zip_file,'w') as zip:
    zip.setpassword(password.encode())
    zip.setencryption(pyzipper.WZ_AES,nbits=256)
    for root,_,files in os.walk('C:'):
        for ordernery_file in files:
            file_path = os.path.join(root,ordernery_file)
            zip.write(file_path,arcname=file_path)
print("加密并压缩成功！")
print('\n',f"密码是{password}")