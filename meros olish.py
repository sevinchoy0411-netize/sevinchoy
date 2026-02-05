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
#     def damas_turi(self):
#         if self.style:
#             return "bu odatiy damas"
#         elif self.labo:
#             return "Labo shaklidagi damas"
#         else:
#             return "Van shaklidagi damas"
# mers = Mersedes("G60",2023,"qora","M117","benzin","4pog'onali avtomat","G","charm","True")
# print(mers.sport_rejimi())
# damas = Damas("damas",2023,5000,"oq","93 156 000",True,False,False)
# print(damas.damas_turi())


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
# bola = Bola("Zoxira",15,"17-maktab")


# 3
# class Hayvon:
#     def __init__(self,nomi,jinsi,rangi):
#         self.nomi = nomi
#         self.jinsi = jinsi
#         self.rangi = rangi
#     def get_info(self):
#         return f"Nomi: {self.nomi}\nJinsi: {self.jinsi}\nRangi: {self.rangi}"
# class It(Hayvon):
#     def __init__(self, nomi, jinsi, rangi,urug):
#         super().__init__(nomi, jinsi, rangi)
#         self.urug = urug
#     def get_data(self):
#         return f"{self.get_info()}\nUrug'i: {self.urug}"
# class Mushuk(Hayvon):
#     def __init__(self, nomi, jinsi, rangi, turi):
#         super().__init__(nomi, jinsi, rangi)
#         self.turi = turi
#     def get_data(self):
#         return f"{self.get_info()}Turi: {self.turi}"
# it = It("simba","erkak","oq","ovchi")
# print(it.get_data())
# mushuk = Mushuk("Beyaz","ayol","oq","honaki")
# print(mushuk.get_data())


# 4
# class Avto:
#     def __init__(self,madel,yil,rang,dvigatel,yoqilgi,uzatma):
#         self.madel = madel
#         self.yil = yil
#         self.rang = rang
#         self.dvigatel = dvigatel
#         self.yoqilgi = yoqilgi
#         self.uzatma =uzatma
#     def get_data(self):
#         return f"{self.madel} mashinasi haqida ma'lumotlar:\n"
# class Avtomobil(Avto):
#     def __init__(self, madel, yil, rang, dvigatel, yoqilgi, uzatma):
#         super().__init__(madel, yil, rang, dvigatel, yoqilgi, uzatma)
#     def get_info(self):
#         return f"{self.get_data()}Yili: {self.yil}\nRang: {self.rang}\nDvigatel: {self.dvigatel}\nYoqilgi: {self.yoqilgi}\nUzatma: {self.uzatma}"
# avto = Avtomobil("G60",2023,"qora","M117","benzin","4pog'onali avtomat")
# print(avto.get_info())


# 5
# class Talaba:
#     def __init__(self,yoshi,ismi):
#         self.yoshi = yoshi
#         self.ismi = ismi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
# class Bakalavr(Talaba):
#     def __init__(self, yoshi, ismi,maktab_baholari):
#         super().__init__(yoshi, ismi)
#         self.baho = maktab_baholari
#     def get_data(self):
#         return f"{self.get_info()}\nMaktab baholari: {self.baho}"
# class Magistr(Talaba):
#     def __init__(self, yoshi, ismi,bakalavr_bahosi):
#         super().__init__(yoshi, ismi)
#         self.bakalavr = bakalavr_bahosi
#     def get_data(self):
#         return f"{self.get_info()}\nBakalavr bahosi: {self.bakalavr}"
# bakalavr = Bakalavr(17,"sevinchoy","4")
# print(bakalavr.get_data())
# magistr = Magistr(21,"sevinchoy","5")
# print(magistr.get_data())


# 6
# class Ustoz:
#     def __init__(self,ismi,yoshi,fani):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.fan = fani
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nDars beradigan fani: {self.fan}"
# class InformatikaUstozi(Ustoz):
#     def __init__(self, ismi, yoshi, fani, dasturlash_tili,project):
#         super().__init__(ismi, yoshi, fani)
#         self.til = dasturlash_tili
#         self.project = project
#     def get_data(self):
#         return f"{self.get_info()}\nBiladigan dasturlsh tillari: {self.til}\nIshtirok etgan va amalga oshirgan loyihalari: {self.project}"
# ustoz = InformatikaUstozi("Mirzabek",23,"Dasturlash","Python,django,php,html,css,javascript","50+")
# print(ustoz.get_data())


