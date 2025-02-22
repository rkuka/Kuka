import pyzipper
import random
import os
oraginal_file = 'test.txt'
zip_file = 'test.zip'
i = random.randint(1,10)
k = random.randint(1,10)
j = random.randint(1,10)
q = random.randint(1,10)
password = f"{i}{k}{j}{q}"
with pyzipper.AESZipFile(zip_file,'w') as zip:
    zip.setpassword(password.encode())
    zip.setencryption(pyzipper.WZ_AES,nbits=256)
    zip.write(oraginal_file,arcname=oraginal_file)
print("加密并压缩成功！")