from student import Student

def main():
    stu1 = Student('蔡徐坤', 18, 'hello')
    stu1.study('唱跳rap篮球')
    stu1.watch_av()
    stu2 = Student('王大锤', 15, 'hello')
    stu2.study('思想品德')
    stu2.watch_av()
    #stu2.__bar() # AttributeError: 'Student' object has no attribute '__bar'
    #print(stu2.__foo) # AttributeError: 'Student' object has no attribute '__foo'
    stu2._Student__bar()


if __name__ == '__main__':
    main()