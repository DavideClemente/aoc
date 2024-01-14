import hashlib
prefix = "iwrupvqb"
i = 0
while True:
    string = prefix + str(i)
    result = hashlib.md5(string.encode())
    hex = result.hexdigest()
    if hex.startswith("000000"):
        print(i)
        break
    i += 1
