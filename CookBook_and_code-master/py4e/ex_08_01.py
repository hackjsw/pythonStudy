listNum = [1, 3, 5, 2, 5]

def chop(x):
    #删除数组第一个和最后一个元素
    del x[0]
    del x[-1]
    return None

def middle(x):
    #获取数组除头尾的值
    a = x[1:-1]
    return a

newList = middle(listNum)

print(listNum)
print(newList)

chop(listNum)
print(listNum)
