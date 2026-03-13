class Bank:
    def __init__(self,id,name,age,money,password):
        self.id = id
        self.name = name
        self.age = age
        self.__money = money
        self._password = password
    def get_info(self):
        return f"Mijoz ID: {self.id}\nMijoz name: {self.name}\nMijoz age: {self.age}\nMijoz puli: {self.__money}\nMijoz paroli: {self._password}"
mijoz = Bank(1,'rayhona',25,500000000,2011)
print(mijoz.get_info())