class Kasalxona:
    def __init__(self,shifoxona_nomi):
        self.name = shifoxona_nomi
        self.doktors = {
            "lor" : 0,
            "okulist" : 0,
            "stomatolog" : 0,
            "pediatr" : 0,
            "xirurg" : 0,
            "kardiolog" : 0
        }
    def reserve(self):
        doktor = "\n".join(self.doktors.keys())
        tanlov = input(f"Qaysi doktor qabuliga yozilmoqchisiz?\n{doktor}\nDoktor nomini kiriting: ") 
        if tanlov in self.doktors:
            self.doktors[tanlov] += 1
            return f"Siz {tanlov} doktoriga {self.doktors[tanlov]}-bo'lib yozildingiz"
        else:
            return f"Bunday doktor topilmadi"
kasal = Kasalxona("Markaziy shifoxona")  
print(kasal.reserve())