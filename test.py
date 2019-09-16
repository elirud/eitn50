with open('image.dat', encoding='latin 1') as f:
    data = f.read()

s = data.encode().hex().upper()

print(data[0:9])

print(data[0:9].encode().hex().upper())

print(len(data[0:9].encode().hex().upper()))
