import matplotlib.pyplot as plt

# 1. Nhập số lượng sinh viên từ Terminal
so_nam = int(input("Nhập số sinh viên nam: "))
so_nu = int(input("Nhập số sinh viên nữ: "))

# 2. Tạo biểu đồ cột
categories = ['Nam', 'Nữ']
counts = [so_nam, so_nu]

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(categories, counts, color=['#1f77b4', '#d62728'], width=0.4)

# 3. Thêm nhãn và tiêu đề
ax.set_ylabel('Số lượng sinh viên')
ax.set_xlabel('Giới tính')
ax.set_title('THỐNG KÊ SỐ LƯỢNG SINH VIÊN NAM VÀ NỮ', fontsize=11, fontweight='bold')
ax.set_ylim(0, max(counts) + 5 if max(counts) > 0 else 10)

# Hiển thị số liệu chi tiết trên đỉnh mỗi cột
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.3, f'{int(height)}', ha='center', va='bottom')

# 4. Lưu biểu đồ thành file ảnh bieu_do.png (Sát lề trái)
plt.savefig('bieu_do.png', bbox_inches='tight')
print("\nĐã lưu biểu đồ thành công vào file 'bieu_do.png' trong thư mục hiện tại!")

# 5. Hiển thị trực tiếp cửa sổ biểu đồ (Sát lề trái)
try:
    plt.show()
except Exception:
    pass