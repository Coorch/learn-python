"""
定义一个类 
描述平面上的点
并提供移动点
和计算与另一个点间的距离
"""
from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        # 初始化
        # x为横坐标，y为纵坐标
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        # 移动到新的横坐标和新的纵坐标
        self.x = x
        self.y = y
    
    def move_by(self, dx, dy):
        # 提供移动的增量
        self.x += dx
        self.y += dy
    
    def distance_to(self, other):
        # other是另一个点
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx*dx + dy*dy)

    def __str__(self):
        #return '(%s, %s)'%(str(self.x), str(self.y))
        return '(%d, %d)'%(self.x, self.y)

    def __repr__(self):
        return 'zzzz'

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()
