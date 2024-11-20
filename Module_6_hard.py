import math


class Figure:
    sides_count = 0

    def __new__(cls, colors: tuple, *sides):
        switch = cls.__is_valid_color(colors)
        if switch:
            return super().__new__(cls)
        else:
            print(
                'Объект не создан. Параметр "colors" должен быть кортежем из 3х целых чисел (от 0 до 255 включительно).')
            return None

    def __init__(self, colors: tuple, *sides):
        self.__color = colors
        self.__sides = []
        if self.__is_valid_size(sides):
            self.__sides = list(sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(colors: tuple):
        switch = True
        if len(colors) == 3:
            for i in colors:
                if i < 0 or i > 255 or isinstance(i, int) == False:
                    switch = False
        else:
            switch = False
        return switch

    def __is_valid_size(self, sides: tuple):
        if len(sides) == self.sides_count:
            for i in sides:
                if isinstance(i, int) == False or i <= 0:
                    return False
        else:
            return False
        return True

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        switch = Figure.__is_valid_color((r, g, b))
        if switch:
            self.__color = (r, g, b)
            return self.__color
        else:
            print(
                'Цвет не был изменён. Параметры r, g, b должны быть целыми числами в пределах от 0 до 255 включительно.')
            return

    def set_sides(self, *new_sides):
        if self.__is_valid_size(new_sides):
            self.__sides = list(new_sides)
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)
        self.__radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 1

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)

    def get_square(self):
        p = 0.5 * len(self)
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, *sides):
        super().__init__(colors)
        self.__sides = []
        if len(sides) == 1 and isinstance(sides[0], int):
            n = sides[0]
        else:
            n = 1
        for i in range(self.sides_count):
            self.__sides.append(n)
        self._Figure__sides = self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
