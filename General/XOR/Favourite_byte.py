string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

s_hex = [o for o in bytes.fromhex(string)]

print(s_hex)


ans = "crypto"

for i in range(128):
    temp = [chr(i^o) for o in s_hex]
    temp = "".join(o for o in temp)
    if str(temp).find(ans)!= -1:
        print(temp)
        break