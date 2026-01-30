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
#         return f"{self.get_info()}\n Bakalavr bahosi: {self.bakalavr}"


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
#         return f"{self.get_info()}\nXotirasi: {self.memory}\nRAMi: {self.ram}"


# 9
# class Shaxs:
#     def __init__(self,ismi,yoshi,birth_day):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.birthday = birth_day
#     def shaxs_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nTug'ilgan kuni: {self.birthday}"
# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, yoshi, birth_day,fani):
#         super().__init__(ismi, yoshi, birth_day)
#         self.fan = fani
#     def get_teacher(self):
#         return f"{self.get_info()}\nDars beradigan fani: {self.fan}"


# 10
# class Mashina:
#     def __init__(self,model,rang,uzatma,yoqilgi,dvigatel,yil):
#         self.model = model
#         self.rang = rang
#         self.uzatma = uzatma
#         self.yoqilgi = yoqilgi
#         self.dvigatel = dvigatel
#         self.yil = yil
#     def get_car(self):
#         return f"Modeli: {self.model}\nRangi: {self.rang}\nYili: {self.yil}\nDvigateli: {self.dvigatel}\nYoqilgisi: {self.yoqilgi}\nUzatma: {self.uzatma}"
# class YukMashina(Mashina):
#     def __init__(self, model, rang, uzatma, yoqilgi, dvigatel, yil,tonna):
#         super().__init__(model, rang, uzatma, yoqilgi, dvigatel, yil,)
#         self.tonna = tonna
#     def yukmashina_info(self):
#         return f"{self.get_info()}\nTonna: {self.tonna}"


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
#         return f"{self.get_info()}\nLavozimi: {self.lavozimi}"


# 12
# class Kitob:
#     def __init__(self,varaq,janr):
#         self.varaq = varaq
#         self.janr = janr
#     def get_book(self):
#         return f"Janri: {self.janr}\nVaraqlar soni: {self.varaq}"
# class Darslik(Kitob):
#     def __init__(self, varaq, janr,fani):
#         super().__init__(varaq, janr)
#         self.fani = fani
#     def darslik_info(self):
#         return f"{self.get_info()}\nFani: {self.fani}"


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


# 14
# class Qurilma:
#     def __init__(self,nomi,kompaniya):
#         self.nomi = nomi
#         self.kompaniya = kompaniya
#     def get_qurilma(self):
#         return f"Qurilma nomi: {self.nomi}\nIshlab chiqargan kompaniyasi: {self.kompaniya}"
# class Telefon(Qurilma):
#     def __init__(self, nomi, kompaniya,rusumi,xotira):
#         super().__init__(nomi, kompaniya)
#         self.rusumi = rusumi
#         self.xotira = xotira
#     def get_phone(self):
#         return f"{self.get_info()}\nTelefon rusumi: {self.rusumi}\nXotirasi: {self.xotira}"
# class Noutbuk(Qurilma):
#     def __init__(self, nomi, kompaniya,ddr,xotira,ram):
#         super().__init__(nomi, kompaniya)
#         self.ddr = ddr
#         self.xotira = xotira
#         self.ram = ram
#     def get_noutbook(self):
#         return f"{self.get_info()}\nXotirasi: {self.xotira}\nDDr'i: {self.ddr}\nRAM'i: {self.ram}"


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
#         return f"{self.get_info()}\nLavozimi: {self.lavozimi}"


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


# 17
# class Transport:
#     def __init__(self,nomi,sigimi,qatnov_usuli):
#         self.nomi = nomi
#         self.sigimi = sigimi
#         self.qatnov = qatnov_usuli
#     def get_transport(self):
#         return f"Transport nomi: {self.nomi}\nTransport sig'imi: {self.sigimi}\nQatnov usuli: {self.qatnov}"
# class Avtobus(Transport):
#     def __init__(self, nomi, sigimi, qatnov_usuli, orindiq_soni):
#         super().__init__(nomi, sigimi, qatnov_usuli)
#         self.soni = orindiq_soni
#     def get_avtobus(self):
#         return f"{self.get_transport}\nAvtobusdagi o'rindiqlar soni: {self.soni}"
# class Poyezd(Transport):
#     def __init__(self, nomi, sigimi, qatnov_usuli,vagon_soni):
#         super().__init__(nomi, sigimi, qatnov_usuli)
#         self.vagon = vagon_soni
#     def poyezd_info(self):
#         return f"{self.get_transport()}\nPoyezddagi vagonlar soni: {self.vagon}"


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
#     def __init__(self, yashash_joyi, ismi, kasbi, ish_joyi):
#         super().__init__(yashash_joyi, ismi, kasbi, ish_joyi)



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
# class Chevrolet(Avto):
#     def __init__(self, madel, yil, rang, dvigatel, yoqilgi, uzatma, salon):
#         super().__init__(madel, yil, rang, dvigatel, yoqilgi, uzatma)
#         self.salon = salon
#     def get_info(self):
#         return f"Saloni: {self.salon}"


# 27
# class  Texnika:
#     def __init__(self,modeli,yili,afzalliklari):
#         self.model = modeli
#         self.yili = yili
#         self.afzalliklari = afzalliklari
#     def get_info(self):
#         return f"Modeli: {self.model}\nYili: {self.yili}\nAfzalliklari: {self.afzalliklari}"
# class Printer(Texnika):
#     def __init__(self, modeli, yili, afzalliklari,rangli,rangsiz):
#         super().__init__(modeli, yili, afzalliklari)
#         self.rangli = rangli
#         self.rangsiz = rangsiz
#     def get_data(self):
#         if self.rangli:
#             return f"{self.get_info()}\nPrinter turi: rangli"
#         else:
#             return f"{self.get_info()}\nPrinter turi: rangsiz"
# class Skanner(Texnika):
#     def __init__(self, modeli, yili, afzalliklari,shtrixkod,skanner):
#         super().__init__(modeli, yili, afzalliklari)
#         self.shtrixkod = shtrixkod
#         self.skanner = skanner
#     def get_data(self):
#         if self.shtrixkod:
#             return f"{self.get_info()}\nTuri: shtrixkod"
#         else:
#             return f"{self.get_info()}\nTuri: QR code"


# 29
# class Sportchi:
#     def __init__(self,yoshi,ismi,sport_turi):
#         self.yoshi = yoshi
#         self.ismi = ismi
#         self.sport_turi = sport_turi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nShug'ullanuvchi sport turi: {self.sport_turi}"
# class Futbolchi(Sportchi):
#     def __init__(self, yoshi, ismi, sport_turi, guruh):
#         super().__init__(yoshi, ismi, sport_turi)
#         self.guruh = guruh
#     def get_data(self):
#         return f"{self.get_info()}\nGuruhdaki vazifasi: {self.guruh}"


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
#         return f"{self.get_info()}Universiteti: {self.univeri}\nYo'nalishi: {self.yonalishi}"


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
#     def get_info(self):
#         return f"{self.get_info()}\nMaktabi: {self.maktab}"


# 32
# class Ota:
#     def __init__(self,ismi,yoshi,tel_raqami):
#         self.ism = ismi
#         self.yoshi = yoshi
#         self.tel_raqam = tel_raqami
#     def get_info(self):
#         return f"Ismi: {self.ism}"
# class Bola(Ota):
#     def __init__(self, ismi, yoshi, tel_raqami, maktab):
#         super().__init__(ismi, yoshi, tel_raqami)
#         self.maktab = maktab
#     def get_info(self):
#         return f"{self.get_info()}\nYoshi: {self.yoshi}\nTelefon raqami: {self.tel_raqam}\nMaktabi: {self.maktab}"