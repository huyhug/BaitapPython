class HocVien:
    # a) Tạo class HocVien với các thuộc tính
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Phương thức show_info
    def show_info(self):
        print("=== THÔNG TIN HỌC VIÊN ===")
        print("Họ tên:     ", self.ho_ten)
        print("Ngày sinh:  ", self.ngay_sinh)
        print("Email:      ", self.email)
        print("Điện thoại: ", self.dien_thoai)
        print("Địa chỉ:   ", self.dia_chi)
        print("Lớp:        ", self.lop)

    # c) Phương thức change_info với tham số mặc định
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop


# d) Chương trình chính
hv = HocVien(
    ho_ten="Hùng Đẹc Zai",
    ngay_sinh="23/04/2005",
    email="huyhung23042005z@gmail.com",
    dien_thoai="0326778717",
    dia_chi="Thanh Hóa",
    lop="IT14.5.a"
)

print("--- Trước khi thay đổi ---")
hv.show_info()

hv.change_info()

print("\n--- Sau khi thay đổi (dùng mặc định) ---")
hv.show_info()

hv.change_info(dia_chi="Thanh Hóa", lop="IT14.5")

print("\n--- Sau khi thay đổi (truyền tay) ---")
hv.show_info()