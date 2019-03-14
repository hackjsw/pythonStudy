ffile = open(r"C:\Users\KTZ\Desktop\pythonStudy\mbox-short.txt")
x = ''
count = 0
tot = 0
for line in ffile:
    if line.startswith("X-DSPAM-Confidence:"):
        x = float(line[line.find(':')+1:])
        tot += x
        count += 1
    else:
        continue
print('Average spam confidence:{0}'.format(tot/count))