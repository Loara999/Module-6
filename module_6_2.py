class Vehicle:
    _COLOR_VARIANTS = ["Красный", "Жёлтый", "Синий"]
    def __init__(self, owner:str, model:str, engine_power:int, color:str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):
        for i in self._COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
                return
        print(f'Нельзя изменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

v1 = Vehicle('Настя', 'Volkswagen Polo', 150, "Белый")
v2 = Sedan('Денис', 'Hyundai Equus', 334, 'Чёрный')
v2.print_info()
v2.set_color('Розовый')
v2.set_color('Красный')
v2.owner = "Denis"
v2.print_info()