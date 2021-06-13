
string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
en = bytes.fromhex(string)

flag = bytes("crypto{","utf-8")

key = [a^b for a,b in zip(en,flag)]


print("".join(chr(o) for o in key)) # myXORke

key.append(ord("y"))
key_length = len(key)
print(key)

for i in range(len(en)):
    print(chr(en[i]^key[i%key_length]),end="")