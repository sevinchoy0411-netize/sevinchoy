# 1
# def kvadrat_top(a):
#     return a**2
# print(kvadrat_top(5))

# 2
# def kvadrat_top(a):
#     return a**3
# print(kvadrat_top(2))

# 3
# def faktorial_top(n):
#     kopaytma = 1
#     for i in range(1, n + 1):
#         kopaytma *= i
#     return kopaytma
# print(faktorial_top(5))

# 4
# def juft_toq_aniqla(son):
#     if son%2 == 0:
#         return "juft son"
#     else:
#         return "toq son"
# print(juft_toq_aniqla(120))

# 5
# def ildiz_top(son):
#     return son**(1/2)
# print(ildiz_top(25))

# 6
# def kattasini_top(a ,b):
#     katta = max(a , b)
#     return katta
# print(kattasini_top(12 , 24))

# 7
# def orta_qiymat_top(a , b):
#     orta = (a+b)/2
#     return orta
# print(orta_qiymat_top(12 , 6))

# 8
# def yigindi(sonlar):
#     yigindi = sum(sonlar)
#     return yigindi
# print(yigindi([2, 5, 8, 3, 10]))

# 9
# def eng_katta_element(matn):
#     katta = max(matn , key=len)
#     return f"eng katta element {katta.upper()}"
# print(eng_katta_element(["salom" , "hammaga"]))

# 10
# def eng_kichik_element(matn):
#     kichik = min(matn , key=len)
#     return f"eng kichik element {kichik.upper()}"
# print(eng_kichik_element(["salom" , "hammaga"]))

# 11
# def soz_sana(matn):
#     bolakla = matn.split()
#     soz = len(bolakla)
#     return soz
# print(soz_sana("salom hammaga qalaysiz yaxshimisiz ahvollaringiz yaxshimi"))

# 12
# def harf_soni(matn):
#     harflar_soni = 0
#     for harf in matn:
#         if harf != " ":
#             harflar_soni += 1
#     return harflar_soni
# print(harf_soni("salom hammaga"))

# 13
# def uzun_soz(matn):
#     bolakla = matn.split()
#     uzun = max(bolakla , key=len)
#     return f"eng uzun soz {uzun}.upper()"
# print(uzun_soz("salom hammaga"))

# 14
# def teskari(matn):
#     return matn[::-1]
# print(teskari("salom hammaga"))

# 15
# def orta_qiymat(sonlar):
#     yigindi = sum(sonlar)
#     orta = yigindi/len(sonlar)
#     return orta
# print(orta_qiymat([12,90,85,78]))

# 16
# def yigindi_top(n):
#     yigindi = 0
#     for i in range(1, n + 1):
#         yigindi += i
#     return yigindi
# print(faktorial_top(5))

# 17
# def kopaytir(n):
#     kopaytma = 1
#     for i in range(1, n + 1):
#         kopaytma *= i
#     return kopaytma
# print(kopaytir(5))

# 18
# def juft_yig(sonlar):
#     juft = []
#     for i in sonlar:
#         if i%2==0:
#             juft.append(i)
#     return juft
# print(juft_yig([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]))

# 19
# def toq_yig(sonlar):
#     toq = []
#     for i in sonlar:
#         if i%2!=0:
#             toq.append(i)
#     return toq
# print(toq_yig([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]))

# 20
# def musbat_yig(sonlar):
#     musbat = []
#     for i in sonlar:
#         if i > 0:
#             musbat.append(i)
#     return musbat
# print(musbat_yig([-1,2,-3,4,-5,6,-7,8,-9,10]))

# 21
# def manfiy_yig(sonlar):
#     manfiy = []
#     for i in sonlar:
#         if i < 0:
#             manfiy.append(i)
#     return manfiy
# print(manfiy_yig([-1,2,-3,4,-5,6,-7,8,-9,10]))

# 23
# def teskari_royxat(royxat):
#     return royxat[::-1]
# print(teskari_royxat(["salom","hammaga"]))

# 24
# def tubligini_aniqla(son):
#     boluvchilari_soni = 0
#     for i in range(1 , son+1):
#         if son%i==0:
#             boluvchilari_soni += 1
#     if boluvchilari_soni == 2:
#         return f"{son} tub son"
#     else:
#         return f"{son} muarakkab son"
# print(tubligini_aniqla(10))

# 26
# def ekub_top(a,b):
#     boluvchi = []
#     eng_kichik = min(a,b)
#     for i in range(1 , eng_kichik+1):
#         if a%i==0 and b%i==0:
#             boluvchi.append(i)
#         ekub = max(boluvchi)
#     return f"{a} va {b} sonlarining ekubi {ekub}ga teng"
# print(ekub_top(5 , 10))

