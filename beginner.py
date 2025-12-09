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
# class Dokon:
#     def __init__(self,dokon_nomi):
#         self.dokon = dokon_nomi
#         self.mahsulot = []
#         self.soni = 0
#     def add_product(self,mahsulot_nomi):
#         self.mahsulot_nomi = mahsulot_nomi
#         self.mahsulot.append(self.mahsulot_nomi)
#         self.soni += 1
#     def remove_product(self,mahsulot_name):
#         self.mahsulot.remove(mahsulot_name)
#         self.soni -= 1
#     def change_product(self,eski_mahsulot,yangi_mahsulot):
#        for index,pro in enumerate(self.mahsulot):
#            if pro == eski_mahsulot:
#                self.mahsulot[index] = yangi_mahsulot
#     def get_info(self):
#         matn = "\n".join([name for name in self.mahsulot])
#         return f"{self.dokon} dokonida {self.soni}ta mahsulot bor va ular:\n{matn}"
    
# dokon = Dokon("magnit")
# dokon.add_product("olma")
# dokon.add_product("uzum")
# dokon.add_product("anor")
# dokon.change_product("anor","behi")
# dokon.change_product("uzum" , "shaftoli")
# print(dokon.get_info())


# 5
# class Kompaniya:
#     def __init__(self,kompaniya_nomi):
#         self.kompaniya = kompaniya_nomi
#         self.ishchilar = []
#         self.soni = 0
#     def add_worker(self,ishchi):
#         self.ishchi = ishchi
#         self.ishchilar.append(self.ishchi)
#         self.soni += 1
#     def remove_worker(self,worker):
#         self.ishchilar.remove(worker)
#         self.soni -= 1
#     def change_worker(self,old_worker,new_worker):
#         for index,pro in enumerate(self.ishchilar):
#             if pro == old_worker:
#                 self.ishchilar[index] = new_worker
#     def get_info(self):
#         matn = "\n".join([name for name in self.ishchilar])
#         return f"{self.kompaniya} kompaniyasida {self.soni}ta ishchi bor va ular: \n{matn}"

# kompaniya = Kompaniya("CyberNest")
# kompaniya.add_worker("jorj")
# kompaniya.add_worker("tom")
# kompaniya.add_worker("jasica")
# kompaniya.add_worker("sevinchoy")
# kompaniya.add_worker("ben")
# kompaniya.remove_worker("jorj")
# kompaniya.change_worker("ben","rayhona")
# print(kompaniya.get_info())


# 6
# class Mashina:
#     def __init__(self, model, speed):
#         self.model = model
#         self.speed = speed
#     def speed_up(self):
#         self.speed += 10
#         if self.speed > 240:
#             self.speed = 240
#         return self.speed
#     def slow_down(self):
#         self.speed -= 10
#         if self.speed < 0:
#             self.speed = 0
#         return self.speed

# mashina = Mashina("Tesla", 90)
# print(mashina.speed_up())


# 7
# class Telefon:
#     def __init__(self,nom,brend,batareya):
#         self.nom = nom
#         self.brend = brend
#         self.batareya = batareya
#     def charge(self):
#         self.batareya += 10
#         if self.batareya > 100:
#             self.batareya = 100
#         return self.batareya
# tel = Telefon("iPhone 17","Apple",90)
# print(tel.charge())


# 8
# class Oqituvchi:
#     def __init__(self,name,subject,experiment):
#         self.name = name
#         self.subject = subject
#         self.experiment = experiment
#     def get_info(self):
#         return f"O'qituvchining ismi: {self.name}\nO'qituvchi dars beradigan fan: {self.subject}\nO'qituvchining tajribasi: {self.experiment}"
# ustoz = Oqituvchi("Mirzabek","Dasturlash","4yil")
# print(ustoz.get_info())


# 9
# class Kompyuter:
#     def __init__(self,ram,hdd,cpu):
#         self.ram = ram
#         self.hdd = hdd
#         self.cpu = cpu
#     def get_info(self):
#         return f"Kompyuterning RAMi: {self.ram}\nKompyuterning xotirasi: {self.hdd}\nKompyuterning CPUsi: {self.cpu}"
# kompyuter = Kompyuter("8GB DDR4 2666MHz Kingston","Seagate Barracuda 1TB HDD","Intel Core i5-10400F")
# print(kompyuter.get_info())


