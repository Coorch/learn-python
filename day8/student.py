class Student(object):

    #__init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法我们可以为学生对象绑定name和age两个属性
    #如果要属性私有，在给属性命名时用两个下划线作为开头
    def __init__(self, name, age, foo):
        self.name = name
        self.age = age
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print('__bar')

    def study(self, course_name):
        print('%s正在学习%s.'%(self.name, course_name))
    
    # REP 8要求标识符的名字用全小写，多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.'%self.name)
        else:
            print('%s正在观看岛国爱情动作片.'%self.name)