# 7
# class Tech:
#     def __init__(self,model,rangi):
#         self.model = model
#         self.rang = rangi
#     def get_tech(self):
#         return f"Modeli: {self.model}\nRangi: {self.rang}"
# class Kompyuter(Tech):
#     def __init__(self, model, rangi,xotirasi,ram):
#         super().__init__(model, rangi)
#         self.memory = xotirasi
#         self.ram = ram
#     def kompyuter_data(self):
#         return f"{self.get_tech()}\nXotirasi: {self.memory}\nRAMi: {self.ram}"
# kompyuter = Kompyuter("hp intel core i5","oq","512","16")
# print(kompyuter.kompyuter_data())


# 8
# class Kompyuter:
#     def init(self, nomi, ekran ):
#         self.name = nomi
#         self.screen = ekran
#     def info(self):
#         return f"Kompyuter nomi {self.name}\nKompyuter ekrani o'lchami:{self.screen}"
# class Noutbook(Kompyuter):
#     def init(self, nomi, ekran, shlef, touchbat, akkumlyator):
#         super().init(nomi, ekran)
#         self.shelf = shlef
#         self.touchbat = touchbat
#         self.batareya = akkumlyator
#     def get_info(self):
#         return f"{self.info()}\nNoutbook ochilish gradusi {self.shlef}\nTouchbat borligi :{self.touch}\nZaryadkasi :{self.batareya}"
# hp = Noutbook("Hp Envy" , "15.6 dyumm" , "180^gradus" , "Bor" , "aktiv holatda 5 soatga yetadi")
# print(hp.get_info())


# 9
# class Shaxs:
#     def __init__(self,ismi,yoshi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#     def shaxs_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, yoshi,fani):
#         super().__init__(ismi, yoshi)
#         self.fan = fani
#     def get_teacher(self):
#         return f"{self.shaxs_info()}\nDars beradigan fani: {self.fan}"
# oqituvchi = Oqituvchi("Mirzabek","23","IT")
# print(oqituvchi.get_teacher())


# 10
# class Mashina:
#     def __init__(self,yoqilgi,dvigatel):
#         self.yoqilgi = yoqilgi
#         self.dvigatel = dvigatel
#     def get_car(self):
#         return f"Dvigateli: {self.dvigatel}\nYoqilgisi: {self.yoqilgi}"
# class YukMashina(Mashina):
#     def __init__(self,yoqilgi, dvigatel,tonna):
#         super().__init__(yoqilgi, dvigatel)
#         self.tonna = tonna
#     def yukmashina_info(self):
#         return f"{self.get_car()}\nTonna: {self.tonna}"
# mashina = YukMashina("dizel","MAZ 500","5tonna")
# print(mashina.yukmashina_info())


# 11
# class Uchuvchi:
#     def __init__(self,tajribasi,parvozlar_soni):
#         self.tajriba = tajribasi
#         self.soni = parvozlar_soni
#     def pilot_info(self):
#         return f"Tajribasi: {self.tajriba}\nParvozlar soni: {self.soni}"
# class HarbiyUchuvchi(Uchuvchi):
#     def __init__(self, tajribasi, parvozlar_soni,lavozimi):
#         super().__init__(tajribasi, parvozlar_soni)
#         self.lavozimi = lavozimi
#     def data_pilot(self):
#         return f"{self.pilot_info()}\nLavozimi: {self.lavozimi}"
# uchuvchi = HarbiyUchuvchi("5yil","150ta",'serjant')
# print(uchuvchi.data_pilot())


# 12
# class Kitob:
#     def __init__(self,varaq,nomi):
#         self.varaq = varaq
#         self.nomi = nomi
#     def get_book(self):
#         return f"Janri: {self.nomi}\nVaraqlar soni: {self.varaq}"
# class Darslik(Kitob):
#     def __init__(self, varaq, nomi,fani):
#         super().__init__(varaq, nomi)
#         self.fani = fani
#     def darslik_info(self):
#         return f"{self.get_book()}\nFani: {self.fani}"
# darslik = Darslik("150","Adabiyot","fani")
# print(darslik.darslik_info())


