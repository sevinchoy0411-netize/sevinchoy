# class Mahsulot:
#     def __init__(self,mahsulot_nomi,mahsulot_narxi,mahsulot_turi):
#         self.name = mahsulot_nomi
#         self.price = mahsulot_narxi
#         self.type = mahsulot_turi
#     def get_info(self):
#         return f"Mahsulot nomi: {self.name}\nMahsulot narxi: {self.price}\nMahsulot turi: {self.type}"

# class Sut_Mahsulotlari(Mahsulot):
#     def __init__(self, mahsulot_nomi, mahsulot_narxi, mahsulot_turi,litr):
#         super().__init__(mahsulot_nomi, mahsulot_narxi, mahsulot_turi)
#         self.litr = litr
#     def get_info_sut(self):
#         return f"{self.get_info()}'dan do'konda {self.litr} litr bor"

# class Shakar(Mahsulot):
#     def __init__(self, mahsulot_nomi, mahsulot_narxi, mahsulot_turi,kg):
#         super().__init__(mahsulot_nomi, mahsulot_narxi, mahsulot_turi)
#         self.kg = kg
#     def get_data(self):
#         return f"{self.get_info()}'dan {self.kg} kg bor"
    
# halimaxon = Sut_Mahsulotlari("Sut",10000,"Sut mahsulotlari",25)
# ozoda = Shakar("Shakar",20000,"Qandolatchilik mahsulotlari",100)
# print(halimaxon.get_info_sut())
# print(ozoda.get_data())


# 1
# class Avto:
#     def __init__(self,madel,yil,rang,dvigatel,yoqilgi,uzatma):
#         self.madel = madel
#         self.yil = yil
#         self.rang = rang
#         self.dvigatel = dvigatel
#         self.yoqilgi = yoqilgi
#         self.uzatma = uzatma
#     def harakatlan(self):
#         return f"{self.madel} mashinasi haqida ma'lumotlar"
# class Mersedes(Avto):
#     def __init__(self, madel, yil, rang, dvigatel,yoqilgi,uzatma,class_turi,salon,amg):
#         super().__init__(madel, yil, rang, dvigatel,yoqilgi,uzatma)
#         self.class_turi = class_turi
#         self.salon = salon
#         self.amg = amg
#     def sport_rejimi(self):
#         if self.amg:
#             return "AMG Turbo rejimi yoqildi"
#         else:
#             return "Bu Mers AMG emas"
# class Damas(Avto):
#     def __init__(self, nomi, yili, probeg, rangi, narxi,van,labo,style):
#         super().__init__(nomi, yili, probeg, rangi, narxi)
#         self.van = van
#         self.labo = labo
#         self.style = style
#         if self.style:
#             return "bu odatiy damas"
#         elif self.labo:
#             return "Labo shaklidagi damas"
#         else:
#             return "Van shaklidagi damas"


# 2
# class  Ota:
#     def __init__(self,ism,yosh):
#         self.name = ism
#         self.year = yosh
#     def get_info(self):
#         return f"Ismi: {self.name}\nYoshi: {self.year}"
# class Bola(Ota):
#     def __init__(self, ism, yosh,maktab_nomi):
#         super().__init__(ism, yosh)
#         self.school = maktab_nomi
#     def get_data(self):
#         return f"{self.get_info()}\nMaktab nomi: {self.school}"
# bola = Bola("Zoxira",15,"9-maktab")


# 3
# class Hayvon:
#     def __init__(self,nomi,jinsi,rangi):
#         self.nomi = nomi
#         self.jinsi = jinsi
#         self.rangi = rangi
#     def get_info(self):
#         return f"Nomi: {self.nomi}\nJinsi: {self.jinsi}\nRangi: {self.rangi}"
# class It(Hayvon):
#     def __init__(self, nomi, jinsi, rangi,turi,urug):
#         super().__init__(nomi, jinsi, rangi)
#         self.turi = turi
#         self.urug = urug
#     def get_data(self):
#         return f"{self.get_info()}\nTuri: {self.turi}\nUrug'i: {self}"
# class Mushuk(Hayvon):
#     def __init__(self, nomi, jinsi, rangi, turi):
#         super().__init__(nomi, jinsi, rangi)
#         self.turi = turi
#     def get_data(self):
#         return f"Turi: {self.turi}"


# 4
# class Avto:
#     def __init__(self,madel,yil,rang,dvigatel,yoqilgi,uzatma):
#         self.madel = madel
#         self.yil = yil
#         self.rang = rang
#         self.dvigatel = dvigatel
#         self.yoqilgi = yoqilgi
#         self.uzatma =uzatma
#     def get_info(self):
#         return f"{self.madel} mashinasi haqida ma'lumotlar:\n"
# class Avtomobil(Avto):
#     def __init__(self, madel, yil, rang, dvigatel, yoqilgi, uzatma):
#         super().__init__(madel, yil, rang, dvigatel, yoqilgi, uzatma)
#     def get_info(self):
#         return f"{self.get_info()}Yili: {self.yil}\nRang: {self.rang}\nDvigatel: {self.dvigatel}\nYoqilgi: {self.yoqilgi}\nUzatma: {self.uzatma}"


# 5
class Talaba:
    def __init__(self,yoshi,ismi):
        self.yoshi = yoshi
        self.ismi = ismi
    def get_info(self):
        return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
class Bakalavr(Talaba):
    def __init__(self, yoshi, ismi,maktab_baholari):
        super().__init__(yoshi, ismi)
        self.baho = maktab_baholari
    def get_data(self):
        return f"{self.get_info()}\nMaktab baholari: {self.baho}"
class Magistr(Talaba):
    def __init__(self, yoshi, ismi,bakalavr_bahosi):
        super().__init__(yoshi, ismi)
        self.bakalavr = bakalavr_bahosi
    def get_data(self):
        return f"{self.get_info()}"