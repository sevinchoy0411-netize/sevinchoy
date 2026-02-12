# class Shifoxona:
#     def __init__(self,shifoxona_nomi):
#         self.name = shifoxona_nomi
#         self.doctors = {
#             1:"Xasanov G'olibjon",
#             2:"Rahmanova Rayhona",
#             3:"Ozodov Mashhur",
#             4:"Saparboyeva Fotima"
#         }
#         self.lor = 0
#         self.lorr = []
#         self.pediatr = 0
#         self.pediatrr = []
#         self.stomatolog = 0
#         self.stomatologr = []
#         self.xirurg = 0
#         self.xirurgr = []
#     def reserve(self,ism):
#         print("Doktorlar ro'yxati")
#         for tartib , doctor in self.doctors.items():
#             print(f"{tartib} - {doctor}")
#         tanlov = int(input("Kerakli doktorni tanlang: "))
#         if tanlov == 1:
#             self.lor += 1
#             self.lorr.append(ism)
#             if self.lor == 1:
#                 print("Siz qabulga birinchi bo'lib yozildingiz")
#             else:
#                 print(f"Siz navbatga {self.lor}-bo'lib yozildingiz. Sizdan oldin {self.lorr[-2]}")
#         elif tanlov == 2:
#             self.pediatr += 1
#             self.pediatrr.append(ism)
#             if self.pediatr == 1:
#                 print("Siz qabulga birinchi bo'lib yozildingiz")
#             else:
#                 print(f"Siz navbatga {self.pediatr}-bo'lib yozildingiz. Sizdan oldin {self.pediatrr[-2]}")
#         elif tanlov == 3:
#             self.stomatolog += 1
#             self.stomatologr.append(ism)
#             if self.stomatolog == 1:
#                 print("Siz qabulga birinchi bo'lib yozildingiz")
#             else:
#                 print(f"Siz navbatga {self.stomatolog}-bo'lib yozildingiz. Sizdan oldin {self.stomatologr[-2]}")
#         elif tanlov == 4:
#             self.xirurg += 1
#             self.xirurgr.append(ism)
#             if self.xirurg == 1:
#                 print("Siz qabulga birinchi bo'lib yozildingiz")
#             else:
#                 print(f"Siz navbatga {self.xirurg}-bo'lib yozildingiz. Sizdan oldin {self.xirurgr[-2]}")
# kasal = Shifoxona("Markaziy shifoxona")    
# print(kasal.reserve("Aliyev Vali"))
# print(kasal.reserve("Sipsayev Sipsagul"))



# 1
class Doktor:
    def __init__(self,name):
        self.name = name
        self.bemorlar = []
    def add_bemor(self,bemor_name):
        self.bemorlar.append(bemor_name)
    def show_bemor(self):
        return self.bemorlar
    def count_bemor(self):
        return len(self.bemorlar)
class Kasalxona:
    def __init__(self,name):
        self.name = name
        self.doktors = []
    def add_doctor(self,doctor_name):
        self.doktors.append(doctor_name)
    def show_doctors(self):
        for nomeri , doctor_ismi in enumerate(self.doktors):
            print(f"{nomeri+1}.{doctor_ismi.name} Navbat soni: {doctor_ismi.count_bemor()}")
class Bemor:
    def __init__(self,name):
        self.name = name
    def choose_doctor(self,doctor_name):
        doctor_name.add_bemor(self.name)
        print(f"{self.name} {doctor_name.name}'ga navbatga yozildingiz")
        print("Navbatdagi bemorlar:" , doctor_name.show_bemor())
        print("Jami bemorlar soni: " , doctor_name.count_bemor())
shifoxona = Kasalxona("1-son Markaziy Poliklinika")
dok1 = Doktor("Dr.Vali")
dok2 = Doktor("Dr.Ali")
shifoxona.add_doctor(dok1)
shifoxona.add_doctor(dok2)

bemor1 = Bemor("Valijon")
bemor2 = Bemor("Ulug'bek")
bemor3 = Bemor("Yoqubboy")

bemor1.choose_doctor(dok1)
bemor2.choose_doctor(dok2)
bemor3.choose_doctor(dok1)

shifoxona.show_doctors()