# 10
# class Sinf:
#     def __init__(self,sinf):
#         self.sinf = sinf
#         self.oquvchilar = []
#         self.soni = 0
#     def add_pupil(self,new_pupil):
#         self.new_pupil = new_pupil
#         if self.new_pupil not in self.oquvchilar:
#             self.oquvchilar.append(new_pupil)
#             self.soni += 1
#     def del_pupil(self,pupil):
#         self.pupil = pupil
#         if self.pupil in self.oquvchilar:
#             self.oquvchilar.remove(pupil)
#             self.soni -= 1
#     def get_info(self):
#         self.matn = "\n".join(self.oquvchilar)
#         return f"{self.sinf} sinfida {self.soni} ta o'quvchi bor va ular:\n{self.matn}"
# pupil = Sinf("8-A")
# pupil.add_pupil("marjona")
# pupil.add_pupil("rayhona")
# pupil.add_pupil("fotima")
# pupil.add_pupil("sevinchoy")
# pupil.add_pupil("marjona")
# print(pupil.get_info())


# 11
# class Shaxs:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def tanishuv(self):
#         return f"Mening ismim {self.ism} yoshim {self.yosh}"
# shaxs = Shaxs("sevinchoy",14)
# print(shaxs.tanishuv())


# 12
# class Maktab:
#     def __init__(self,maktab_soni):
#         self.maktab = maktab_soni
#         self.sinflar = []
#         self.soni = 0
#     def add_class(self,new_class):
#         self.new_class = new_class
#         if self.new_class not in self.sinflar:
#             self.sinflar.append(new_class)
#             self.soni += 1
#     def get_info(self):
#         self.matn = "\n".join(self.sinflar)
#         return f"{self.maktab} - maktabda {self.soni}ta sinf bor va ular:\n{self.matn}"
# maktab = Maktab(6)
# maktab.add_class("1-A")
# maktab.add_class("2-A")
# maktab.add_class("3-A")
# maktab.add_class("4-A")
# maktab.add_class("5-A")
# maktab.add_class("6-A")
# maktab.add_class("7-A")
# maktab.add_class("8-A")
# print(maktab.get_info())


# 13
# class Kitob:
#     def __init__(self,nomi,muallifi,sahifa_soni):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.sahifa_soni = sahifa_soni
#     def get_info(self):
#         return f"Kitob nomi: {self.nomi}\nKitob muallifi: {self.muallifi}\nKitobning sahifalari soni: {self.sahifa_soni}"
# kitob = Kitob("Al-karnaku kemasidagi qotillik","Agata Kristi",215)
# print(kitob.get_info())


# 14
# class Kutubxona:
#     def __init__(self,kutubxona_nomi):
#         self.nomi = kutubxona_nomi
#         self.kitoblar = []
#     def add_book(self,kitob):
#         self.kitob = kitob
#         if self.kitob not in self.kitoblar:
#             self.kitoblar.append(kitob)
#     def get_info(self):
#         self.matn = "\n".join(self.kitoblar)
#         return f"{self.nomi} kutubxonasidagi kitoblar:\n{self.matn}"
# kutubxona = Kutubxona("Alisher Navoiy")
# kutubxona.add_book("O'n besh yoshli kapitan")
# kutubxona.add_book("Sariq devni minib")
# kutubxona.add_book("Odam bo'lish qiyin")
# kutubxona.add_book("O'tkan kunlar")
# print(kutubxona.get_info())


# 15
# class Mahsulot:
#     def __init__(self,mahsulot_nomi):
#         self.product = mahsulot_nomi
#     def get_info(self):
#         return f"{self.product}"

# class Dokon:
#     def __init__(self,dokon_nomi):
#         self.market_name = dokon_nomi
#         self.mahsulot = []
#         self.son = 0
#     def add_product(self,mahsulot_nomi):
#         narsa = Mahsulot(mahsulot_nomi)
#         self.mahsulot.append(narsa)
#         self.son += 1
#     def get_product(self):
#         malumot = "\n".join([product.get_info() for product in self.mahsulot])
#         return f"{self.market_name} dokonida {self.son} ta mahsulot bor ular: \n{malumot}"

