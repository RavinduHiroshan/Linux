import hashlib
userInput=str(input())
noise=bytes("Km5d5ivMy8iexuHcZrsD","ascii")
epoh=200000
conver = bytes(userInput,"ascii")
output = hashlib.pbkdf2_hmac('sha512', conver, noise , epoh)
print(output.hex())

