print("                                作者     ：     顾家                     ",'\n')
print('To  xxx ：')
import time
words = "love"
for item in words.split():
 letterlist = []
 for y in range(12, -12, -1):
  list_X = []
  letters = ''
  for x in range(-30, 30):
   expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
   if expression <= 0:
    letters += item[(x-y) % len(item)]
   else:
    letters += ' '
  list_X.append(letters)
  letterlist += list_X
 print('\n'.join(letterlist))
 time.sleep(0.5)
print('                                           Yours,')
print('                                           xxx')
time.sleep(30)