# dokon = Dokon("magnit")
# dokon.add_product("olma")
# dokon.add_product("anor")
# dokon.add_product("nok")
# print(dokon.get_product())


# 16
# class Hayvon:
#     def __init__(self,ismi,turi):
#         self.name = ismi
#         self.kind = turi
#     def ovoz_chiqar(self):
#         if self.name == "mushuk":
#             return "Miyov-miyov"
#         elif self.name == "it":
#             return "Vov-vov"
# hayvon = Hayvon("mushuk","mushuk")
# print(hayvon.ovoz_chiqar())

# 17
# class Uy:
#     def __init__(self,manzil,xonalar):
#         self.manzil = manzil
#         self.xona = xonalar
#     def get_info(self):
#         return f"Uyning manzili: {self.manzil}\nUydagi xonalar soni: {self.xona}"
# uy = Uy("5dom",3)
# print(uy.get_info())


# 18
# class Shaxs:
#     def __init__(self,ismi,yoshi):
#         self.name = ismi
#         self.age = yoshi
#     def get_info(self):
#         return f"Ismi: {self.name} yoshi: {self.age}"

# class Oila:
#     def __init__(self,oila_nomi):
#         self.family_name = oila_nomi
#         self.odam = []
#         self.soni = 0
#     def add_member(self,ismi,yoshi):
#         member = Shaxs(ismi,yoshi)
#         self.odam.append(member)
#         self.soni += 1
#     def get_member(self):
#         data = "\n".join([shaxs.get_info() for shaxs in self.odam])
#         return f"{self.family_name} oilasida {self.soni} ta odam bor ular: \n{data}"
# oila = Oila("kimdir")
# oila.add_member("Sevinchoy",14)
# oila.add_member("Zuhra",10)
# oila.add_member("Tohirjon",1)
# print(oila.get_member())


# 19
# class Sportchi:
#     def __init__(self,ism,sport,natija):
#         self.ism = ism
#         self.sport = sport
#         self.natija = natija
#     def get_info(self):
#         return f"Sportchi haqida ma'lumot:\nIsmi: {self.ism}\nSport turi: {self.sport}\nNatijasi: {self.natija}"
# sportchi = Sportchi("hgde","jwhf","ghuj")
# print(sportchi.get_info())


# 20
# class Sportchi:
#     def __init__(self,ism,sport,natija):
#         self.ism = ism
#         self.sport = sport
#         self.natija = natija
#     def get_info(self):
#         return f"Ismi: {self.ism} sport turi: {self.sport} natijasi: {self.natija}"
# class Stadion:
#     def __init__(self,stadion_nomi):
#         self.nomi = stadion_nomi
#         self.sportchilar = []
#         self.soni = 0
#     def add_athlet(self,ism,sport,natija):
#         athlet = Sportchi(ism,sport,natija)
#         self.sportchilar.append(athlet)
#         self.soni += 1
#     def get_athlet(self):
#         data = "\n".join([athlet.get_info() for athlet in self.sportchilar])
#         return f"{self.nomi} stadionida {self.soni} ta sportchi bor va ular: \n{data}"
# stadion = Stadion("nimadir")
# stadion.add_athlet("hgde","jwhf","ghuj")
# stadion.add_athlet("hgde","jwhf","ghuj")
# stadion.add_athlet("hgde","jwhf","ghuj")
# print(stadion.get_athlet())


# class Ishchi:
#     def __init__(self,ismi,yoshi,vazifasi):
#         self.ism = ismi
#         self.yosh = yoshi
#         self.vazifa = vazifasi
#     def get_info(self):
#         return f"Ismi: {self.ism} yoshi: {self.yosh} vazifasi: {self.vazifa}"

