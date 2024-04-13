import json

class Sach:
    def __init__(self, tenSach, tacGia, soLuong):
        self.tenSach = tenSach
        self.tacGia = tacGia
        self.soLuong = soLuong

class quanLySach:
    def __init__(self):
        self.sach = []

    def addSach(self, tenSach, tacGia, soLuong):
        self.sach.append(Sach(tenSach, tacGia, soLuong))
        print("Thêm sách thành công")
        self.luuDanhSachSach()

    def deleteS(self, tenSach):
        found = False
        for book in self.sach:
            if book.tenSach == tenSach:
                self.sach.remove(book)
                found = True
                print("Xóa sách thành công")
                break
        if not found:
            print("Sách không tồn tại")
        self.luuDanhSachSach()

    def updateS(self, tenSach, new_tacGia, new_soLuong):
        found = False
        for book in self.sach:
            if book.tenSach == tenSach:
                book.tacGia = new_tacGia
                book.soLuong = new_soLuong
                found = True
                print("Cập nhật thông tin sách thành công")
                break
        if not found:
            print("Sách không tồn tại")
        self.luuDanhSachSach()

    def sapXepDanhSachSach(self, theo_tieu_chi="tacGia"):
        if theo_tieu_chi == "tacGia":
            self.sach.sort(key=lambda x: x.tacGia)
        elif theo_tieu_chi == "soLuong":
            self.sach.sort(key=lambda x: x.soLuong)
        else:
            print("Tiêu chí không hợp lệ.")

    def hienThiSachTheoTenTacGia(self, ten):
        found = False
        for book in self.sach:
            if book.tacGia == ten:
                print(book.tenSach, book.tacGia, book.soLuong)
                found = True
        if not found:
            print("Sách không tồn tại")
    def hienThiSach(self):
        if self.sach:
            for book in self.sach:
                print(book.tenSach, book.tacGia, book.soLuong)
        else:
            print("Không có sách nào")
    def luuDanhSachSach(self):
        if self.sach:
            with open("book.json", "w") as file:
                data = [vars(book) for book in self.sach]
                json.dump(data, file, indent=4)

def menu():
    quanLy = quanLySach()
    try:
        with open("book.json", "r") as file:
            quanLy.sach = [Sach(**sach) for sach in json.load(file)]
    except FileNotFoundError:
        print("Không tìm thấy tệp dữ liệu.")

    while True:
        print("\n----------------------MENU------------------------")
        print("1. Thêm sách")
        print("2. Xóa sách")
        print("3. Cập nhật thông tin sách")
        print("4. Sắp xếp danh sách")
        print("5. Hiển thị sách theo tên tác giả")
        print("6. Hiển thị danh sách sách")
        print("7. Thoát")
        print("----------------------------------------------------------------")
        print("Vui lòng chọn chức năng:")
        chucNang = int(input())

        if chucNang == 1:
            print("Thêm sách")
            tenSach = input("Nhập tên sách: ")
            tacGia = input("Nhập tên tác giả: ")
            soLuong = int(input("Nhập số lượng: "))
            quanLy.addSach(tenSach, tacGia, soLuong)
        elif chucNang == 2:
            print("Xóa sách")
            tenSach = input("Nhập tên sách: ")
            quanLy.deleteS(tenSach)
        elif chucNang == 3:
            print("Cập nhật thông tin sách")
            tenSach = input("Nhập tên sách: ")
            tacGia = input("Nhập tên tác giả mới: ")
            soLuong = int(input("Nhập số lượng mới: "))
            quanLy.updateS(tenSach, tacGia, soLuong)
        elif chucNang == 4:
            print("Sắp xếp danh sách")
            theo_tieu_chi = input("Nhập tiêu chí (tacGia hoặc soLuong): ")
            quanLy.sapXepDanhSachSach(theo_tieu_chi)
        elif chucNang == 5:
            print("Hiển thị sách theo tên tác giả")
            ten = input("Nhập tên tác giả: ")
            quanLy.hienThiSachTheoTenTacGia(ten)
        elif chucNang == 6:
            print("Hiển thị danh sách sách")
            quanLy.hienThiSach()
        elif chucNang == 7:
            print("Kết thúc chương trình.")
menu()
           
