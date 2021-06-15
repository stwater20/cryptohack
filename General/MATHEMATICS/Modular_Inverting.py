# 3 * d ≡ 1 mod 13


import sys

d = sys.maxsize

for i in range(d):
    if (3*i) % 13 == 1 % 13:
        print(i)
        break