# class Kompaniya:
#     def __init__(self,kompaniya_nomi):
#         self.nomi = kompaniya_nomi
#         self.workers = []
#         self.soni = 0
#     def add_worker(self,ismi,yoshi,vazifasi):
#         worker = Ishchi(ismi,yoshi,vazifasi)
#         self.workers.append(worker)
#         self.soni += 1
#     def get_worker(self):
#         data = "\n".join([ishchi.get_info() for ishchi in self.workers])
#         return f"{self.nomi} kompaniyasida {self.soni} ta ishchi bor ular: \n{data}"
# kompaniya = Kompaniya("CyberNest")
# kompaniya.add_worker("jorj",15,"dasturchi")
# kompaniya.add_worker("tom",16,"kiberxavfsizlik xodimi")
# kompaniya.add_worker("jasica",17,"developer")
# kompaniya.add_worker("sevinchoy",14,"kiberxavfsizlik hodimi,dasturchi")
# kompaniya.add_worker("ben",15,"dasturchi")
# print(kompaniya.get_worker())


# 22
# class Kino:
#     def __init__(self,nom,janr,davomiylik):
#         self.nom = nom
#         self.janr = janr
#         self.davomiylik = davomiylik
#     def get_info(self):
#         return f"Film nomi: {self.nom}\nJanri: {self.janr}\nDavomiyligi: {self.davomiylik}"
# kino = Kino("Shavqat qilinmaydi","kriminal","1soat")
# print(kino.get_info())


# 23
# class Kino:
#     def __init__(self,nomi,janr,during):
#         self.nom = nomi
#         self.janr = janr
#         self.during = during
#     def get_info(self):
#         return f"Nomi: {self.nom} janri: {self.janr} davomiyligi: {self.during}"

# class Kinoteatr:
#     def __init__(self,kinoteatr_nomi):
#         self.name = kinoteatr_nomi
#         self.kino = []
#     def add_film(self,nomi,janr,during):
#         film = Kino(nomi,janr,during)
#         self.kino.append(film)
#     def get_film(self):
#         matnga = "\n".join([film.get_info() for film in self.kino])
#         return f"{self.name} kinoteatridagi filmlar: \n{matnga}"
# kinoteatr = Kinoteatr("Alisher Navoiy")
# kinoteatr.add_film("shafqat qilinmaydi","kriminal","1soat")
# kinoteatr.add_film("qotil","kriminal","2soat")
# kinoteatr.add_film("o'zganing qasosi","kriminal","2soat")
# kinoteatr.add_film("dozaxdan kelgan sudiya","qorqinchli","3soat")
# print(kinoteatr.get_film())


# class Talaba:
#     def __init__(self,talaba_ismi,talaba_sinfi,talaba_yoshi):
#         self.name = talaba_ismi
#         self.sinf = talaba_sinfi
#         self.age = talaba_yoshi
#     def get_info(self):
#         return f"Talabaning ismi: {self.name} , Talaba sinfi: {self.sinf} , talaba yoshi : {self.age}"

# class Maktab:
#     def __init__(self,maktab_nomi):
#         self.school_name = maktab_nomi
#         self.oquvchilar = []
#         self.oquvchi_soni = 0
#     def add_student(self,talaba_ismi,talaba_sinfi,talaba_yoshi):
#         student = Talaba(talaba_ismi,talaba_sinfi,talaba_yoshi)
#         self.oquvchilar.append(student)
#         self.oquvchi_soni +=1
#     def get_student(self):
#         malumot = "\n".join([talaba.get_info() for talaba in self.oquvchilar])
#         return f"{self.school_name} maktabida {self.oquvchi_soni} ta o'quvchi bor va ular ro'yhati quyidagicha:\n{malumot}"
# maktab_6 = Maktab("6-son maktab")
# maktab_6.add_student("Sevinchoy" , "8-A" , "14")
# maktab_6.add_student("Zoxira" , "9-B",15)
# print(maktab_6.get_student())

# 24
# class Oqituvchi:
#     def __init__(self,ismi,yoshi,fani):
#         self.name = ismi
#         self.age = yoshi
#         self.subject = fani
#     def get_info(self):
#         return f"O'qituvchi ismi: {self.name} , O'qituvchining yoshi: {self.age} , O'qituvchi yo'nalishi: {self.subject}"
# class Maktab:
#     def __init__(self,maktab_nomi):
#         self.number = maktab_nomi
#         self.oqituvchi = []
#         self.soni = 0
#     def add_teacher(self,ismi,yoshi,fani):
#         teacher = Oqituvchi(ismi,yoshi,fani)
#         self.oqituvchi.append(teacher)
#         self.soni += 1
#     def get_tecacher(self):
#         malumot = "\n".join([teacher.get_info() for teacher in self.oqituvchi])
#         return f"{self.number} maktabida {self.soni} ta o'qituvchi bor va ular: \n{malumot}"
# maktab = Maktab("6-son maktab")
# maktab.add_teacher("Barno","30","ingliz tili")
# maktab.add_teacher("Shohista","30","ingliz tili")
# print(maktab.get_tecacher())