# 13
# class Hayvon:
#     def __init__(self,ismi,turi,jinsi):
#         self.ismi = ismi
#         self.turi = turi
#         self.jinsi = jinsi
#     def ovoz(self):
#         if self.turi == "xo'roz":
#             return "qu-qu-ri-qu"
#         if self.turi == "o'rdak":
#             return "g'aq-g'aq"
# class It(Hayvon):
#     def __init__(self, ismi, turi, jinsi):
#         super().__init__(ismi, turi, jinsi)
#     def ovoz(self):
#         return "vov-vov"
# class Mushuk(Hayvon):
#     def __init__(self, ismi, turi, jinsi):
#         super().__init__(ismi, turi, jinsi)
#     def ovoz(self):
#         return "miyov-miyov"
# it = It("simba","it","erkak")
# print(it.ovoz())
# mushuk = Mushuk("Zeytin","mushuk","erkak")
# print(mushuk.ovoz())


# 14
# class Qurilma:
#     def __init__(self,nomi,kompaniya):
#         self.nomi = nomi
#         self.kompaniya = kompaniya
#     def get_qurilma(self):
#         return f"Qurilma nomi: {self.nomi}\nIshlab chiqargan kompaniyasi: {self.kompaniya}"
# class Telefon(Qurilma):
#     def __init__(self, nomi, kompaniya,xotira):
#         super().__init__(nomi, kompaniya)
#         self.xotira = xotira
#     def get_phone(self):
#         return f"{self.get_qurilma()}\nXotirasi: {self.xotira}"
# class Noutbuk(Qurilma):
#     def __init__(self, nomi, kompaniya,ddr,xotira,ram):
#         super().__init__(nomi, kompaniya)
#         self.ddr = ddr
#         self.xotira = xotira
#         self.ram = ram
#     def get_noutbook(self):
#         return f"{self.get_qurilma()}\nXotirasi: {self.xotira}\nDDR'i: {self.ddr}\nRAM'i: {self.ram}"
# telefon = Telefon("Galaxy A23","Samsung","64")
# print(telefon.get_phone())
# noutbuk = Noutbuk("hp intel core i5","hp",5,"SSD","16")
# print(noutbuk.get_noutbook())


# 15
# class Kompaniya:
#     def __init__(self,kompaniya_nomi,vazifasi):
#         self.nomi = kompaniya_nomi
#         self.vazifa = vazifasi
#     def get_company(self):
#         return f"Kompaniya nomi: {self.nomi}\nIshlab chiqaradigan mahsuloti: {self.vazifa}"
# class Ishchi(Kompaniya):
#     def __init__(self, kompaniya_nomi, vazifasi, lavozimi):
#         super().__init__(kompaniya_nomi, vazifasi)
#         self.lavozimi = lavozimi
#     def get_worker(self):
#         return f"{self.get_company()}\nLavozimi: {self.lavozimi}"
# ishchi = Ishchi("CyberNest","dasturchi","bosh dasturchi")
# print(ishchi.get_worker())


# 16
# class Shaxs:
#     def __init__(self,ismi,yoshi,sana):
#         self.ism = ismi
#         self.yoshi = yoshi
#         self.sana = sana
#     def about_shaxs(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yoshi}\nTug'ilgan sanasi: {self.sana}"
# class Oquvchi(Shaxs):
#     def __init__(self, ismi, yoshi, sana,maktab,sinf):
#         super().__init__(ismi, yoshi, sana)
#         self.maktab = maktab
#         self.sinf = sinf
#     def about_oquvchi(self):
#         return f"{self.about_shaxs()}\nMaktabi: {self.maktab}\nSinfi: {self.sinf}"
# oquvchi = Oquvchi("Sevinchoy",14,"4-yanvar","6-maktab","8-sinf")
# print(oquvchi.about_oquvchi())


