import json
import random

class Employee:
    def __init__(self, ho_ten, ngay_sinh, chuc_vu, phong_ban):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.chuc_vu = chuc_vu
        self.phong_ban = phong_ban

    def cap_nhat_thong_tin(self, ho_ten, ngay_sinh, chuc_vu, phong_ban):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.chuc_vu = chuc_vu
        self.phong_ban = phong_ban

    def xoa_nhan_vien(self):
        self.ho_ten = None
        self.ngay_sinh = None
        self.chuc_vu = None
        self.phong_ban = None

class Department:
    def __init__(self, ten_phong_ban):
        self.ten_phong_ban = ten_phong_ban

    def cap_nhat_ten_phong_ban(self, ten_phong_ban):
        self.ten_phong_ban = ten_phong_ban

    def xoa_phong_ban(self):
        self.ten_phong_ban = None

class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nhan_vien = []
        self.danh_sach_phong_ban = []

    def them_moi_nhan_vien(self, ho_ten, ngay_sinh, chuc_vu, phong_ban):
        new_employee = Employee(ho_ten, ngay_sinh, chuc_vu, phong_ban)
        self.danh_sach_nhan_vien.append(new_employee)
        self.luu_danh_sach_nhan_vien()

    def cap_nhat_nhan_vien(self, index, ho_ten, ngay_sinh, chuc_vu, phong_ban):
        self.danh_sach_nhan_vien[index].cap_nhat_thong_tin(ho_ten, ngay_sinh, chuc_vu, phong_ban)
        self.luu_danh_sach_nhan_vien()

    def xoa_nhan_vien(self, index):
        self.danh_sach_nhan_vien[index].xoa_nhan_vien()
        del self.danh_sach_nhan_vien[index]
        self.luu_danh_sach_nhan_vien()

    def them_moi_phong_ban(self, ten_phong_ban):
        new_department = Department(ten_phong_ban)
        self.danh_sach_phong_ban.append(new_department)
        self.luu_danh_sach_phong_ban()

    def cap_nhat_ten_phong_ban(self, index, ten_phong_ban_moi):
        self.danh_sach_phong_ban[index].cap_nhat_ten_phong_ban(ten_phong_ban_moi)
        for employee in self.danh_sach_nhan_vien:
            if employee.phong_ban == self.danh_sach_phong_ban[index].ten_phong_ban:
                employee.phong_ban = ten_phong_ban_moi
        self.luu_danh_sach_phong_ban()
        self.luu_danh_sach_nhan_vien()

    def xoa_phong_ban(self, index):
        if self.danh_sach_phong_ban[index].ten_phong_ban:
            for employee in self.danh_sach_nhan_vien:
                if employee.phong_ban == self.danh_sach_phong_ban[index].ten_phong_ban:
                    employee.phong_ban = None
        del self.danh_sach_phong_ban[index]
        self.luu_danh_sach_phong_ban()

    def hien_thi_danh_sach_nhan_vien_theo_phong_ban(self, ten_phong_ban):
        print(f"Danh sách nhân viên trong phòng ban {ten_phong_ban}:")
        for employee in self.danh_sach_nhan_vien:
            if employee.phong_ban == ten_phong_ban:
                print(f"Họ và tên: {employee.ho_ten}, Ngày sinh: {employee.ngay_sinh}, Chức vụ: {employee.chuc_vu}, Phòng ban: {employee.phong_ban}")

    def tim_kiem_nhan_vien_theo_ten(self, ten):
        print(f"Kết quả tìm kiếm nhân viên với từ khoá '{ten}':")
        for employee in self.danh_sach_nhan_vien:
            if ten.lower() in employee.ho_ten.lower():
                print(f"Họ và tên: {employee.ho_ten}, Ngày sinh: {employee.ngay_sinh}, Chức vụ: {employee.chuc_vu}, Phòng ban: {employee.phong_ban}")

    def sap_xep_danh_sach_nhan_vien(self, theo_tieu_chi="ho_ten"):
        if theo_tieu_chi == "ho_ten":
            self.danh_sach_nhan_vien.sort(key=lambda x: x.ho_ten)
        elif theo_tieu_chi == "ngay_sinh":
            self.danh_sach_nhan_vien.sort(key=lambda x: x.ngay_sinh)
        else:
            print("Tiêu chí không hợp lệ.")

    def thong_ke_so_luong_nhan_vien_theo_phong_ban(self):
        thong_ke = {}
        for department in self.danh_sach_phong_ban:
            count = sum(1 for employee in self.danh_sach_nhan_vien if employee.phong_ban == department.ten_phong_ban)
            thong_ke[department.ten_phong_ban] = count
        print("Thống kê số lượng nhân viên theo phòng ban:")
        for phong_ban, so_luong in thong_ke.items():
            print(f"{phong_ban}: {so_luong}")

    def hien_thi_danh_sach_phong_ban(self):
        print("Danh sách phòng ban:")
        for department in self.danh_sach_phong_ban:
            print(department.ten_phong_ban)

    def luu_danh_sach_nhan_vien(self):
        with open("employee.json", "w") as file:
            data = []
            for employee in self.danh_sach_nhan_vien:
                data.append(vars(employee))
            json.dump(data, file, indent=4)

    def luu_danh_sach_phong_ban(self):
        with open("department.json", "w") as file:
            data = []
            for department in self.danh_sach_phong_ban:
                data.append(vars(department))
            json.dump(data, file, indent=4)

