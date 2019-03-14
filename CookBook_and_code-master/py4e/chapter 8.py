ffile = open(r"C:\Users\KTZ\Desktop\pythonStudy\mbox-short.txt")

for line in ffile:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])