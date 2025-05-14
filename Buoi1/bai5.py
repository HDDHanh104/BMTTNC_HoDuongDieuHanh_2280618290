# Nhập số giờ làm việc hàng tuần và mức lương theo giờ
gio_lam_viec = float(input("Nhập số giờ làm việc hàng tuần của nhân viên: "))
luong_theo_gio = float(input("Nhập mức lương theo giờ tiêu chuẩn: "))

# Số giờ tiêu chuẩn mỗi tuần
gio_tieu_chuan = 44

# Kiểm tra nếu số giờ làm việc vượt quá số giờ tiêu chuẩn
if gio_lam_viec > gio_tieu_chuan:
    # Tính lương cho số giờ làm việc tiêu chuẩn (44 giờ)
    luong_tieu_chuan = gio_tieu_chuan * luong_theo_gio
    
    # Tính số giờ làm thêm
    gio_lam_them = gio_lam_viec - gio_tieu_chuan
    
    # Tính lương cho số giờ làm thêm (150% mức lương theo giờ)
    luong_lam_them = gio_lam_them * luong_theo_gio * 1.5
    
    # Tổng lương thực nhận
    luong_thuc_nhan = luong_tieu_chuan + luong_lam_them
else:
    # Nếu số giờ làm việc không vượt quá 44 giờ, chỉ tính lương theo giờ
    luong_thuc_nhan = gio_lam_viec * luong_theo_gio

# In ra số tiền thực nhận của nhân viên
print(f"Số tiền thực nhận của nhân viên là: {luong_thuc_nhan:.2f} VND")
