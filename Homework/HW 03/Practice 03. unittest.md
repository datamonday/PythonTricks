```python
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
        

if __name__ == '__main__':
    messi = FCBPlayerData('Messi', 10, 33, 'RW', 70.7580, 2023, '20/21', 35, 196, 30, 9)
    print(messi, '\n')
    print('场均进球：', messi.avg_goals())
    print('进球效率：', messi.eff_goals())
```

    [FCBPlayerData: 
    name = Messi, 
    number = 10, 
    age = 33, 
    pos = RW, 
    salary = 70.758, 
    contract = 2023, 
    league = Liga, 
    club = FCB, 
    season = 20/21, 
    games = 35, 
    shots = 196, 
    goals = 30, 
    assists = 9] 
    
    场均进球： 0.86
    进球效率： 6.53
    

## 4.1 unittest 模块使用
- 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
- 如果单元测试通过，说明被测试的函数能正常工作。如果不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。
- 这种以测试为驱动的开发模式最大的好处：确保一个程序模块的行为符合设计的测试用例。在将来修改时，可以极大程度地保证该模块行为仍然正确。

- 为了编写单元测试，需要引入Python自带的unittest模块。
- unittest是python的标准的单元测试框架，能够很好的和自动化测试相结合，并有独立的测试报告框架。

---
unittest的主要有四部分构成:
- test fixture: 用于初始化、清理等动作。
- test case: 测试用例，unittest的最小单元。用以对指定输入的返回结果进行检测。在unittest中提供 了TestCase基类，用来创建新的测试用例类。
- test suite: 测试套件，一系列测试用例或测试套件的集合。在unittest中由TestSuite类实现。
- test runner: 测试执行器，负责用例执行并生成测试报告，在unittest中提供了命令行模式和GUI模式来执行。


> Reference: 
>
> https://www.jianshu.com/p/4a17a3040f07
>
> https://www.jianshu.com/p/9cee0c8cb8fc

---
以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
```python
with self.assertRaises(KeyError):
    value = d['empty']
```
而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
```python
with self.assertRaises(AttributeError):
    value = d.empty
```


```python
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
```

    E
    ======================================================================
    ERROR: C:\Users\34123\AppData\Roaming\jupyter\runtime\kernel-9644a50b-5aeb-4689-a1d6-023c67ce95c7 (unittest.loader._FailedTest)
    ----------------------------------------------------------------------
    AttributeError: module '__main__' has no attribute 'C:\Users\34123\AppData\Roaming\jupyter\runtime\kernel-9644a50b-5aeb-4689-a1d6-023c67ce95c7'
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (errors=1)
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: True
    


    D:\anaconda\envs\tensorflow\lib\site-packages\IPython\core\interactiveshell.py:3445: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
    