# 17
# class Transport:
#     def __init__(self,nomi,sigimi):
#         self.nomi = nomi
#         self.sigimi = sigimi
#     def get_transport(self):
#         return f"Transport nomi: {self.nomi}\nTransport sig'imi: {self.sigimi}"
# class Avtobus(Transport):
#     def __init__(self, nomi, sigimi,orindiq_soni):
#         super().__init__(nomi, sigimi)
#         self.soni = orindiq_soni
#     def get_avtobus(self):
#         return f"{self.get_transport()}\nAvtobusdagi o'rindiqlar soni: {self.soni}"
# class Poyezd(Transport):
#     def __init__(self, nomi, sigimi,vagon_soni):
#         super().__init__(nomi, sigimi)
#         self.vagon = vagon_soni
#     def poyezd_info(self):
#         return f"{self.get_transport()}\nPoyezddagi vagonlar soni: {self.vagon}"
# # avtobus = Avtobus("avtobus","36","36")
# # print(avtobus.get_avtobus())
# poyezd = Poyezd("poyezd","38",10)
# print(poyezd.poyezd_info())


# 18
# class Shaxs:
#     def __init__(self,ismi,yoshi,birth_day):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.birthday = birth_day
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nTug'ilgan kuni: {self.birthday}"
# class Talaba(Shaxs):
#     def __init__(self, ismi, yoshi, birth_day,kurs):
#         super().__init__(ismi, yoshi, birth_day)
#         self.kurs = kurs
#     def get_data(self):
#         return f"{self.get_info()}\nO'qiyotgan kursi: {self.kurs}"
# talaba = Talaba("Sevinchoy",14,"4-yanvar","IT")
# print(talaba.get_data())


# 19
# class Mahsulot:
#     def __init__(self,nomi,turi,narxi):
#         self.nomi = nomi
#         self.turi = turi
#         self.narxi = narxi
#     def about_product(self):
#         return f"Mahsulot nomi: {self.nomi}\nMahsulot turi: {self.turi}\nMahsulot narxi: {self.narxi}"
# class Meva(Mahsulot):
#     def __init__(self, nomi, turi, narxi,kg):
#         super().__init__(nomi, turi, narxi)
#         self.kg = kg
#     def fruit_data(self):
#         return f"{self.about_product()}\nBundan {self.kg} bor"
# banan = Meva("banan","tropic","25000",35)
# print(banan.fruit_data())


# 20
# class Bino:
#     def __init__(self,qavat_soni,maydoni):
#         self.qavat = qavat_soni
#         self.maydon = maydoni
#     def get_building(self):
#         return f"Qavatlar soni: {self.qavat}\nMaydoni: {self.maydon}"
# class Uy(Bino):
#     def __init__(self, qavat_soni, maydoni, xona_soni):
#         super().__init__(qavat_soni, maydoni)
#         self.xona = xona_soni
#     def uy_info(self):
#         return f"{self.get_building()}\nXonalar soni: {self.xona}"
# uy = Uy(4,"220",3)
# print(uy.uy_info())


# 21
# class Citizen:
#     def __init__(self,yashash_joyi,ismi,kasbi,ish_joyi):
#         self.manzil = yashash_joyi
#         self.ismi = ismi
#         self.kasb = kasbi
#         self.ishjoyi = ish_joyi
#     def get_citizen(self):
#         return f"Ismi: {self.ismi}\nYashash joyi: {self.manzil}\nKasbi: {self.kasb}\nIsh joyi: {self.ishjoyi}"
# class Person(Citizen):
#     def __init__(self, yashash_joyi, ismi, kasbi, ish_joyi,tel):
#         super().__init__(yashash_joyi, ismi, kasbi, ish_joyi)
#         self.telefon = tel
#     def get_person(self):
#         return f"{self.get_citizen()}\nTelefon raqami: {self.telefon}"
# person = Person("Yangi O'zbekiston","Sevinchoy","Dasturchi","Unicon Soft",991234567)
# print(person.get_person())


