# 1
# class Doktor:
#     def __init__(self,name):
#         self.name = name
#         self.bemorlar = []
#     def add_bemor(self,bemor_name):
#         self.bemorlar.append(bemor_name)
#     def show_bemor(self):
#         return self.bemorlar
#     def count_bemor(self):
#         return len(self.bemorlar)
# class Kasalxona:
#     def __init__(self,name):
#         self.name = name
#         self.doktors = []
#     def add_doctor(self,doctor_name):
#         self.doktors.append(doctor_name)
#     def show_doctors(self):
#         for nomeri , doctor_ismi in enumerate(self.doktors):
#             print(f"{nomeri+1}.{doctor_ismi.name} Navbat soni: {doctor_ismi.count_bemor()}")
# class Bemor:
#     def __init__(self,name):
#         self.name = name
#     def choose_doctor(self,doctor_name):
#         doctor_name.add_bemor(self.name)
#         print(f"{self.name} {doctor_name.name}'ga navbatga yozildingiz")
#         print("Navbatdagi bemorlar:" , doctor_name.show_bemor())
#         print("Jami bemorlar soni: " , doctor_name.count_bemor())
# shifoxona = Kasalxona("1-son Markaziy Poliklinika")
# dok1 = Doktor("Dr.Vali")
# dok2 = Doktor("Dr.Ali")
# shifoxona.add_doctor(dok1)
# shifoxona.add_doctor(dok2)

# bemor1 = Bemor("Valijon")
# bemor2 = Bemor("Ulug'bek")
# bemor3 = Bemor("Yoqubboy")

# bemor1.choose_doctor(dok1)
# bemor2.choose_doctor(dok2)
# bemor3.choose_doctor(dok1)

# shifoxona.show_doctors()



# 2
# class Mashina:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         self.boshlangich = price/2
#         self.mijoz = []
#     def add_mijoz(self,mijoz_name):
#         self.mijoz.append(mijoz_name)
#     def show_mijoz(self):
#         return self.mijoz
#     def count_mijoz(self):
#         return len(self.mijoz)
#     def boshlangich_tolov(self):
#         return f"Boshlang'ich to'lov: {self.boshlangich}"
# class Avtosalon:
#     def __init__(self,name):
#         self.name = name
#         self.cars = []
#     def add_car(self,car_name):
#         self.cars.append(car_name)
#     def show_car(self):
#         for index , mashina_nomi in enumerate(self.cars):
#             print(f"{index+1}.{mashina_nomi.name} Navbatdagilar soni: {mashina_nomi.count_mijoz()}")
# class Mijoz:
#     def __init__(self,name):
#         self.name = name
#     def choose_car(self,car_name):
#         car_name.add_mijoz(self.name)
#         print(f"{self.name} {car_name.name} mashinasiga navbatga yozildingiz")
#         print(f"Mashinaning narxi: {car_name.price}")
#         print(f"{car_name.boshlangich_tolov()}")
#         print("Navbatdagi mijozlar soni" , car_name.show_mijoz())
#         print("Jami mijozlar soni" , car_name.count_mijoz())
# avtosalon = Avtosalon("Avtosalon")
# car1 = Mashina("Kia K5",43980)
# car2 = Mashina("Trecker2",19660)
# avtosalon.add_car(car1)
# avtosalon.add_car(car2)

# mijoz1 = Mijoz("Rayhona")
# mijoz2 = Mijoz("Sevinchoy")
# mijoz3 = Mijoz("Mirzabek")

# mijoz1.choose_car(car1)
# mijoz2.choose_car(car2)
# mijoz3.choose_car(car1)

# avtosalon.show_car()



# 3
class Taom:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.mijoz = []
    def add_mijoz(self,mijoz_name):
        self.mijoz.append(mijoz_name)
    def show_mijoz(self):
        return self.mijoz
    def count_mijoz(self):
        return len(self.mijoz)
class Restoran:
    def __init__(self,name):
        self.name = name
        self.taom = []
    def add_dish(self,dish):
        self.taom.append(dish)
    def show_dish(self):
        for i , nomi in enumerate(self.taom):
            print(f"{i+1}.{nomi.name} bu taomni tanlaganlar soni: {nomi.count_mijoz()}")
class Mijoz:
    def __init__(self,name):
        self.name = name
    def choose_dish(self, dish):
        dish.add_mijoz(self.name)
        print(f"{self.name} {dish.name} taomini tanladingiz")
        print(f"Taom narxi: {dish.price}")
        # print(f"{dish.umumiy_narx()}")
restoran = Restoran("Restoran")
taom1 = Taom("Chees burger",35000)
taom2 = Taom("Pizza",10000)
taom3 = Taom("Lavash",40000)
restoran.add_dish(taom1)
restoran.add_dish(taom2)
restoran.add_dish(taom3)

mijoz1 = Mijoz("Rayhona")
mijoz2 = Mijoz("Dilnura")

mijoz1.choose_dish(taom1)
mijoz2.choose_dish(taom3)

restoran.show_dish()