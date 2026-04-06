# ============================================================
# BÀI 1: Thêm phần tử 'c' vào vị trí số 2 của tuple
# ============================================================
_tuple = ('a', 'b', 'd', 'e')

# Chuyển tuple -> list -> chèn -> chuyển lại tuple
_list = list(_tuple)
_list.insert(2, 'c')
_new_tuple = tuple(_list)

print(f"Bài 1 - Tuple gốc : {_tuple}")
print(f"Bài 1 - Tuple mới : {_new_tuple}")


# ============================================================
# BÀI 2: Loại bỏ TẤT CẢ phần tử có giá trị giống nhau (xóa cả nhóm)
# ============================================================
_tuple = ('ab', 'b', 'c', 'd', 'e', 'ab')

_new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)

print(f"\nBài 2 - Tuple gốc : {_tuple}")
print(f"Bài 2 - Tuple mới : {_new_tuple}")


# ============================================================
# BÀI 3: Loại bỏ trùng lặp, giữ lại 1 phần tử (giữ thứ tự)
# ============================================================
_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

seen = []
result = []
for x in _tuple:
    if x not in seen:
        seen.append(x)
        result.append(x)
_new_tuple = tuple(result)

print(f"\nBài 3 - Tuple gốc : {_tuple}")
print(f"Bài 3 - Tuple mới : {_new_tuple}")


# ============================================================
# BÀI LUYỆN TẬP NÂNG CAO: Mã hóa / Giải mã văn bản dùng file
# ============================================================

import json

# --- Tạo file bộ mật mã (chạy 1 lần để tạo file) ---
bo_mat_ma = {
    'a': '!', 'b': '@', 'c': '#', 'd': '$',
    'e': '%', 'f': '^', 'g': '&', 'h': '*',
    'i': '(', 'j': ')', 'k': '-', 'l': '+',
    'm': '=', 'n': '[', 'o': ']', 'p': '{',
    'q': '}', 'r': ';', 's': ':', 't': "'",
    'u': '"', 'v': ',', 'w': '.', 'x': '/',
    'y': '?', 'z': '~', ' ': '_'
}

# Lưu bộ mật mã ra file
with open('mat_ma.json', 'w', encoding='utf-8') as f:
    json.dump(bo_mat_ma, f, ensure_ascii=False, indent=2)
print("\n✅ Đã tạo file 'mat_ma.json'")


# --- Tạo file văn bản gốc ---
van_ban_goc = "hello world python"
with open('van_ban_goc.txt', 'w', encoding='utf-8') as f:
    f.write(van_ban_goc)
print("✅ Đã tạo file 'van_ban_goc.txt'")


# ============================================================
# HÀM MÃ HÓA: Đọc file văn bản, mã hóa, lưu file kết quả
# ============================================================
def ma_hoa(file_van_ban, file_mat_ma, file_ket_qua):
    # Đọc bộ mật mã
    with open(file_mat_ma, 'r', encoding='utf-8') as f:
        bo_ma = json.load(f)

    # Đọc văn bản gốc
    with open(file_van_ban, 'r', encoding='utf-8') as f:
        noi_dung = f.read()

    # Mã hóa từng ký tự
    ket_qua = ''
    for ky_tu in noi_dung:
        ket_qua += bo_ma.get(ky_tu.lower(), ky_tu)  # giữ nguyên nếu không có trong bộ mã

    # Lưu kết quả
    with open(file_ket_qua, 'w', encoding='utf-8') as f:
        f.write(ket_qua)

    print(f"\n✅ Mã hóa xong!")
    print(f"   Văn bản gốc : {noi_dung}")
    print(f"   Văn bản mã  : {ket_qua}")


# ============================================================
# HÀM GIẢI MÃ: Đọc file mã hóa, giải mã, in kết quả
# ============================================================
def giai_ma(file_ma_hoa, file_mat_ma):
    # Đọc bộ mật mã
    with open(file_mat_ma, 'r', encoding='utf-8') as f:
        bo_ma = json.load(f)

    # Đảo ngược bộ mật mã: ký hiệu -> chữ gốc
    bo_ma_nguoc = {v: k for k, v in bo_ma.items()}

    # Đọc file đã mã hóa
    with open(file_ma_hoa, 'r', encoding='utf-8') as f:
        noi_dung_ma = f.read()

    # Giải mã từng ký tự
    ket_qua = ''
    for ky_tu in noi_dung_ma:
        ket_qua += bo_ma_nguoc.get(ky_tu, ky_tu)

    print(f"\n✅ Giải mã xong!")
    print(f"   Văn bản mã  : {noi_dung_ma}")
    print(f"   Văn bản gốc : {ket_qua}")


# --- Chạy thử ---
ma_hoa('van_ban_goc.txt', 'mat_ma.json', 'van_ban_ma.txt')
giai_ma('van_ban_ma.txt', 'mat_ma.json')