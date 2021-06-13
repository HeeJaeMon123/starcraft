# class == 틀
from random import *
class Unit:
    def __init__(self, name, hp, speed):  # init : 생성자 (객체 생성시 자동 호출)
        self.name = name
        self.hp = hp 
        self.speed = speed
        print("{} unit created".format(name))

    def move(self, location):
        print("{} : {} location move [speed : {}".format(self.name, location, self.speed))


    def damaged(self, damage):
        print("{} : {} damage get".format(self.name, damage))
        self.hp -= damage
        print("currnet hp : {}".format(self.hp))
        if self.hp <=0:
            print("{} distoryed".format(self.name))



class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):  # init : 생성자 (객체 생성시 자동 호출)
        Unit.__init__(self, name, hp, speed)  # 상속하면 상위클래스의 생성자 호출해야함
        self.damage = damage

    def attack(self, location):
        print("{} : {} location attack. [damage : {}]".format(self.name, location, self.damage))

    

class Marine(AttackUnit):
    def __init__(self):
            AttackUnit.__init__(self, "marine",40,1,5)

    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{} : use stimpack".format(self.name))
        else:
            print("{} cannot use stimpack".format(self.name))


class Tank(AttackUnit):
    seize = False

    def __init__(self):
        AttackUnit.__init__(self, "tank",10,1,35)
        self.seize_mode = False

    def set_seize(self):
        if self.seize == False:  # Tank.seize로 해야하나?
            return

        if self.seize_mode == False:
            print("{} convert to seize".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{} not seize".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{} {} location [speed : {}]".format(name, location, self.speed))


class flyableattack(AttackUnit, flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp,0, damage) #  지상 speed 0
        flyable.__init__(self, speed)

    def move(self, location):

        self.fly(self.name, location)


class Wrath(flyableattack):
    def __init__(self):
        flyableattack.__init__(self, "raith",80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{} 해제".format(self.name))
            self.clocked = False
        else:
            print("{} 설정".format(self.name))
            self.clocked = True


def game_start():
    print("start!")

def game_over():
    print("player : gg")    

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wrath()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")


Tank.seize = True
print("seize mode on")

#공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize()
    elif isinstance(unit, Wrath):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")



#공격 받음
for unit in attack_units:
    unit.damaged(randint(5,20))

game_over()
