class Mathematics:
    def __init__(self, num):
        self.num = num
        self.num_copy = num

    def factorial(self):
        if self.num_copy != 0:
            self.num_copy -= 1
        if self.num_copy == 0:
            return 1
        else:
            return (self.num_copy + 1) * self.factorial()

    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num

    def square_root(self):
        return self.num ** 0.5