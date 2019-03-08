import os  # 引入文件操作库

def CEF(path):
   for root, dirs, files in os.walk(path):
    if not os.listdir(root):
        #os.rmdir(root)
        print('delete foldersname: '+ root)
    for file in files:
        #if os.path.getsize(file) == 0:
        print(file)

if __name__ == "__main__":  # 执行本文件则执行下述代码
    path = input("Please input the files path:")  # 输入路径
    CEF(path)
