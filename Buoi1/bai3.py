# Nhập số từ người dùng
so = int(input("Nhập một số: "))

# Kiểm tra số chẵn hay lẻ
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")
