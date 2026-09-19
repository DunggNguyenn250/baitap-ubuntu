import matplotlib.pyplot as plt

# 1. Nh?p s? sinh viên nam, n?
so_nam = int(input("Nh?p s? sinh viên nam trong l?p: "))
so_nu = int(input("Nh?p s? sinh viên n? trong l?p: "))

# 2. C?u h?nh d? li?u bi?u ð?
gioi_tinh = ['Nam', 'N?']
so_luong = [so_nam, so_nu]
mau_sac = ['blue', 'pink']

# 3. V? bi?u ð? c?t
plt.bar(gioi_tinh, so_luong, color=mau_sac)
plt.title('Bi?u ð? s? lý?ng sinh viên Nam và N?')
plt.xlabel('Gi?i tính')
plt.ylabel('S? lý?ng')

# 4. Lýu bi?u ð? thành file ?nh (V? ch?y trên SSH server không có UI)
ten_file = 'bieudo_namnu.png'
plt.show()
print(f"Hoàn thành bieu do")