# 22
# class Kitob:
#     def __init__(self,nomi,varaq_soni,janr,narxi,muallifi):
#         self.varaq = varaq_soni
#         self.nomi = nomi
#         self.janri = janr
#         self.narxi = narxi
#         self.muallifi = muallifi
#     def about_book(self):
#         return f"Kitob nomi: {self.nomi}\nMuallifi: {self.muallifi}\nJanri: {self.janri}\nVaraqlar soni: {self.varaq}\nNarxi: {self.narxi}"
# class ElektronKitob(Kitob):
#     def __init__(self, nomi, varaq_soni, janr, narxi, muallifi,yuborilish_usuli):
#         super().__init__(nomi, varaq_soni, janr, narxi, muallifi)
#         self.usuli = yuborilish_usuli
#     def get_elektronkitob(self):
#         return f"{self.about_book()}\nijtimoiy tarmoqdan yuborilish usuli: {self.usuli}"
# ebook = ElektronKitob("Molxona",100,"satirik asar",35000,"Jorj Oruel","telegram")
# print(ebook.get_elektronkitob())


# 23
# class Mashina:
#     def __init__(self,model,rang,yil,probeg,dvigatel,uzatma,yoqilgi):
#         self.model = model
#         self.rangi = rang
#         self.yili = yil
#         self.probeg = probeg
#         self.dvigatel = dvigatel
#         self.uzatma = uzatma
#         self.yoqilgi = yoqilgi
#     def get_car(self):
#         return f"Mashina modeli: {self.model}\nRangi: {self.rangi}\nYili: {self.yili}\nYurgan masofasi: {self.probeg}\nDvigateli: {self.dvigatel}\nUzatma: {self.uzatma}\nYoqilgi turi: {self.yoqilgi}"
# class ElektroAvto(Mashina):
#     def __init__(self, model, rang, yil, probeg, dvigatel, uzatma, yoqilgi, vaqt):
#         super().__init__(model, rang, yil, probeg, dvigatel, uzatma, yoqilgi)
#         self.vaqt = vaqt
#     def get_avto(self):
#         return f"{self.get_car()}\nQuvvat olish muddati: {self.vaqt}"
# kia = ElektroAvto("Kia EV6","qora",2023,5000,"PMSM","yo'q","elektr","18-20daqiqa")
# print(kia.get_avto())


# 26
# class Avto:
#     def __init__(self,madel,yil,rang,dvigatel,yoqilgi,uzatma):
#         self.madel = madel
#         self.yil = yil
#         self.rang = rang
#         self.dvigatel = dvigatel
#         self.yoqilgi = yoqilgi
#         self.uzatma = uzatma
#     def harakatlan(self):
#         return f"Modeli: {self.madel}\nYili: {self.yil}\nRangi: {self.rang}\nDvigateli: {self.dvigatel}\nYoqilg'i turi: {self.yoqilgi}\nUzatmasi: {self.uzatma}"
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
# class Chevrolet(Avto):
#     def __init__(self, madel, yil, rang, dvigatel, yoqilgi, uzatma, salon):
#         super().__init__(madel, yil, rang, dvigatel, yoqilgi, uzatma)
#         self.salon = salon
#     def get_info(self):
#         return f"{self.harakatlan()}\nSaloni: {self.salon}"
# mers = Mersedes("g60",2023,"qora","M117","benzin","4pog'onali avtomat","G","charm",True)
# print(mers.sport_rejimi(),mers.harakatlan())
# malibu = Chevrolet("malibu2",2023,"qora","3.5L V6","benzin","4pog'onali avtomat","charm")
# print(malibu.get_info())


# 27
# class  Texnika:
#     def __init__(self,modeli,yili):
#         self.model = modeli
#         self.yili = yili
#     def get_info(self):
#         return f"Modeli: {self.model}\nYili: {self.yili}"
# class Printer(Texnika):
#     def __init__(self, modeli, yili,rangli,rangsiz):
#         super().__init__(modeli, yili)
#         self.rangli = rangli
#         self.rangsiz = rangsiz
#     def get_data(self):
#         if self.rangli:
#             return f"{self.get_info()}\nPrinter turi: rangli"
#         else:
#             return f"{self.get_info()}\nPrinter turi: rangsiz"
# class Skanner(Texnika):
#     def __init__(self, modeli, yili,shtrixkod,skanner):
#         super().__init__(modeli, yili)
#         self.shtrixkod = shtrixkod
#         self.skanner = skanner
#     def get_data(self):
#         if self.shtrixkod:
#             return f"{self.get_info()}\nTuri: shtrixkod"
#         else:
#             return f"{self.get_info()}\nTuri: QR code"
# printer = Printer("printer12",2023,True,False)
# print(printer.get_data())
# skanner = Skanner("Scan23",2024,False,True)
# print(skanner.get_data())


