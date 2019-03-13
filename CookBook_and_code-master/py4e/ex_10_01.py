ffile = open(r"C:\Users\KTZ\Desktop\pythonStudy\mbox-short.txt")

for line in ffile:
    print(line.rstrip().upper())