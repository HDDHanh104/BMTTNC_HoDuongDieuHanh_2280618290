def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    return False

# Sử dụng hàm và in kết quả
my_dict = {'a': 10, 'b': 6, 'c': 2, 'd': 47}
key_to_delete = 'd'

result = xoa_phan_tu(my_dict, key_to_delete)

if result:
    print("Phần tử đã được xóa. Dictionary sau khi xóa:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")
