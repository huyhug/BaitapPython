import math

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0!")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def __str__(self):
        if self.mau_so == 1:
            return str(self.tu_so)
        return f"{self.tu_so}/{self.mau_so}"

    def __repr__(self):
        return self.__str__()

    def nhan(self, other):
        """Nhân 2 phân số"""
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def chia(self, other):
        """Chia 2 phân số"""
        if other.tu_so == 0:
            raise ValueError("Không thể chia cho phân số có tử số = 0!")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau).toi_gian()

    def tong(self, other):
        """Tổng 2 phân số"""
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def hieu(self, other):
        """Hiệu 2 phân số"""
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def toi_gian(self):
        """Tối giản phân số"""
        ucln = math.gcd(abs(self.tu_so), abs(self.mau_so))
        tu = self.tu_so // ucln
        mau = self.mau_so // ucln
        # Đảm bảo mẫu số luôn dương
        if mau < 0:
            tu, mau = -tu, -mau
        return PhanSo(tu, mau)


# ========== TEST ==========
a = PhanSo(1, 2)   # 1/2
b = PhanSo(3, 4)   # 3/4

print(f"a = {a}")
print(f"b = {b}")
print(f"a × b = {a.nhan(b)}")
print(f"a ÷ b = {a.chia(b)}")
print(f"a + b = {a.tong(b)}")
print(f"a - b = {a.hieu(b)}")
print(f"Tối giản 6/9 = {PhanSo(6, 9).toi_gian()}")

# Test mẫu số mặc định = 1
c = PhanSo(5)
print(f"\nc = {c}  (mẫu số mặc định = 1)")

# Test lỗi mẫu số = 0
try:
    d = PhanSo(1, 0)
except ValueError as e:
    print(f"Lỗi: {e}")