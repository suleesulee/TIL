'''
easy한 문제.. __init__ 메소드에서 같은 클래스에서 계속 사용될 m_log를 선언후 사용한다는 것
이 부분이 파이썬 문법이 약하면 헷갈린다(전역으로 써야하나 init안에 넣어야하나)
'''


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m_log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.m_log :
            if self.m_log[message] <= timestamp:
                self.m_log[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.m_log[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)