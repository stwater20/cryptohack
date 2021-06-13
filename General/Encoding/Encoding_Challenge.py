from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes
from codecs import encode as rot13

def solution(r_type,r_encoded):
    if r_type == "base64":
        return base64.b64decode(r_encoded).decode('utf-8')
    elif r_type == "hex":
        return bytearray.fromhex(r_encoded).decode()
    elif r_type == "bigint":
        len_decode = len(r_encoded)
        x =  int(r_encoded, 16).to_bytes(len_decode, 'big')
        return str(x, 'UTF-8').lstrip('\x00')
    elif r_type == "rot13":
        return rot13(r_encoded,'rot13')
    elif r_type == "utf-8":
        return ''.join(chr(o) for o in r_encoded)
    else:
        print(r_encoded) 

for i in range(101):
    received = json_recv()
    print(i)
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    ans = solution(received["type"],received["encoded"])
    to_send = {
        "decoded": ans
    }
    json_send(to_send)

    # json_recv()
