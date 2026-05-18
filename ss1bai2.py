print('--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN---')
name_patient = input("Nhập tên bệnh nhân: ")
weight = float(input("Nhập cân nặng bệnh nhân: "))
print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ---")
print("Bệnh nhân: ", name_patient)
print("Cân nặng đã nhập: ", weight)
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là: ", type(weight))
#=== PHÂN TÍCH LỖI ===
# 1. Trace code: Giả sử nhập Tên = "An", Cân nặng = 50. Khi chạy đến dòng cuối,
#    hàm type(weight) sẽ trả về kiểu <class 'str'> (chuỗi) chứ không phải kiểu số.
# 2. Đặc điểm hàm input(): Mặc định trong Python, tất cả dữ liệu đi qua hàm input() 
#    nhập từ bàn phím vào đều được tự động coi là một chuỗi ký tự (String).
# 3. Nguyên nhân lưu dạng chuỗi: Do khi nhận cân nặng ở dòng `weight = input(...)`, 
#    code không dùng hàm ép kiểu (như int() hoặc float()) để chuyển chuỗi thành số.
# -> Cách sửa: Đổi thành `weight = float(input("Nhập cân nặng bệnh nhân : "))`