# 29
# class Sportchi:
#     def __init__(self,yoshi,ismi,sport_turi):
#         self.yoshi = yoshi
#         self.ismi = ismi
#         self.sport_turi = sport_turi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nShug'ullanuvchi sport turi: {self.sport_turi}"
# class Futbolchi(Sportchi):
#     def __init__(self, yoshi, ismi, sport_turi, guruh,vazifa):
#         super().__init__(yoshi, ismi, sport_turi)
#         self.guruh = guruh
#         self.vazifa = vazifa
#     def get_data(self):
#         return f"{self.get_info()}\nGuruhi: {self.guruh}\nGuruhdaki vazifasi: {self.vazifa}"
# futbolchi = Futbolchi(21,"Vali","futbol","O'zbekiston terma jamoasi","darvozabon")
# print(futbolchi.get_data())


# 30
# class Student:
#     def __init__(self,ismi,yoshi):
#         self.yoshi = yoshi
#         self.ismi = ismi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
# class Talaba(Student):
#     def __init__(self, ismi, yoshi, yonalishi, univeri):
#         super().__init__(ismi, yoshi)
#         self.yonalishi = yonalishi
#         self.univeri = univeri
#     def get_data(self):
#         return f"{self.get_info()}\nUniversiteti: {self.univeri}\nYo'nalishi: {self.yonalishi}"
# talaba = Talaba("Rayhona",21,"Dasturiy injenering","al-Xorazmiy")
# print(talaba.get_data())


# 31
# class Ota:
#     def __init__(self,ismi,yoshi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
# class Bola(Ota):
#     def __init__(self, ismi, yoshi, maktab):
#         super().__init__(ismi, yoshi)
#         self.maktab = maktab
#     def get_data(self):
#         return f"{self.get_info()}\nMaktabi: {self.maktab}"
# bola = Bola("Zuhra",10,"6-maktab")
# print(bola.get_data())


# 32
# class Ota:
#     def __init__(self,ismi,yoshi,tel_raqami):
#         self.ism = ismi
#         self.yoshi = yoshi
#         self.tel_raqam = tel_raqami
#     def get_info(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yoshi}\nTelefon raqami: {self.tel_raqam}"
# class Bola(Ota):
#     def __init__(self, ismi, yoshi, tel_raqami, maktab):
#         super().__init__(ismi, yoshi, tel_raqami)
#         self.maktab = maktab
#     def get_data(self):
#         return f"{self.get_info()}\nMaktabi: {self.maktab}"
# oquvchi = Bola("Zuhra",10,991234567,"6-maktab")
# print(oquvchi.get_data())


# 35
# class Hayvon:
#     def __init__(self,nomi,yoshi,jinsi):
#         self.ismi = nomi
#         self.yoshi = yoshi
#         self.jinsi = jinsi
#     def info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nJinsi: {self.jinsi}"
# class Mushuk(Hayvon):
#     def __init__(self, nomi, yoshi, jinsi,yovvoyi,honaki):
#         super().__init__(nomi, yoshi, jinsi)
#         self.yovvoyi = yovvoyi
#         self.honaki = honaki
#     def get_cat(self):
#         if self.yovvoyi:
#             return f"{self.info()}\nBu yovvoyi mushuk turi"
#         else:
#             return f"{self.info()}\nBu honaki mushuk"
# mushuk = Mushuk("Beyaz",2,"ayol",False,True)
# print(mushuk.get_cat())


