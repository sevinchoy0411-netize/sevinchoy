# class Word:
#     def __init__(self,fayl):
#         self.fayl = fayl
#     def asosiyga_kirish(self):
#         return "Siz asosiy bo'limidasiz"
#     def joylashga_kirish(self):
#         return "Siz joylash bo'limidasiz"
#     def dizaynga_kirish(self):
#         return "Siz dizayn bo'limidasiz"
#     def get_file(self):
#         return f"Fayl nomi: {self.fayl}"
# fayl1 = Word("Meros")
# print(fayl1.get_file())

# class Talaba:
#     def __init__(self,ism,yosh,yonalish):
#         self.ism = ism
#         self.yosh = yosh
#         self.megor = yonalish
#     def malumot_ber(self):
#         return f"Talaba ismi: {self.ism}\nTalaba yoshi: {self.yosh}\nTalabaning yo'nalishi: {self.megor}"
# talaba1 = Talaba("valijon",2007,"Dasturiy injenering")
# print(talaba1.malumot_ber())

# class Talaba:
#     def __init__(self,ismi,yili,universiteti,yonalishi):
#         self.ism = ismi
#         self.yili = yili
#         self.universitet = universiteti
#         self.megor = yonalishi
#     def get_name(self):
#         return f"Talaba ismi: {self.ism}"
#     def get_age(self):
#         return f"Talaba yoshi: {2025-self.yili}"
#     def get_university(self):
#         return f"Talaba {self.universitet} da o'qiydi"
#     def get_faculty(self):
#         return f"Talaba {self.universitet} universitetining {self.megor} yo'nalishida o'qiydi"
#     def get_info(self):
#         return f"Talabaning ismi {self.ism}\nTalabaning yili: {self.yili}\nTalaba o'qiydigan universitet: {self.universitet}\nTalabaning yonalishi: {self.megor}"
# talaba1 = Talaba("Ulug'bek",2007,"Al-Xorazmiy","sun'iy intelekt")
# print(talaba1.get_info())

# 1
# class Student:
#     def __init__(self,ism,yosh,baho):
#         self.name = ism
#         self.age = yosh
#         self.grade = baho
#     def info(self):
#         return f"Studentning ismi: {self.name}\nTalabaning  yoshi: {self.age}\nTalabaning bahosi: {self.grade}"
# student1 = Student("Ulug'bek",20,5)
# print(student1.info())

# 2
# class Avto:
#     def __init__(self,model,yil,rang):
#         self.rusum = model
#         self.yili = yil
#         self.rangi = rang
#     def car(self):
#         return f"Mashinaning modeli: {self.rusum}\nMashinaning yili: {self.yili}\nMashinaning rangi: {self.rangi}"
# mashina = Avto("Tracker2",2025,"Qora")
# print(mashina.car())

# 3
# class Bankhisob:
#     def __init__(self,balans):
#         self.hisob = balans
#     def add_money(self,miqdor):
#         return f"Balansingiz {self.hisob} edi {self.hisob+miqdor} bo'ldi"
#     def yechish(self,summa):
#         return f"balansingizda {self.hisob} pul bor edi {self.hisob-summa} qoldi"
# user1 = Bankhisob(5000000)
# print(user1.add_money(500000))

# 4
class Dokon:
    def __init__(self,dokon_nomi):
        self.dokon = dokon_nomi
        self.mahsulot = []
        self.soni = 0
    def add_product(self,mahsulot_nomi):
        self.mahsulot.append(mahsulot_nomi)
        self.soni += 1
    def remove_product(self,mahsulot_name):
        self.mahsulot.remove(mahsulot_name)
        self.soni -= 1
    def get_info(self):
        matn = "\n".join([name for name in self.mahsulot])
        return f"{self.dokon} dokonida {self.soni}ta mahsulot bor va ular:\n{matn}"
    