# 25
# class Fakultet:
#     def __init__(self,fakultet_nomi):
#         self.name = fakultet_nomi
#     def get_info(self):
#         return f"fakultet nomi: {self.name}"
# class Universitet:
#     def __init__(self,univer_nomi):
#         self.ism = univer_nomi
#         self.facultet = []
#         self.number = 0
#     def add_facultet(self,fakultet_nomi):
#         fakultet = Fakultet(fakultet_nomi)
#         self.facultet.append(fakultet)
#         self.number += 1
#     def get_facultet(self):
#         data = "\n".join([i.get_info() for i in self.facultet])
#         return f"{self.ism} universitetida {self.number} ta fakultet bor va ular: \n{data}"
# univer = Universitet("al-Xorazmiy")
# univer.add_facultet("cybersecurity")
# univer.add_facultet("texnika va IT yo'nalishlari")
# univer.add_facultet("axborot texnologiyalari")
# univer.add_facultet("filologiya")
# print(univer.get_facultet())


# 26
# class Avto:
#     def __init__(self,nomi,yili,rangi):
#         self.nomi = nomi
#         self.yili = yili
#         self.rang = rangi
#     def get_info(self):
#         return f"Avto nomi: {self.nomi} , yili: {self.yili} , rangi: {self.rang}"
# class Avtosalon:
#     def __init__(self,avtosalon_nomi):
#         self.name = avtosalon_nomi
#         self.mashina = []
#         self.soni = 0
#     def add_avto(self,nomi,yili,rangi):
#         avto = Avto(nomi,yili,rangi)
#         self.mashina.append(avto)
#         self.soni += 1
#     def get_avto(self):
#         data = "\n".join([i.get_info() for i in self.mashina])
#         return f"{self.name} avtosalonida {self.soni} ta moshina bor va ular: \n{data}"
# avto = Avtosalon("novidir")
# avto.add_avto("nexia3","2020","oq")
# avto.add_avto("tracker","2024","qora")
# print(avto.get_avto())


# 27
# class Shifokor:
#     def __init__(self,ism,yosh,yonalish):
#         self.name = ism
#         self.age = yosh
#         self.megar = yonalish
#     def get_info(self):
#         return f"Ismi: {self.name}, yoshi: {self.age}, yo'nalishi: {self.megar}"
# class Kasalxona:
#     def __init__(self,kasalxona_nomi):
#         self.hospital = kasalxona_nomi
#         self.doctor = []
#         self.soni = 0
#     def add_doctor(self,ism,yosh,yonalish):
#         doctor = Shifokor(ism,yosh,yonalish)
#         self.doctor.append(doctor)
#         self.soni += 1
#     def get_doctor(self):
#         data = "\n".join([i.get_info() for i in self.doctor])
#         return f"{self.hospital} shifoxonasida {self.soni}ta shifokor bor va ular: \n{data}"
# kasalxona = Kasalxona("novidir")
# kasalxona.add_doctor("gjd","jgd","hye")
# kasalxona.add_doctor("sh","ygd","hdu")
# kasalxona.add_doctor("sg","hsiu","hd")
# print(kasalxona.get_doctor())


# 28
# class Oyinchi:
#     def __init__(self,ism,level,ball):
#         self.name = ism
#         self.level = level
#         self.ball = ball
#     def get_info(self):
#         return f"O'yinchining ismi: {self.name}\nLeveli: {self.level}\nBalli: {self.ball}"
# oyin = Oyinchi("kimdir","nimadir","nechadir")
# print(oyin.get_info())