# 36
# class Kompaniya:
#     def __init__(self,company_name):
#         self.name = company_name
#         self.workers = []
#         self.soni = 0
#     def add_worker(self,worker):
#         self.workers.append(worker)
#         self.soni += 1
#     def del_worker(self,worker):
#         self.workers.remove(worker)
#         self.soni -= 1
#     def show_data(self):
#         worker = "\n".join(self.workers)
#         return f"{self.name} kompaniyasida {self.soni}ta ishchi bor va ular: \n{worker}"
# class ITKompaniya(Kompaniya):
#     def __init__(self, company_name):
#         super().__init__(company_name)
#         self.loyihalar = 0
#     def add_project(self):
#         self.loyihalar += 1
#     def show_data(self):
#         return super().show_data()
#     def get_project(self):
#         return f"Loyihalar soni: {self.loyihalar}"
# cybernest = ITKompaniya("CyberNest")
# cybernest.add_worker("Maftuna")
# cybernest.add_worker("Zohira")
# cybernest.add_worker("Valijon")
# cybernest.add_worker("Sevinchoy")
# cybernest.add_project()
# cybernest.add_project()
# cybernest.add_project()
# cybernest.add_project()
# print(cybernest.show_data(),cybernest.get_project())


# 37
# class Mahsulot:
#     def __init__(self,nomi,turi,narx):
#         self.nomi = nomi
#         self.turi = turi
#         self.narx = narx
#     def get_info(self):
#         return f"Nomi: {self.nomi}\nTuri: {self.turi}\nNarxi: {self.narx}"
# class Ichimlik(Mahsulot):
#     def __init__(self, nomi, turi, narx, gazli, gazsiz):
#         super().__init__(nomi, turi, narx)
#         self.gazli = gazli
#         self.gazsiz = gazsiz
#     def get_data(self):
#         if self.gazli:
#             return f"{self.get_info()}\nIchimlik turi: gazli"
#         else:
#             return f"{self.get_info()}\nIchimlik turi: gazsiz"
# cola = Ichimlik("Cola", "ichimlik", "18000", True, False)
# print(cola.get_data())


# 38
# class Uskuna:
#     def __init__(self,nomi,modeli,narx,kompaniya):
#         self.turi = nomi
#         self.modeli = modeli
#         self.narx = narx
#         self.kompaniya = kompaniya
#     def get_data(self):
#         return f"Nomi: {self.turi}\nModeli: {self.modeli}\nKompaniyasi: {self.kompaniya}\nNarxi: {self.narx}"
# class Televizor(Uskuna):
#     def __init__(self, nomi, modeli, narx, kompaniya,kanal):
#         super().__init__(nomi, modeli, narx, kompaniya)
#         self.kanal = kanal
#     def get_info(self):
#         return f"{self.get_data()}\nKanallar soni: {self.kanal}"
# tv = Televizor("televizor","gdhxn234","3000000","Immer",43)
# print(tv.get_info())


# 39
# class Avto:
#     def __init__(self,yil,model,uzatma,yoqilgi):
#         self.yil = yil
#         self.model = model
#         self.uzatma = uzatma
#         self.yoqilgi = yoqilgi
#     def info(self):
#         return f"Modeli: {self.model}\nYili: {self.yili}\nYoqilg'i turi: {self.yoqilgi}\nUzatma: {self.uzatma}"
# class Elektromobil(Avto):
#     def __init__(self, yil, model, uzatma, yoqilgi,muddat):
#         super().__init__(yil, model, uzatma, yoqilgi)
#         self.muddat = muddat
#     def data(self):
#         return f"{self.info()}\nQuvvat olish muddati: {self.muddat}"


# 40
# class Shaxs:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def about_shaxs(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yosh}"
# class Talaba(Shaxs):
#     def __init__(self, ism, yosh,universitet,yonalish):
#         super().__init__(ism, yosh)
#         self.universitet = universitet
#         self.yonalish = yonalish
#     def about_talaba(self):
#         return f"{self.about_shaxs()}\nUniversitet: {self.universitet}\nYo'nalishi: {self.yonalish}"
# class Oqituvchi(Shaxs):
#     def __init__(self, ism, yosh,maktab,fan):
#         super().__init__(ism, yosh)
#         self.maktab = maktab
#         self.fan = fan
#     def get_teacher(self):
#         return f"{self.about_shaxs()}\nDars berish joyi: {self.maktab}\nFani: {self.fan()}"
