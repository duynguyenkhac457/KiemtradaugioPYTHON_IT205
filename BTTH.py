list_parking = []
auto_id = 1

while True:
    print("QUẢN LÍ BÃI XE - SMART PAKING")
    print("1. Thêm xe mới vào bãi")
    print("2. Hiển thị danh sách xe trong bãi")
    print("3. Xóa xe khỏi bãi")
    print("4. Thoát chương trình")

    choice = input("Nhập chức năng: ")

    match(choice):
        case "1":
            while True:
                print("1. Xe máy")
                print("2. Xe ô tô")
                car_type =  input("Nhập loại xe: ")
                if car_type.isdigit() and (car_type == "1" or car_type == "2"):
                    car_type = int(car_type)
                    break
                else:
                    print("Chỉ được nhập 1 hoặc 2!!!")
            name_owner = input("Nhập tên chủ xe: ") 
            if name_owner == "" :
                print("Không được để trống!!!")
            else:
                list_parking.append({
                    "id": auto_id,
                    "type": car_type,
                    "owner": name_owner
                })
                auto_id += 1
                print("Đã thêm thành công!!!")
        case "2":
            if not list_parking:
                print("Bãi xe trống!!!")
                continue

            print(f"{"ID":<5} | {"Loại xe":<10} | {"Tên chủ xe":<10}")
            print("_"*30)
            for car in list_parking:
                print(f"{car["id"]:<5} | {car["type"]:<10} | {car["owner"]:<10}")
            print("_"*30)
        case "3":
            found = False
            delete_car = int(input("Nhập ID xe muốn xóa: "))
            for car in list_parking:
                if car["id"] == delete_car:
                    list_parking.remove(car)
                    found = True
                    print("Đã xóa thành công!!!")
                    break

            if not found:
                print("Không tìm thấy xe cần xóa!")
        case "4":
            print("Đã thoát chương trình")
            break
        case _:
            print("Không hợp lệ!!!")