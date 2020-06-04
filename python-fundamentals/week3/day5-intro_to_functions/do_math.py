class DoMath():
    def _init_(self, a, b):
        self.a = float(a)
        self.b = float(b)
        self.comments = []

    def add(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def change_num(self, new_a, new_b):
        self.a = float(new_a)
        self.b = float(new_b)

    def store_comment(self, comment):
        self.comments.append(comment)
        return self.add()
