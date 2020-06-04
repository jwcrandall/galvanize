class DoMath():
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        self.comments = []

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def change_nums(self, new_a, new_b):
        self.a = float(new_a)
        self.b = float(new_b)

    def store_comment(self, comment):
        self.comments.append(comment)
        return self.add()
