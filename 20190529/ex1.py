'''奥特曼打小怪兽
需要用到抽象类
魔法，装饰器
'''
from abc import abstractclassmethod, ABCMeta
from random import randint,randrange


class Fighter(object, metaclass = ABCMeta):
    #战斗者
    __slots__ = ('_name', '_hp') #魔法限制此类只能绑定名字和血量两个属性

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp
    
    @property
    def alive(self):
        return self._hp > 0
    
    @abstractclassmethod
    def attack(self, other):
        '''攻击
        param other：被攻击对象

        '''
        pass
    

class Ultraman(Fighter):
    #奥特曼

    __slots__ = ('_name', '_hp', '_mp')#相比于父类可多绑定一个魔法属性

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self, other):
        #普攻，被攻击对象生命随机减少15-25
        other.hp -= randint(15, 25)
    
    def huge_attack(self, other):
        """究极必杀技
        打掉对方至少50点血或四分之三血
        即四分之三血量不大于50时，打掉50点血；大于50，打掉四分之三血
        必杀技消耗很大，需要50点魔法值，如果不足，发动失败
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >=50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other) # 只能发动普攻
            return False
    
    def magic_attack(self, others):
        '''魔法群攻
        此招需要耗费20点魔法值，不足则发动失败
        发动成功，对被攻击全员造成随机10-15的伤害
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp._hp -= randint(10, 25)
            return True
        else:
            return False
    
    def resume(self):
        #恢复魔法值
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n'%self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    #小怪兽

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)
    
    def __str__(self):
        return '~~~%s小怪兽~~~\n'%self._name + \
            '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    #判断有没有小怪兽存活
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive_one(monsters):
    #选中一只或者的小怪兽
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    #显示奥特曼和小怪兽的信息
    print(ultraman)
    for monster in monsters:
        print(monster)


def main():
    u = Ultraman('corch', 1000, 120)
    m1 = Monster('di', 250)
    m2 = Monster('bai', 500)
    m3 = Monster('chui', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%2d个回合========'% fight_round)
        m = select_alive_one(ms) # 
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.'%(u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.'%(u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.'%u.name)
            else:
                print('%s使用魔法失败.'%u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s'%(u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.'%(u.name, m.name))
                print('%s的魔法值恢复了%d点.'%(u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s.'%(m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n========战斗结束！========\n')
    if u.alive > 0:
        print('奥特曼%s胜利'%u.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()