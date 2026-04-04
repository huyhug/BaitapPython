# ============================================================
# BÀI 1: Tính tổng các phần tử trong list
# ============================================================
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong = sum(_list)
print(f"Bài 1 - Tổng: {tong}")
# Hoặc dùng vòng lặp:
tong2 = 0
for x in _list:
    tong2 += x
print(f"Bài 1 - Tổng (vòng lặp): {tong2}")


# ============================================================
# BÀI 2: Tính tích các phần tử trong list
# ============================================================
_list = [1, 2, 3, 4, 5]
tich = 1
for x in _list:
    tich *= x
print(f"\nBài 2 - Tích: {tich}")


# ============================================================
# BÀI 3: Tách list thành list số chẵn và số lẻ
# ============================================================
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [x for x in _list if x % 2 == 0]
odd  = [x for x in _list if x % 2 != 0]
print(f"\nBài 3 - Số chẵn (even): {even}")
print(f"Bài 3 - Số lẻ  (odd) : {odd}")


# ============================================================
# BÀI 4: Lấy 2 phần tử ở vị trí thứ 2 và thứ 3
# ============================================================
_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
_new = _list[2:4]   # index 2 và 3 (vị trí thứ 3 và 4 theo đề = index 2,3)
print(f"\nBài 4 - List mới: {_new}")


# ============================================================
# BÀI 5: Thêm phần tử vào list để tạo list mới
# ============================================================
_list = ['zero', 'three']
_new = _list.copy()
_new.insert(1, 'one')   # chèn 'one' vào vị trí index 1
_new.insert(2, 'two')   # chèn 'two' vào vị trí index 2
print(f"\nBài 5 - List mới: {_new}")


# ============================================================
# BÀI 7a: Loại bỏ TẤT CẢ phần tử trùng (xóa hẳn cả nhóm trùng)
# ============================================================
_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new = [x for x in _list if _list.count(x) == 1]
print(f"\nBài 7a - Loại bỏ tất cả phần tử trùng: {_new}")


# ============================================================
# BÀI 7b: Giữ lại 1 phần tử nếu trùng lặp (unique, giữ thứ tự)
# ============================================================
_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
seen = []
_new = []
for x in _list:
    if x not in seen:
        seen.append(x)
        _new.append(x)
print(f"Bài 7b - Giữ lại 1 phần tử trùng: {_new}")


# ============================================================
# BÀI 8: Lấy số lớn nhất trong list
# ============================================================
_list = [11, 2, 23, 45, 6, 9]
lon_nhat = max(_list)
print(f"\nBài 8 - Số lớn nhất: {lon_nhat}")


# ============================================================
# BÀI 9: Lấy số nhỏ nhất trong list
# ============================================================
_list = [11, 2, 23, 45, 6, 9]
nho_nhat = min(_list)
print(f"\nBài 9 - Số nhỏ nhất: {nho_nhat}")


# ============================================================
# BÀI 10: Copy một list thành list mới
# ============================================================
_list = [1, 2, 3, 4, 5]
_new = _list.copy()      # cách 1: dùng .copy()
_new2 = list(_list)      # cách 2: dùng list()
_new3 = _list[:]         # cách 3: dùng slicing
print(f"\nBài 10 - List gốc : {_list}")
print(f"Bài 10 - List copy: {_new}")


# ============================================================
# BÀI 11: Tìm các từ có độ dài > n từ list
# ============================================================
_list = ['apple', 'hi', 'banana', 'cat', 'elephant', 'ok']
n = int(input("\nBài 11 - Nhập n: "))
ket_qua = [x for x in _list if len(x) > n]
print(f"Bài 11 - Các từ có độ dài > {n}: {ket_qua}")


# ============================================================
# BÀI 12: Đếm chuỗi thỏa: độ dài >= n VÀ ký tự đầu == ký tự cuối
# ============================================================
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
do_dai = int(input("\nBài 12 - Nhập độ dài tối thiểu: "))
dem = 0
for s in _list:
    if len(s) >= do_dai and s[0] == s[-1]:
        dem += 1
print(f"Bài 12 - Số chuỗi thỏa mãn: {dem}")