"""
编写代码，定义一个名叫为 ListInstanceAttr 的类，显示从一个实例可以访问的所有属性名及其值。
再将这个 ListInstanceAttr 类作为超类，用在多重继承中，看一看运行结果。

- 内省（introspection）是指计算机程序在运行时（run time）检查对象（object）类型的一种能力，也称作运行时类型检查（run-time type checking）

- Introspection is an act of self examination. In computer programming, introspection is the ability to determine the type of an object at runtime.
- Python提供了可用于内省的工具，它们是类的一些特殊属性和函数，允许我们访问对象实现的一些内部机制。比如 `instance.__class__` 和 `instance.__dict__`。

"""

class ListInstanceAttr(object):
    def gather_attrs(self):
#         attrs = ['%s = %s' % (key, getattr(self, key)) for key in sorted(self.__dict__)]
#         attrs = ['%r = %r' % (key, getattr(self, key)) for key in sorted(self.__dict__)]
        attrs = [f'{key} = {getattr(self, key)}' for key in self.__dict__]
        return ', \n'.join(attrs)
    
    def __str__(self):
        return '[%s: \n%s]' % (self.__class__.__name__, self.gather_attrs())
#     def __repr__(self):
#         return '[%r: %r]' % (self.__class__.__name__, self.gather_attrs())
    
class SoccerPlayer(ListInstanceAttr):
    """
    球员基本信息统计
    ---
    param number: 球衣号码
    param name: 姓名
    param age: 年龄
    param position: 位置
    param salary: 年薪 (百万欧€)
    param contract: 合同截止年限
    param league: 联赛
    param club: 俱乐部
    """
    def __init__(self, name, number, age, position, salary, contract, league, club):
        self.name = name
        self.number = number
        self.age = age
        self.pos = position
        self.salary = salary
        self.contract = contract
        self.league = league
        self.club = club
        
class FCBPlayerData(SoccerPlayer):
    """
    FCB球员数据信息统计
    ----
    param season: 赛季
    param games: 参加比赛数
    param shots: 射门次数
    param goals: 进球数
    param assists: 助攻数
    """
    def __init__(self, name, number, age, position, salary, contract, season, games, shots, goals, assists):
        SoccerPlayer.__init__(self, name, number, age, position, salary, contract, 'Liga', 'FCB')
        self.season = season
        self.games = games
        self.shots = shots
        self.goals = goals
        self.assists = assists
        
    # 场均进球
    def avg_goals(self) -> float:
        if self.games > 0:
            return round(float(self.goals) / self.games, 2)
        else:
            raise ZeroDivisionError("[Error] divide by zero!")
    
    # 进球效率        
    def eff_goals(self) -> float:
        if self.goals > 0:
            return round(float(self.shots) / self.goals, 2)
        else:
            raise ZeroDivisionError("[Error] divide by zero!")
            
    def raise_salary(self, percent):
        self.salary = round(self.salary * (1.0 + percent), 4)
        

# if __name__ == '__main__':
#     messi = FCBPlayerData('Messi', 10, 33, 'RW', 70.7580, 2023, '20/21', 35, 196, 30, 9)
#     print(messi, '\n')
#     print('场均进球：', messi.avg_goals())
#     print('进球效率：', messi.eff_goals())

# 单元测试
import unittest

class TestPlayer(unittest.TestCase):
    def test_init(self):
        messi = FCBPlayerData('Messi', 10, 33, 'RW', 70.7580, 2023, '20/21', 35, 196, 30, 9)
        self.assertEqual(messi.name, 'Messi')
        self.assertEqual(messi.number, 10)
        self.assertEqual(messi.age, 33)
        self.assertEqual(messi.pos, 'RW')
        self.assertEqual(messi.salary, 70.7580)
        self.assertEqual(messi.contract, 2023)
#         self.assertEquals(messi, ['Messi', 10, 33, 'RW', 70.7580, 2023, '20/21', 35, 196, 30, 9])
        self.assertTrue(isinstance(messi, object))
        
if __name__ == '__main__':
    unittest.main()