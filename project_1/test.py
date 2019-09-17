import codecs

decode_hex = codecs.getdecoder("hex_codec")

with open('imagehex.dat') as f:
    datahex = f.read().replace('\n', '').upper()

for i in range(100):
    ab = datahex[1024+6*i:1030+6*i]
    a = ab[3] + ab[0:2]
    b = ab[4:] + ab[2]
    print(a, b)

# s = data.encode().hex().upper()
#
# print(data[0:9])
#
# print(data[0:9].encode().hex().upper())
#
# print(len(data[0:9].encode().hex().upper()))
