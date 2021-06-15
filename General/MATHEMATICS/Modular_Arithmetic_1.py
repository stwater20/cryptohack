#11 ≡ a mod 6
#8146798528947 ≡ b mod 17

# note https://ithelp.ithome.com.tw/articles/10205727

import sys

a=sys.maxsize
b=sys.maxsize

for i in range(sys.maxsize):
    if i % 6 == 11 % 6:
        print(i) #5
        break

for i in range(sys.maxsize):
    if i % 17 == 8146798528947 % 17:
        print(i) #4
        break