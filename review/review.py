# TUPLE
# sonlar = (10,20,30,40)
# print(sonlar , type(sonlar))


# DICT
# eng_uzb = {
#     "aplle" : "olma",
#     "cherry" : "olcha",
#     "pen" : "ruchka",
#     "pencil" : "qalam"
# }
# print(eng_uzb.keys(),eng_uzb.values(),eng_uzb.items())
# soz_tarjima = str(input("soz kiriting: "))
# print(eng_uzb.get(soz_tarjima,"unday so'z yo'q"))


# BREAK
# for i in range(1,150):
#     if i ==  100:
#         break
#     print(i)


# CONTINUE
# for i in range(1,150):
#     if i == 100:
#         continue
#     print(i)


# PASS
# def yigindi(a,b):
#     pass
# print(yigindi(10,20))


# DICT
# programming = {
#     'programmer' : "dasturchi",
#     'developer' : "dasturchi",
#     'syntax' : "kod yozish qoidasi",
#     'algorithm' : "algoritm",
#     'variable' : "o'zgaruvchi",
#     'function' : "funksiya",
#     'data' : "ma'lumot",
#     'erroe' : "xato",
#     'memory' : "xotira",
#     'module' : "modul",
#     'network' : "tarmoq",
#     'user' : "foydalanuvchi",
#     'backend' : "ma'lumotlar bazasi bilan shug'ullanadigan qism",
#     'frontend' : "interfeys",
#     'object' : "obyekt",
#     'comment' : "izoh",
#     'library' : "kutubxona",
#     'string' : "matn",
#     'boolean' : "mantiqiy qiymat",
#     'inheritance' : "merosxo'rlik"
# }


# LAMBDA
# x = lambda a,b: max(a,b)
# print(x(10,20))

# x = lambda a,b,c: f"{a} katta" if a>b and a>c else (f"{b} katta" if b>a and b>c else ("teng" if a==b and a==c else f"{c} katta"))
# print(x(50,50,50))


# REKURSIYA
# def raqam_soni(son):
#     if son == 0:
#         return 0
#     else: 
#         return 1 + raqam_soni(son//10)
# print(raqam_soni(123456789))

# from words import words
# import random
# tasodifiy_soz = random.choice(list(words))
# print(tasodifiy_soz)


# OS
# import os
# print(os.getcwd()) #cwd - current working directionary #joriy papkani bilish
# print(os.listdir()) #papkadagi fayllar royhati
# os.mkdir("Python tili") #yangi papka yaratish
# os.rmdir("Python tili") #papkani o'chitish
# os.makedirs("a/b/c") #papkalar yaratish
# os.removedirs("a/b/c") #papkalar o'chirish
# print(os.path.exists("sevinchoy")) #bor-yo'qlik
# print(os.system()) #OS buyruq


# FAYLLAR BILAN ISHLASH
# f = open("sevinchoy/test.txt","r")
# matn = f.read()
# print(matn)
# f.close()

# f = open("sevinchoy/test.txt" "r")
# for qator in f:
#     print(qator)
# f.close()

# f = open("sevinchoy/test.txt","w")
# matn = input("matn kiriting: ")
# f.write(matn)
# f.close()

# a = open("sevinchoy/test.txt","r")
# oqi = a.read()
# print(oqi)

# with open("test.txt","r") as matn:
    # print(matn.read())

# with open("test.txt","a") as a:
#     a.write("\nYangi qator")

# with open("sevinchoy/matn.txt","x") as f:
#     print(f)

# with open("sevinchoy/matn.txt","w") as w:
#     w.write("salom hammaga")

# with open("sevinchoy/matn.txt","a") as a:
#     a.write("\nYangi qator")

# with open("sevinchoy/matn.txt","r") as r:
#     print(r.read())


# JSON va CSV
# import json
# data = {"Ism" : "Vali","Yoshi" : 20}
# with open("data.json","w") as matn:
#     json.dump(data,matn)

# with open("data.json","r") as f:
#     malumot = json.load(f)
# print(malumot)


# TRY/EXCEPT
# try:
#     son = int(input("a: "))
#     print(son/2)
# except ZeroDivisionError:
#     print("0 kiritmang!!!")
# except ValueError:
#     print("Noto'g'ri qiymat kiritdingiz")

# try:
#     print("5"+10)
# except TypeError:
#     print("Qiymat bir xil emas")

# ismlar = ["ali","vali","hasan","husan"]
# try:
#     print(ismlar[5])
# except IndexError:
#     print("indeks noto'g'ri")

# lugat = {
#     "book" : "kitob",
#     "pen" : "ruchka"
# }
# try: 
#     print(lugat["phone"])
# except KeyError:
#     print("bunday so'z lug'atda yo'q"