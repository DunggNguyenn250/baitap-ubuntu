import plotext as plt

# 1. Nhập số sinh viên nam, nữ
so_nam = int(input("Nhập số sinh viên nam trong lớp: "))
so_nu = int(input("Nhập số sinh viên nữ trong lớp: "))

# 2. Cấu hình dữ liệu biểu đồ
gioi_tinh = ['Nam', 'Nu']  # Dùng chữ không dấu để tránh lỗi font trên Terminal SSH
so_luong = [so_nam, so_nu]

# 3. Vẽ biểu đồ cột
plt.bar(gioi_tinh, so_luong)

# 4. Thêm tiêu đề và tên các trục
plt.title("Bieu do so luong sinh vien Nam va Nu")
plt.xlabel("Gioi tinh")
plt.ylabel("So luong")

# 5. Thiết lập kích thước đồ họa cho cửa sổ Terminal
plt.plotsize(50, 15)

# 6. Hiển thị biểu đồ
print("\n" + "="*50)
plt.show()
print("="*50)