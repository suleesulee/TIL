class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1 + self.v2
        Cal._history.append("add : %d + %d= %d" %(self.v1, self.v2, result))
        return result
    def sub(self):
        result = self.v1 - self.v2
        Cal._history.append("add : %d - %d= %d" %(self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)
class CalMulti(Cal):
    def multi(self):
        result = self.v1 * self.v2
        Cal._history.append("add : %d * %d= %d" %(self.v1, self.v2, result))
        return result
    def info(self):
        return "calMultiply=> %s" %super().info()
class CalDiv(CalMulti):
    def devi(self):
        result = self.v1 / self.v2
        Cal._history.append("add : %d / %d= %d" %(self.v1, self.v2, result))
        return result
    def info(self):
        return "calMultiply=> %s" %super().info()
c0 = Cal(30, 60)
print(c0.info())

c1 = CalMulti(10,10)
print(c1.info())
c2 = CalDiv(10,10)
print(c2.info())