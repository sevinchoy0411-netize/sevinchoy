class Shifoxona:
    def __init__(self,shifoxona_nomi):
        self.name = shifoxona_nomi
        self.doctors = {
            1:"Xasanov G'olibjon",
            2:"Rahmanova Rayhona",
            3:"Ozodov Mashhur",
            4:"Saparboyeva Fotima"
        }
        self.lor = 0
        self.lorr = []
        self.pediatr = 0
        self.pediatrr = []
        self.stomatolog = 0
        self.stomatologr = []
        self.xirurg = 0
        self.xirurgr = []
    def reserve(self,ism):
        print("Doktorlar ro'yxati")
        for tartib , doctor in self.doctors.items():
            print(f"{tartib} - {doctor}")
        tanlov = int(input("Kerakli doktorni tanlang: "))
        if tanlov == 1:
            self.lor += 1
            self.lorr.append(ism)
            if self.lor == 1:
                print("Siz qabulga birinchi bo'lib yozildingiz")
            else:
                print(f"Siz navbatga {self.lor}-bo'lib yozildingiz. Sizdan oldin {self.lorr[-2]}")
        elif tanlov == 2:
            self.pediatr += 1
            self.pediatrr.append(ism)
            if self.pediatr == 1:
                print("Siz qabulga birinchi bo'lib yozildingiz")
            else:
                print(f"Siz navbatga {self.pediatr}-bo'lib yozildingiz. Sizdan oldin {self.pediatrr[-2]}")
        elif tanlov == 3:
            self.stomatolog += 1
            self.stomatologr.append(ism)
            if self.stomatolog == 1:
                print("Siz qabulga birinchi bo'lib yozildingiz")
            else:
                print(f"Siz navbatga {self.stomatolog}-bo'lib yozildingiz. Sizdan oldin {self.stomatologr[-2]}")
        elif tanlov == 4:
            self.xirurg += 1
            self.xirurgr.append(ism)
            if self.xirurg == 1:
                print("Siz qabulga birinchi bo'lib yozildingiz")
            else:
                print(f"Siz navbatga {self.xirurg}-bo'lib yozildingiz. Sizdan oldin {self.xirurgr[-2]}")
kasal = Shifoxona("Markaziy shifoxona")    
print(kasal.reserve("Aliyev Vali"))
print(kasal.reserve("Sipsayev Sipsagul"))