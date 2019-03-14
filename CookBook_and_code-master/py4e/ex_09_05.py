ffile = input('Input File:')
files = open(ffile)

def fdtc(fname):
    #取关键字-邮件地址
    a = []
    for line in fname:
        words = line.split()
        #print(words)
        if len(words) > 3 and words[0] == 'From':
            a.append(words[1])
        #字符分段，取邮件地址
    shoolCount = []
    for word in a:
        b = word.split('@')
        #    print(b[1])
        shoolCount.append(b[1])
        #字典值加权
    fb = {}
    for x in shoolCount:
        fb[x] = fb.get(x, 0) + 1

    print(fb)

fdtc(files)