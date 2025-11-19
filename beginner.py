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

# 17
# class Uy:
#     def __init__(self,manzil,xonalar):
#         self.manzil = manzil
#         self.xona = xonalar
#     def get_info(self):
#         return f"Uyning manzili: {self.manzil}\nUydagi xonalar soni: {self.xona}"
# uy = Uy("5dom",3)
# print(uy.get_info())

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