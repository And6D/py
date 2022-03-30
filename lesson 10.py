class House():
    """"описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """строит дом"""
        print('Дом  на улице ' + self.street + " под номером "
        + str(self.number) + " построен.")

    def age_of_house(self, year):
        """возраст дома"""
        self.age = + year

House1 = House("Проспект Кирова", 405)
House2 = House("Проспект Кирова", 407)

House1.build()

House1.age_of_house(77)
print("Возраст дома ", House1.age, " лет")

print("Название улицы", House1.street)
print("Номер дома", House1.number)

class VillageHouse(House):
     """Наследование из класса House"""
     def __init__(self, road, number):
         super().__init__(self,number)
         self.road = road

VHouse = VillageHouse("Не понятно", 405)
print(VHouse.road)
