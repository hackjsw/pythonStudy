ffile = input('Input File:')
files = open(ffile)
#取出文件并比对关键词，取邮件地址
a = []
for line in files:
    words = line.split()
    #print(words)
    if len(words) > 3 and words[0] == 'From':
        a.append(words[1])
#将所有邮件地址发送的邮件数量进行统计
counts = {}
fb = {}
for x in a:
    fb[x] = fb.get(x, 0) + 1

bigcount =None
bigword = None
#在字典中比对value值
for k, v in fb.items():
    if bigcount is None or v > bigcount:
        #取出字典中value最大值并进行存储
        bigword = k
        bigcount = v

print(bigword,bigcount)