# 29
# class Oyinchi:
#     def __init__(self,ism,level,ball):
#         self.name = ism
#         self.level = level
#         self.ball = ball
#     def get_info(self):
#         return f"O'yinchining ismi: {self.name}\nLeveli: {self.level}\nBalli: {self.ball}"
# class Oyin:
#     def __init__(self,oyin_nomi):
#         self.game = oyin_nomi
#         self.oyinchilar = []
#         self.soni = 0
#     def add_player(self,ism,level,ball):
#         player = Oyinchi(ism,level,ball)
#         self.oyinchilar.append(player)
#         self.soni += 1
#     def get_player(self):
#         data = "\n".join([i.get_info() for i in self.oyinchilar])
#         return f"{self.game} o'yinida {self.soni}ta o'yinchi bor va ular: \n{data}"
# oyin = Oyin("novidir")
# oyin.add_player("kimdir","nimadir","nechadir")
# print(oyin.get_player())


# 30
# class Taom:
#     def __init__(self):
#         self.meals = []
#     def add_meal(self,new_meal):
#         self.new = new_meal
#         self.meals.append(self.new)
#     def get_meal(self):
#         data = "\n".join(self.meals)
#         return f"Menyu: \n{data}"
# menyu = Taom()
# menyu.add_meal("shashlik")
# menyu.add_meal("somsa")
# menyu.add_meal("manti")
# menyu.add_meal("palov")
# print(menyu.get_meal())

# 31
# class Taom:
#     def __init__(self,nom,narx,kaloriya):
#         self.name = nom
#         self.cost = narx
#         self.caloriya = kaloriya
#     def get_info(self):
#         return f"Nomi: {self.name}\nNarxi: {self.cost}\nKaloriyasi: {self.caloriya}"
# taom = Taom("nimadir","hdyg","dgh")
# print(taom.get_info())

# 32
# class Taom:
#     def __init__(self,nomi,narxi,kaloriyasi):
#         self.name = nomi
#         self.cost = narxi
#         self.caloriya = kaloriyasi
#     def get_info(self):
#         return f"Nomi: {self.name}, narxi: {self.cost}, kaloriyasi: {self.caloriya}"
# class Restoran:
#     def __init__(self,nomi):
#         self.ism = nomi
#         self.menyu = []
#     def add_meal(self,nomi,narxi,kaloriya):
#         meal = Taom(nomi,narxi,kaloriya)
#         self.menyu.append(meal)
#     def get_meal(self):
#         data = "\n".join([i.get_info() for i in self.menyu])
#         return f"{self.ism} restoranidagi taomlar menyusi: \n{data}"
# taom = Restoran("gff")
# taom.add_meal("ds","lgvifd","jgf")
# taom.add_meal("fjs","ihf","ugdh")
# taom.add_meal("jdbn","jds","jhu")
# taom.add_meal("jdb","ygdhs","hd")
# print(taom.get_meal())

# 33
# class Kompyuter:
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.dasturlar = []
#     def add_software(self,new):
#         self.new = new
#         self.dasturlar.append(self.new)
#     def get_software(self):
#         software = "\n".join(self.dasturlar)
#         return f"{self.nomi} kompyuteridagi dasturlar: \n{software}"
# kompyuter = Kompyuter("hp")
# kompyuter.add_software("Visual Studio Code")
# kompyuter.add_software("python")
# kompyuter.add_software("Google")
# kompyuter.add_software("Word")
# kompyuter.add_software("excel")
# print(kompyuter.get_software())


# 34
# class Dastur:
#     def __init__(self,nom,versiya,producer):
#         self.nom = nom
#         self.version = versiya
#         self.producer = producer
#     def get_info(self):
#         return f"Nomi: {self.nom}\nVersiyasi: {self.version}\nIshlab chiqaruvchisi: {self.producer}"
# dastur = Dastur("hf","hf","gfy")
# print(dastur.get_info())


# 35
# class Bank:
#     def __init__(self,banknomi):
#         self.bank = banknomi
#         self.mijozlar = []
#     def mijoz_qoshish(self,mijoz):
#         self.mijoz = mijoz
#         self.mijozlar.append(self.mijoz)
#     def get_info(self):
#         data = "\n".join(self.mijozlar)
#         return f"{self.bank} bankidagi mijozlar: \n{data}"
# bank = Bank("XalqBanki")
# bank.mijoz_qoshish("shg")
# bank.mijoz_qoshish("fd")
# bank.mijoz_qoshish("hghb")
# print(bank.get_info())


