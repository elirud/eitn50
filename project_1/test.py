with open('imagehex.dat') as f:
    datahex = f.read().replace('\n', '').upper()

with open('image.dat', 'rb') as f:
    data = f.read()


def unfuck(fucked):
    unfucked = list(reversed([fucked[i:i+2] for i in range(0, len(fucked), 2)]))
    return ''.join(unfucked)


#print the first 200 FAT entries
print("First 200 FAT entries:\n------------------------")
for i in range(100):
    ab = datahex[1024+6*i:1030+6*i]
    a = ab[3] + ab[0:2]
    b = ab[4:] + ab[2]
    print(a, b)
print("------------------------")


print("The 224 root directory entries:\n------------------------")
for j in range(21):
    print(j+1)
    entry = datahex[19456+64*j:19520+64*j]
    print(len(entry))
    print(f'Filename: {unfuck(entry[0:16])} - {"".join(reversed(bytes.fromhex(unfuck(entry[0:16])).decode("utf-8")))}\nExtension: {unfuck(entry[16:22])}\nAttributes: {unfuck(entry[22:24])}\n'
          f'Creation Time: {unfuck(entry[28:32])}\nCreation Date: {unfuck(entry[32:36])}\n'
          f'Last Access Date: {unfuck(entry[36:40])}\nLast Write Time: {unfuck(entry[44:48])}\n'
          f'Last Write Date: {unfuck(entry[48:52])}\nFirst Logical Cluster: {unfuck(entry[52:56])}\n'
          f'File Size: {unfuck(entry[56:])}\n..................................')


# print(datahex.find(unfuck("04034b50").upper()))
# f = open("test.zip", "wb")
# f.write(data[148992:])
# f.close()
