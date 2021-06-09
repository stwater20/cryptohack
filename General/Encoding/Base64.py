import base64


string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

string_byte = bytearray.fromhex(string)

print(base64.b64encode(string_byte))
