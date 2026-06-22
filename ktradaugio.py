from abc import ABC, abstractmethod


class XeCoBan(ABC):
    def __init__(self, bien_so):
        self.bien_so = bien_so
        self.__dong_ho_km = 0

    @property
    def dong_ho_km(self):
        return self.__dong_ho_km

    def chay(self, quang_duong):
        if quang_duong <= 0:
            raise ValueError("Quãng đường phải là số dương")
        self.__dong_ho_km += quang_duong

    @abstractmethod
    def tinh_hieu_suat(self):
        pass

    def __lt__(self, xe_khac):
        if not isinstance(xe_khac, XeCoBan):
            return NotImplemented
        return self.__dong_ho_km < xe_khac.__dong_ho_km

    @staticmethod
    def kiem_tra_bien_so(bien_so):
        return len(bien_so) == 9 and bien_so.startswith("29")


class TinhNangTuHanh:
    def tinh_hieu_suat(self):
        return 95.0


class XeBuytDien(XeCoBan):
    def tinh_hieu_suat(self):
        hieu_suat = 100 - (self.dong_ho_km * 0.005)
        return max(hieu_suat, 50.0)


class RoboBus(XeBuytDien, TinhNangTuHanh):
    def tinh_hieu_suat(self):
        hieu_suat_dien = XeBuytDien.tinh_hieu_suat(self)
        hieu_suat_ai = TinhNangTuHanh.tinh_hieu_suat(self)
        return (hieu_suat_dien + hieu_suat_ai) / 2


def main():
    xe_hien_tai = None

    while True:
        print("\n===== MENU ROBOBUS =====")
        print("1. Khởi tạo xe RoboBus")
        print("2. Giả lập chạy xe")
        print("0. Thoát")

        lua_chon = input("Chọn chức năng: ")

        match lua_chon:
            case "1":
                while True:
                    bien_so = input("Nhập biển số xe: ")
                    if XeCoBan.kiem_tra_bien_so(bien_so):
                        xe_hien_tai = RoboBus(bien_so)
                        print("Khởi tạo RoboBus thành công!")
                        print("MRO:", [lop.__name__ for lop in RoboBus.__mro__])
                        break
                    else:
                        print("Biển số không hợp lệ, nhập lại.")

            case "2":
                if xe_hien_tai is None:
                    print("Chưa có xe được khởi tạo.")
                    continue
                try:
                    quang_duong = float(input("Nhập số km đã chạy: "))
                    xe_hien_tai.chay(quang_duong)
                    hieu_suat = xe_hien_tai.tinh_hieu_suat()
                    print("Tổng km đã đi:", xe_hien_tai.dong_ho_km)
                    print("Hiệu suất hiện tại:", round(hieu_suat, 2))
                except ValueError as loi:
                    print("Lỗi:", loi)

            case "0":
                print("Thoát chương trình.")
                break

            case _:
                print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()