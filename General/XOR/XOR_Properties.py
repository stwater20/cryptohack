# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

from pwn import xor

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key1_key3_key2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1 = [o for o in bytes.fromhex(key1)]
k1_k2 = [o for o in bytes.fromhex(key2_key1)]
k2_k3 = [o for o in bytes.fromhex(key2_key3)]
f_k1_k3_k2 = [o for o in bytes.fromhex(flag_key1_key3_key2)]
k2 = [a^b for (a,b) in zip(k1,k1_k2)]
k3 = [a^b for (a,b) in zip(k2,k2_k3)]
flag = [a^b^c^d for (a,b,c,d) in zip(k1,k2,k3,f_k1_k3_k2)]
print("".join(chr(o) for o in flag))

