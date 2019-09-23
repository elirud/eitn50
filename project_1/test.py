with open('imagehex.dat') as f:
    datahex = f.read().replace('\n', '').upper()


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

print(datahex)
print(len(datahex))

print("The 224 root directory entries:\n------------------------")
for j in range(8):
    print(j+1)
    entry = datahex[19456+64*j:19520+64*j]
    print(f'Filename: {unfuck(entry[0:8])}\nExtension: {unfuck(entry[8:11])}\nAttributes: {unfuck(entry[11:13])}\n'
          f'Creation Time: {unfuck(entry[14:16])}\nCreation Date: {unfuck(entry[16:18])}\n'
          f'Last Access Date: {unfuck(entry[18:20])}\nLast Write Time: {unfuck(entry[22:24])}\n'
          f'Last Write Date: {unfuck(entry[24:26])}\nFirst Logical Cluster: {unfuck(entry[26:28])}\n'
          f'File Size: {unfuck(entry[28:])}\n..................................')

