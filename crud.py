# class Maktab:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.grades = []
#     def add_grade(self, sinf):
#         self.grades.append(sinf)
#     def show_grades(self):
#         grades = "\n".join(self.grades)
#         return f"{self.nomi} maktabidagi sinflar:\n{grades}"
#     def update_grades(self, sinf, sinff):
#         if sinf in self.grades:
#             index = self.grades.index(sinf)
#             self.grades[index] = sinff
#     def delete_grades(self, sinf):
#         if sinf in self.grades:
#             self.grades.remove(sinf)
# mk = Maktab("6-son")
# mk.add_grade("5-A")
# mk.add_grade("6-B")
# mk.add_grade("7-D")
# mk.add_grade("8-B")
# mk.update_grades("8-B", "8-A")
# mk.delete_grades("5-A")
# print(mk.show_grades())


# class Talaba:
#     def __init__(self,talaba_id,talaba_name,talaba_yosh):
#         self.talaba_id = talaba_id
#         self.talaba_name = talaba_name
#         self.talaba_age = talaba_yosh
#     def info(self):
#         return f"Talaba ID: {self.talaba_id}\nTalaba ismi: {self.talaba_name}\nTalaba yoshi: {self.talaba_age}"
# class TalabaCrud:
#     def __init__(self,name):
#         self.name = name
#         self.talabalar = []
#     def create_student(self,talaba_id,talaba_name,talaba_yosh):
#         talaba = Talaba(talaba_id,talaba_name,talaba_yosh)
#         self.talabalar.append(talaba)
#         print("Talaba muvaffaqiyatli qo'shildi👌")
#     def update_student(self,talaba_id, new_name = None, new_age = None):
#         for talaba in self.talabalar:
#             if talaba.talaba_id == talaba_id:
#                 if new_name:
#                     talaba.talaba_name = new_name
#                 if new_age:
#                     talaba.talaba_age = new_age
#                 return
#             print("Talaba muvaffaqiyatli yangilandi🔄️")
#     def delete_student(self,talaba_id):
#         for talaba in self.talabalar:
#             if talaba.talaba_id == talaba_id:
#                 self.talabalar.remove(talaba)
#                 print("Talaba muvaffaqiyatli o'chirildi😥")
#                 return 
#     def read_student(self):
#         for talaba in self.talabalar:
#             print(talaba.info())

# univer = TalabaCrud("TATU")
# univer.create_student(1,"Nizomjon",15)
# univer.create_student(2,"Madatdek",15)
# univer.update_student(1,"Nizomaddin",20)
# univer.delete_student(1)
# univer.read_student()


# class Kitob:
#     def __init__(self,kitob_id,kitob_name):
#         self.kitob_id = kitob_id
#         self.kitob_name = kitob_name
#     def kitob_info(self):
#         return f"Kitob ID'si: {self.kitob_id}\nKitob_nomi: {self.kitob_name}"
# class Kutubxona:
#     def __init__(self,name):
#         self.name = name
#         self.kitoblar = []
#     def creat_kitob(self,kitob_id,kitob_name):
#         kitob = Kitob(kitob_id,kitob_name)
#         self.kitoblar.append(kitob)
#         print("Kitob muvaffaqiyatli qo'shildi👌")
#     def update_kitob(self,kitob_id,new_name):
#         for kitob in self.kitoblar:
#             if kitob.kitob_id == kitob_id:
#                 if new_name:
#                     kitob.kitob_name = new_name
#                     return
#             print("Kitob muvaffaqiyatli yangilandi🔄️")
#     def delete_kitob(self,kitob_id):
#         for kitob in self.kitoblar:
#             if kitob.kitob_id == kitob_id:
#                 self.kitoblar.remove(kitob)
#                 print("Talaba muvaffaqiyatli o'chirildi😥")
#                 return 
#     def read_kitob(self):
#         for kitob in self.kitoblar:
#             print(kitob.kitob_info())

# kutubxona = Kutubxona("Alisher Navoiy")
# kutubxona.creat_kitob(1,"Ufq")
# kutubxona.creat_kitob(2,"Molxona")
# kutubxona.creat_kitob(3,"1984")
# kutubxona.creat_kitob(4,"Propaganda")
# kutubxona.update_kitob(1,"Qizil ajdarho")
# kutubxona.delete_kitob(4)
# kutubxona.read_kitob()


