class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    #访问器getter方法
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    # 修改器setter方法
    @age.setter
    def age(self, age):
        self._age = age

    
    def play(self):
        print('%s正在愉快的玩耍.'%self._name)
    
    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.'%self._name)
        else:
            print('%s只能观看《熊出没》.'%self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    def study(self, course):
        print('%s的%s正在学习%s.'%(self._grade, self._name, course))

class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print('%s%s正在讲%s'%(self._name, self._title, course))


def main():
    #person = Person('王大锤', 12)
    #person.play()
    #person.age = 22
    #person.play()
    #person._gender = '男'
    #AttributeError: 'Person' object has no attribute '_is_gay'
    #person._is_gay = 'True'
    
    #AttributeError: can't set attribute
    #person.name = '白元芳'
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('corch', 38, '研究员')
    t.teach('数学')
    t.watch_av()

if __name__ == '__main__':
    main()