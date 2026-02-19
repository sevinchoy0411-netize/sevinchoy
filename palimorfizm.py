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


# 6
# class Hayvon:
#     def harakat(self):
#         return "Hayvonclar harakati"
# class Qush(Hayvon):
#     def harakat(self):
#         return "Qush uchyabdi"
# class Baliq(Hayvon):
#     def harakat(self):
#         return "Baliq suzmoqda"
# hayvonlar = [Qush(),Baliq()]
# for hayvon in hayvonlar:
#     print(hayvon.harakat())


# 7
# class Avto:
#     def narxi(self):
#         return "Mashina narxlari"
# class Malibu(Avto):
#     def __init__(self,price):
#         self.price = price
#     def narxi(self):
#         return f"Malibu narxi: {self.price}$"
# class Cobalt(Avto):
#     def __init__(self,price):
#         self.price = price
#     def narxi(self):
#         return f"Cobalt narxi: {self.price}$"
# class Nexia(Avto):
#     def __init__(self,narx):
#         self.price = narx
#     def narxi(self):
#         return f"Nexia narxi: {self.price}$"
# avtolar = [Malibu(25000),Cobalt(14500),Nexia(10000)]
# for i in avtolar:
#     print(i.narxi())


# 8
# class Asbob:
#     def ovoz_chiqar(self):
#         return "Musiqa asboblari ovozi"
# class Gitara(Asbob):
#     def ovoz_chiqar(self):
#         return "Ting-ting"
# class Baraban(Asbob):
#     def ovoz_chiqar(self):
#         return "Tum-tum"
# asboblar = [Gitara(),Baraban()]
# for ovoz in asboblar:
#     print(ovoz.ovoz_chiqar())


# 9
# class Oyinchi:
#     def sport_turi(self):
#         return "Sportchilarning sport turlari"
# class Futbolchi(Oyinchi):
#     def sport_turi(self):
#         return "Sport turi: futbol"
# class Basketbolchi(Oyinchi):
#     def sport_turi(self):
#         return "Sport turi: basketbol"
# sport = [Futbolchi(),Basketbolchi()]
# for sports in sport:
#     print(sports.sport_turi())


# 10
# class Raqam:
#     def aniqlik(self):
#         return "Raqamlar"
# class Juftson(Raqam):
#     def aniqlik(self):
#         for i in range(1,10):
#             if i%2==0:
#                 print(i)
# class Toqson(Raqam):
#     def aniqlik(self):
#         for i in range(1,10):
#             if i%2!=0:
#                 print(i)
# sonlar = [Juftson(),Toqson()]
# for son in sonlar:
#     print(son.aniqlik())