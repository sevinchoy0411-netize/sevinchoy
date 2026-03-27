# class Maktab:
#     def __init__(self,maktab_nomi):
#         self.maktab = maktab_nomi
#         self.grades = []
#     def add_grade(self,sinf):
#         self.grades.append(sinf)
#     def get_grades(self):
#         data = "\n".join(self.grades)
#         return f"{self.maktab} maktabidagi sinflar: \n{data}"
# maktab6 = Maktab("6-son")
# maktab6.add_grade("6-b")
# maktab6.add_grade("7-b")
# maktab6.add_grade("8-b")
# maktab6.add_grade("9-b")
# print(maktab6.get_grades())


# class Avto:
#     def __init__(self,yili,model,rangi,yurgani):
#         self.yil = yili
#         self.model = model
#         self.rang = rangi
#         self.yurgani = yurgani
#     def get_info(self):
#         return f"Mashina modeli: {self.model}\nMashina ishlab chiqarilgan yili: {self.yil}\nMashina yurgan masofasi: {self.yurgani}\nMashina rangi: {self.rang}"
#     def get_year(self,joriy_yil):
#         return f"Avtomobil ishlab chiqarilganiga {joriy_yil - self.yil} yil bo'lgan"
#     def get_price(self,price,joriy_yil):
#         if joriy_yil-self.yil > 5:
#             price -= 10000
#         else:
#             price -= 5000
#         return f"Mashina narxi hozirda: {price}"
#     def check_colour(self,foiz,narx,joriy_yil):
#         foiz * 2
#         narx_u = narx * foiz / 100
#         if joriy_yil-self.yil > 5:
#             narx_u -= 10000
#         else:
#             narx_u -= 5000
#         return f"Mashina narxi hozirda: {narx_u}"
# avto1 = Avto(2023,"tracker 2","qora","3000")
# print(avto1.get_price(22000,2026))


# class Avto:
#     def __init__(self,yili,model,rangi,yurgani):
#         self.yil = yili
#         self.model = model
#         self.rang = rangi
#         self.yurgani = yurgani
#     def check_colour(self,foiz,narx,joriy_yil):
#         foiz2 = foiz * 2
#         foiz_u = narx * foiz2 / 100
#         if joriy_yil-self.yil > 5:
#             narx_y = 10000
#         else:
#             narx_y = 5000
#         narx_q = narx_y + foiz_u
#         narx_u = narx - narx_q
#         return f"Mashina narxi hozirda: {narx_u}"
# avto1 = Avto(2023,"tracker 2","qora","3000")
# print(avto1.check_colour(5,35000,2026))


# class Mashina:
#     def __init__(self,madel,year,price):
#         self.name = madel
#         self.year = year
#         self.price = price
#     def get_info(self):
#         return f"Mashina modeli: {self.name}\nMashina ishlab chiqarilgan yili: {self.year}\nMashina narxi: {self.price}"
#     def get_price(self,current_year,percentage_of_color):
#         count_year = current_year - self.year
#         if count_year >= 5:
#             self.price -= 10000
#         else:
#             self.price -= 5000
#         if percentage_of_color != 0:
#             self.price = self.price - self.price*percentage_of_color*2/100
#         else:
#             self.price
#         return f"{self.name}'ning yili va kraska holatidan kelib chiqib hisoblangan narxi: {self.price}"
# avto1 = Mashina("Kia K5",2023,40000)
# print(avto1.get_price(2026,10))