# Tạo menu và xử lý lựa chọn của người dùng
def menu():
    quan_ly = QuanLyNhanVien()
    try:
        with open("department.json") as file:
            quan_ly.danh_sach_phong_ban = [Department(**department) for department in json.load(file)]
    except FileNotFoundError:
        ten_phong_ban = random.sample(["Kế toán", "Nhân sự", "Marketing", "Kinh doanh"], 4)
        for ten in ten_phong_ban:
            quan_ly.them_moi_phong_ban(ten)

    try:
        with open("employee.json") as file:
            quan_ly.danh_sach_nhan_vien = [Employee(**employee) for employee in json.load(file)]
    except FileNotFoundError:
        for _ in range(12):
            ho_ten = f"{random.choice(['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh'])} {random.choice(['Văn', 'Thị', 'Hữu', 'Hoàng', 'Trọng', 'Minh', 'Tấn', 'Ngọc', 'Tiến', 'Gia'])} {random.choice(['Hải', 'Hà', 'Hùng', 'Linh', 'Minh', 'Quân', 'Thảo', 'Trang', 'Tuấn', 'Vy', 'An', 'Binh', 'Cường', 'Đức', 'Giang', 'Kiên', 'Nam', 'Phương', 'Sơn', 'Thanh'])}"
            ngay_sinh = f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1980, 2004)}"
            chuc_vu = random.choice(["Trưởng phòng", "Phó phòng", "Nhân viên"])
            phong_ban = random.choice([department.ten_phong_ban for department in quan_ly.danh_sach_phong_ban])
            quan_ly.them_moi_nhan_vien(ho_ten, ngay_sinh, chuc_vu, phong_ban)

    while True:
        print("\n----- MENU -----")
        print("1. Quản lý Nhân viên")
        print("2. Quản lý Phòng ban")
        print("3. Chức năng bổ sung")
        print("4. Thoát")

        lua_chon = input("Vui lòng chọn chức năng: ")

        if lua_chon == "1":
            menu_quan_ly_nhan_vien(quan_ly)
        elif lua_chon == "2":
            menu_quan_ly_phong_ban(quan_ly)
        elif lua_chon == "3":
            menu_chuc_nang_bo_sung(quan_ly)
        elif lua_chon == "4":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def menu_quan_ly_nhan_vien(quan_ly):
    while True:
        print("\n----- QUẢN LÝ NHÂN VIÊN -----")
        print("1. Thêm mới nhân viên")
        print("2. Cập nhật thông tin nhân viên")
        print("3. Xóa nhân viên")
        print("4. Hiển thị danh sách nhân viên theo phòng ban")
        print("5. Tìm kiếm nhân viên theo tên")
        print("6. Sắp xếp danh sách nhân viên")
        print("7. Thống kê số lượng nhân viên trong mỗi phòng ban")
        print("8. Quay lại")

        lua_chon = input("Vui lòng chọn chức năng: ")

        if lua_chon == "1":
            ho_ten = input("Nhập họ tên: ")
            ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
            chuc_vu = input("Nhập chức vụ: ")
            quan_ly.hien_thi_danh_sach_phong_ban()
            phong_ban = input("Chọn phòng ban: ")
            quan_ly.them_moi_nhan_vien(ho_ten, ngay_sinh, chuc_vu, phong_ban)
        elif lua_chon == "2":
            index = int(input("Nhập số thứ tự của nhân viên cần cập nhật: ")) - 1
            ho_ten_moi = input("Nhập họ tên mới: ")
            ngay_sinh_moi = input("Nhập ngày sinh mới (dd/mm/yyyy): ")
            chuc_vu_moi = input("Nhập chức vụ mới: ")
            quan_ly.hien_thi_danh_sach_phong_ban()
            phong_ban_moi = input("Chọn phòng ban mới: ")
            quan_ly.cap_nhat_nhan_vien(index, ho_ten_moi, ngay_sinh_moi, chuc_vu_moi, phong_ban_moi)
        elif lua_chon == "3":
            index = int(input("Nhập số thứ tự của nhân viên cần xoá: ")) - 1
            quan_ly.xoa_nhan_vien(index)
        elif lua_chon == "4":
            quan_ly.hien_thi_danh_sach_phong_ban()
            phong_ban = input("Nhập tên phòng ban: ")
            quan_ly.hien_thi_danh_sach_nhan_vien_theo_phong_ban(phong_ban)
        elif lua_chon == "5":
            ten = input("Nhập tên hoặc phần của tên nhân viên: ")
            quan_ly.tim_kiem_nhan_vien_theo_ten(ten)
        elif lua_chon == "6":
            tieu_chi = input("Chọn tiêu chí sắp xếp (ho_ten hoặc ngay_sinh): ")
            quan_ly.sap_xep_danh_sach_nhan_vien(tieu_chi)
        elif lua_chon == "7":
            quan_ly.thong_ke_so_luong_nhan_vien_theo_phong_ban()
        elif lua_chon == "8":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def menu_quan_ly_phong_ban(quan_ly):
    while True:
        print("\n----- QUẢN LÝ PHÒNG BAN -----")
        print("1. Thêm mới phòng ban")
        print("2. Cập nhật tên phòng ban")
        print("3. Xóa phòng ban")
        print("4. Hiển thị danh sách phòng ban")
        print("5. Quay lại")

        lua_chon = input("Vui lòng chọn chức năng: ")

        if lua_chon == "1":
            ten_phong_ban = input("Nhập tên phòng ban: ")
            quan_ly.them_moi_phong_ban(ten_phong_ban)
        elif lua_chon == "2":
            index = int(input("Nhập số thứ tự của phòng ban cần cập nhật: ")) - 1
            ten_phong_ban_moi = input("Nhập tên mới của phòng ban: ")
            quan_ly.cap_nhat_ten_phong_ban(index, ten_phong_ban_moi)
        elif lua_chon == "3":
            index = int(input("Nhập số thứ tự của phòng ban cần xoá: ")) - 1
            quan_ly.xoa_phong_ban(index)
        elif lua_chon == "4":
            quan_ly.hien_thi_danh_sach_phong_ban()
        elif lua_chon == "5":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def menu_chuc_nang_bo_sung(quan_ly):
    while True:
        print("\n----- CHỨC NĂNG BỔ SUNG -----")
        print("1. Sắp xếp danh sách nhân viên")
        print("2. Thống kê số lượng nhân viên trong mỗi phòng ban")
        print("3. Hiển thị danh sách nhân viên theo phòng ban")
        print("4. Quay lại")

        lua_chon = input("Vui lòng chọn chức năng: ")

        if lua_chon == "1":
            tieu_chi = input("Chọn tiêu chí sắp xếp (ho_ten hoặc ngay_sinh): ")
            quan_ly.sap_xep_danh_sach_nhan_vien(tieu_chi)
        elif lua_chon == "2":
            quan_ly.thong_ke_so_luong_nhan_vien_theo_phong_ban()
        elif lua_chon == "3":
            quan_ly.hien_thi_danh_sach_phong_ban()
            phong_ban = input("Nhập tên phòng ban: ")
            quan_ly.hien_thi_danh_sach_nhan_vien_theo_phong_ban(phong_ban)
        elif lua_chon == "4":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
