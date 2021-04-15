import threading
import time


lock = threading.Lock()

class Account:
    """
    模拟银行账户
    """
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    """
    模拟取钱函数
    -------------------------------------------------------------------------
    with语句的目的是简化try/finally模式

    with 语句实质是上下文管理。
    1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
    2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
    3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
    4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法。

    自定义类必须包含上述几个方法才能正确使用with关键字。

    Ref: https://www.jianshu.com/p/5b01fb36fd4c
    -------------------------------------------------------------------------
    :param account:
    :param amount:
    :return:
    """
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            print("Thread ", threading.current_thread().name, "取钱成功！")
            account.balance -= amount
            print("Thread ", threading.current_thread().name, "当前余额：", account.balance)
        else:
            print("Thread ", threading.current_thread().name, "余额不足，取钱失败！")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))

    ta.start()
    tb.start()