# 27
# def count_ekuk(a,b):
#     boluvchi = []
#     eng_kichik = min(a,b)
#     for i in range(1 , eng_kichik+1):
#         if a%i==0 and b%i==0:
#             boluvchi.append(i)
#         ekub = max(boluvchi)
#         ekuk = a*b/ekub
#     return ekuk
# print(count_ekuk(12,15))

# 28
# def fibonacci(son):
#     a , b = 0 , 1
#     for i in range(1 , son+1):
#         print(a , end=' ')
#         a , b = b , a+b
# fibonacci(10)

# 30
# def katta_qil(matn):
#     return matn.upper()
# print(katta_qil("salom hammaga"))

# 31
# def kichik_qil(matn):
#     return matn.lower()
# print(kichik_qil("SALOM HAMMAGA"))

# 32
# def del_unli(matn):
#     unlilar = "uioea"
#     unlisiz = []
#     for harf in matn:
#         if harf not in unlilar:
#             unlisiz.append(harf)
#         matnga = "".join(unlisiz)
#     return matnga
# print(del_unli("salom hammaga"))

# 33
# def del_undosh(matn):
#     undosh = "qrtypsdfghjklzxcvbnm"
#     undoshsiz = []
#     for harf  in matn:
#         if harf not in undosh:
#             undoshsiz.append(harf)
#         matnga = "".join(undoshsiz)
#     return matnga
# print(del_undosh("salom hammaga"))

# 34
# def kattaroq_qil(matn):
#     return matn.title()
# print(kattaroq_qil("salom hammaga qalaysiz zormisiz"))

# 37
# def palindrom(son):
#     if son%11 == 0:
#         return f"{son} palindrom"
#     else:
#         return f"{son} palindrom emas"

# 38
# def palindrom_top(matn):
#     if matn[::-1] == matn:
#         return f"{matn} palindrom"
#     else:
#         return f"{matn} palindrom emas"
# print(palindrom_top("ikki"))

# 39
# def element_soni(royxat):
#     return len(royxat)
# print(element_soni(["salom" , "hammaga"]))

# 40
# def string_qil(royxat):
#     matn = " ".join(royxat)
#     return matn
# print(string_qil(["salom" , "hammaga" , "qalaysiz"]))

# 41
# def tartibla(son):
#     son.sort()
#     return son
# print(tartibla([1,20, 80 , 90 , 34 , 56]))

# 42
# def juft_chiqar(son):
#     juft = []
#     for i in son:
#         if i%2==0:
#             juft.append(i)
#     return juft
# print(juft_chiqar([1 , 3 , 2 , 4 , 5 , 6 , 7 , 8 , 9 , 10]))

# 43
# def manfiy(son):
#     manfiy = []
#     for i in son:
#         if i < 0:
#             manfiy.append(i)
#     return manfiy
# print(manfiy([1 , -2 , 3 , -4 , 5 , -6 , 7 , -8 , 9 , -10]))

# 44
# def daraja_qaytar(son , daraja):
#     return son**daraja
# print(daraja_qaytar(2 , 3))

# 45
# def teskari_qaytar(royxat):
#     teskari = []
#     for soz in royxat[::-1]:
#         teskari.append(soz[::-1])
#     return teskari
# print(teskari_qaytar(["salom", "hammaga"]))

# 46
# def yilni_aniqla(yil):
#     if (yil%4 == 0 or yil%400 == 0) and yil%100 != 0:
#         return f"{yil} yil kabisa yili"
#     else:
#         return f"{yil} yil kabisa yili emas"
# print(yilni_aniqla(2020))

# 47
# def kvadrat_qaytar(son):
#     for i in son:
#         print(i**2, end=" ")
# print(kvadrat_qaytar([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]))

# 48
# def kub_qaytar(son):
#     for i in son:
#         print(i**3, end=" ")
# print(kub_qaytar([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]))

# 49
# def hisobla(n):
#     if n == 0:
#         return 0
#     else:
#         return n + hisobla(n-1)
# print(hisobla(10))

# 50
# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return faktorial(n-1)*n
# print(faktorial(5))

# 51
# def fibonacci(son):
#     if son == 1 or son == 2:
#         return 1
#     else:
#         return fibonacci(son-1)+fibonacci(son-2)
# for i in range(1 , 10):
#     print(fibonacci(i) , end=" ")