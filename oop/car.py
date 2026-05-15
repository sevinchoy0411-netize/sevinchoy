class Car:
    def __init__(self,modeli,narxi,yili,yoqilgi):
        self.model = modeli
        self.price = narxi
        self.year = yili
        self.fuel_type = yoqilgi
    def get_car(self):
        return f"Modeli: {self.model}\nYili: {self.year}\nYoqilg'i turi: {self.fuel_type}\nNarxi: {self.price}"

# avto1 = Car('Cobalt','$13,500',2024,'Benzin/Gaz')
# print(avto1.get_car())

class YengilAvto(Car):
    def __init__(self, modeli, narxi, yili, yoqilgi, tezlik,rangi,dvigatel):
        super().__init__(modeli, narxi, yili, yoqilgi)
        self.color = rangi
        self.engine = dvigatel
        self.speed = tezlik
    def about_car(self):
        return f"Mashina modeli: {self.model}\nMashina rangi: {self.color}\nMashina yili: {self.year}\nYoqilg'i turi: {self.fuel_type}\nDvigateli: {self.engine}\nTezligi: {self.speed}\nMashina narxi: {self.price}"

car1 = YengilAvto('Tesla Model 3','$47,740',2024,'Elektr','201 km/h','To\'q kulrang','Ikki motorli')
print(car1.about_car())