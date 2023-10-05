class Numbers(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self):
        MULTIPLIER = 7
        return self.x * MULTIPLIER

n3 = Numbers(2,3)
result1 = n3.multiply()
print("Result of multiplication:", result1)

n2 = Numbers(4,5)
result2 = n2.add()
print("Result of addition:", result2)