# 36
# class Mijoz:
#     def __init__(self,ism,balans):
#         self.ism = ism
#         self.balans = balans
#     def get_info(self):
#         return f"Ismi: {self.ism}\nBalansi: {self.balans}"
# mijoz = Mijoz("dh","hdg")
# print(mijoz.get_info())


# 37
# class Sinf:
#     def __init__(self,sinf):
#         self.sinf = sinf
#         self.fan = []
#     def add_subject(self,fan):
#         self.subject = fan
#         self.fan.append(self.subject)
#     def get_subject(self):
#         data = "\n".join(self.fan)
#         return f"{self.sinf} sinfida o'tiluvchi fanlar: \n{data}"
# sinf = Sinf("hs")
# sinf.add_subject("gfa")
# sinf.add_subject("fygh")
# sinf.add_subject("fgsf")
# sinf.add_subject("hgfs")
# print(sinf.get_subject())


# 38
# class Fan:
#     def __init__(self,nom,teacher):
#         self.name = nom
#         self.teacher = teacher
#     def get_info(self):
#         return f"Nomi: {self.name}\nO'qituvchisi: {self.teacher}"
# fan = Fan("IT","Mirzabek")
# print(fan.get_info())


# 39
# class Institut:
#     def __init__(self,institut_nomi):
#         self.name = institut_nomi
#         self.student = []
#         self.teacher = []
#     def add_student(self,new_student):
#         self.talaba = new_student
#         self.student.append(self.talaba)
#     def add_teacher(self,new_teacher):
#         self.new = new_teacher
#         self.teacher.append(self.new)
#     def get_student(self):
#         talabalar = "\n".join(self.student)
#         return f"{self.name} institutidagi talabalar: \n{talabalar}"
#     def get_teacher(self):
#         teachers = "\n".join(self.teacher)
#         return f"{self.name} institutidagi o'qituvchilar: \n{teachers}"
#     def get_info(self):
#         talabalar = "\n".join(self.student)
#         teachers = "\n".join(self.teacher)
#         return f"{self.name} institutidagi talabalar: \n{talabalar}\nO'qituvchilar: \n{teachers}"
# univer = Institut("al-Xorazmiy")
# univer.add_student("Sevinchoy")
# univer.add_student("Rayhona")
# univer.add_teacher("Mirzabek")
# print(univer.get_info())


# 40
# class Market:
#     def __init__(self,dokon_nomi):
#         self.name = dokon_nomi
#         self.mijozlar = []
#         self.mahsulot = []
#     def add_mijoz(self,mijoz):
#         self.mijoz = mijoz
#         self.mijozlar.append(self.mijoz)
#     def add_product(self,product):
#         self.product = product
#         self.mahsulot.append(self.product)
#     def get_mijoz(self):
#         mijoz = "\n".join(self.mijozlar)
#         return f"Mijozlar: \n{mijoz}"
#     def get_product(self):
#         product = "\n".join(self.mahsulot)
#         return f"{self.name} do'konida bor mahsulotlar: \n{product}"
# market = Market("Xalomaxon")
# market.add_product("olma")
# market.add_product("anor")
# market.add_product("non")
# market.add_product("go'sht")
# print(market.get_product())


# 41
# class Teatr:
#     def __init__(self,teatr_nomi):
#         self.teatr = teatr_nomi
#         self.spektakl = []
#     def add_spektakl(self,spektakl):
#         self.spektakl.append(spektakl)
#     def get_spektakl(self):
#         data = "\n".join(self.spektakl)
#         return f"{self.teatr} teatrida bo'ladigan spektakllar: \n{data}"
# teatr = Teatr("htr")
# teatr.add_spektakl("hgfd")
# teatr.add_spektakl("kgjd")
# teatr.add_spektakl("fh")
# teatr.add_spektakl("hg")
# print(teatr.get_spektakl())


# 42
# class Spektakl: 
#     def __init__(self,nom,muallif,vaqt):
#         self.nom = nom
#         self.muallif = muallif
#         self.vaqt = vaqt
#     def get_spektakl(self):
#         return f"Nomi: {self.nom}\nMuallifi: {self.muallif}\nVaqti: {self.vaqt}"
# spektakl = Spektakl("gjh","ghc","fgvy")
# print(spektakl.get_spektakl())