class Building:
    def __init__(self, square, price, tenants):
        self.square = square
        self.price = price
        self.tenants = tenants
    def info(self):
        print(f'Площадь: {self.square} кв.м.')
        print(f'Cтоимость 1 кв.метра: {self.price} руб.')
        print(f'Количество проживающих: {self.tenants}')
    def calculate_price(self):
        print(f'Общая стоимость: {self.square * self.price}')

class Country_House(Building):
    def __init__(self, square, price, tenants, area):
        super().__init__(square, price, tenants)
        self.area = area
    def price_to_tenants(self):
        print(f'Соотношение стоимости к числу проживающих: {(self.square * self.price)/self.tenants}')
    def info(self):
        super().info()
        print(f'Область или край: {self.area}')

class Apartment_Building(Country_House):
    def __init__(self, square, price, tenants, area, city):
        super().__init__(square, price, tenants, area)
        self.city = city
    def price_to_tenants(self):
        print(f'Соотношение стоимости к числу проживающих: {(self.square * self.price)/self.tenants}')
    def info(self):
        super().info()
        print(f'Город: {self.city}')


f = Building(235, 44.1, 5)
f.info()
f.calculate_price()
print("---------")
a = Apartment_Building(313, 32, 3, "Ленинградская область", "Санкт-Петербург")
a.info()
a.calculate_price()
a.price_to_tenants()

