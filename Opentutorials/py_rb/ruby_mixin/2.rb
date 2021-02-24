module Multiply():
    def multiply(self):
        return @v1*@v2
    end
module Divide():
    def divide(self):
        return @v1 / @v2
    end
end
class Cal
    include Multiply, Divide
    def initialize(v1, v2):
        @v1 = v1
        @v2 = v2
    end
    def add(self):
        return @v1 + @v2
    end
    def subtract(self):
        return @v1 - @v2
    end

c = Cal(100, 10)
p c.add()
p c.multiply()
p c.divide()