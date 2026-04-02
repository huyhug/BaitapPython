class BaiTap:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def phep_toan_so_hoc(self):
        print("=== Phép toán số học ===")
        print("a + b =", self._a + self._b)
        print("a - b =", self._a - self._b)
        print("a * b =", self._a * self._b)
        print("a / b =", self._a / self._b)
        print("a ** b =", self._a ** self._b)

    def phep_toan_quan_he(self):
        print("\n=== Phép toán quan hệ ===")
        print("a > b:", self._a > self._b)
        print("a < b:", self._a < self._b)
        print("a == b:", self._a == self._b)
        print("a != b:", self._a != self._b)

    def phep_toan_gan(self):
        print("\n=== Phép toán gán ===")
        x = self._a
        x += self._b
        print("a += b:", x)

        x = self._a
        x -= self._b
        print("a -= b:", x)

        x = self._a
        x *= self._b
        print("a *= b:", x)

        x = self._a
        x /= self._b
        print("a /= b:", x)

    def phep_toan_logic(self):
        print("\n=== Phép toán logic ===")
        print("(a > b) and (b < c):", (self._a > self._b) and (self._b < self._c))
        print("(a > b) or (b > c):", (self._a > self._b) or (self._b > self._c))
        print("not(a > b):", not(self._a > self._b))

    def phep_toan_bit(self):
        print("\n=== Phép toán bit ===")
        print("a & b:", self._a & self._b)
        print("a | b:", self._a | self._b)
        print("~a:", ~self._a)
        print("a ^ b:", self._a ^ self._b)
        print("a << 3:", self._a << 3)
        print("a >> 2:", self._a >> 2)


bt = BaiTap(16, 3, 5)

bt.phep_toan_so_hoc()
bt.phep_toan_quan_he()
bt.phep_toan_gan()
bt.phep_toan_logic()
bt.phep_toan_bit()
