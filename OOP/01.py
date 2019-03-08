#定义一个空类
class Student():
    pass


#定义一个对象
mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = 'Python'

    def doHomeWork(self):
        print('doing homework')

        return None

#实例化,具体人物
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomeWork()
