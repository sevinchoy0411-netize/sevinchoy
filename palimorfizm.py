# class Avto:
#     def info(self):
#         print("avto")
# class Tesla(Avto):
#     def info(self):
#         print("Elektra carlar oilasi")
# class Malibu(Avto):
#     def info(self):
#         print("Benzinda yuruvchi carlar oilasi")
# avtolar = [Tesla(),Malibu()]
# for avto in avtolar:
#     avto.info()


# 1
# class Hayvon:
#     def ovoz(self):
#         return "hayvonlarning ovozi"
# class Mushuk(Hayvon):
#     def ovoz(self):
#         return "Miyov-miyov"
# class Kuchuk(Hayvon):
#     def ovoz(self):
#         return "Vov-vov"
# hayvonlar = [Mushuk(),Kuchuk()]
# for hayvon in hayvonlar:
#     print(hayvon.ovoz())


# 2
# class Transport:
#     def tezlik(self):
#         return "Mashina tezligi"
# class Avto(Transport):
#     def __init__(self,tezlik):
#         self._tezlik = tezlik
#     def tezlik(self):
#         return f"Mashina tezligi: {self._tezlik}"
# class Velosiped(Transport):
#     def __init__(self,tezlik):
#         self._tezlik = tezlik
#     def tezlik(self):
#         return f"Velosiped tezligi: {self._tezlik}"
# transportlar = [Avto("60km\h"),Velosiped("3km\h")]
# for i in transportlar:
#     print(i.tezlik())


# 3
# class Meva:
#     def rang(self):
#         return "Meva rangi"
# class Olma(Meva):
#     def __init__(self,rangi):
#         self.rangi = rangi
#     def rang(self):
#         return f"Meva rangi: {self.rangi}"
# class Banan(Meva):
#     def __init__(self,rangi):
#         self.rangi = rangi
#     def rang(self):
#         return f"Meva rangi: {self.rangi}"
# mevalar = [Olma("qizil"),Banan("sariq")]
# for meva in mevalar:
#     print(meva.rang())


# 4
# class Xodim:
#     def ish_haqi(self):
#         return "Xodimlar ish haqi"
# class Direktor(Xodim):
#     def __init__(self,oylik):
#         self.oylik = oylik
#     def ish_haqi(self):
#         return f"Direktorning ish haqi: {self.oylik} so'm"
# class Oqituvchi(Xodim):
#     def __init__(self,dars):
#         self.dars = dars
#     def ish_haqi(self):
#         return f"O'qituvchining oyliki: {self.dars*200000} so'm"
# oylik = [Direktor(9000000),Oqituvchi(27)]
# for i in oylik:
#     print(i.ish_haqi())


# 5
# class Qurilma:
#     def ishlab_chiqaruvchi(self):
#         return "Ishlab chiqaruvchilar"
# class Kompyuter(Qurilma):
#     def __init__(self,kompaniya):
#         self.kompaniya = kompaniya
#     def ishlab_chiqaruvchi(self):
#         return f"Kompyuter ishlab chiqaruvchi kompaniya: {self.kompaniya}"
# class Telefon(Qurilma):
#     def __init__(self,brend):
#         self.brend = brend
#     def ishlab_chiqaruvchi(self):
#         return f"Telefonni ishlab chiqargan brend: {self.brend}"
# qurilmalar = [Kompyuter("hp"),Telefon("iPhone")]
# for i in qurilmalar:
#     print(i.ishlab_chiqaruvchi())