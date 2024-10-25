class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def survived(self,food):
        print(f'{self.name} съел {food.name}.')
        self.fed = True

    def died(self,food):
        print(f'{self.name} не стал есть {food.name}.')
        self.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True

class Flower(Plant):
    pass

class Mammal(Animal):

    def eat(self, food:Plant):
        if food.edible:
            self.survived(food)
        else:
            self.died(food)

class Predator(Animal):

    def eat(self, food):
        if isinstance(food, Mammal):
            self.survived(food)
            food.alive = False
        elif isinstance(food, Plant):
            self.died(food)
        else:
            print('Пожалуйста, не кормите хищника строчками, числами, истиной/ложью, списками, кортежами и словарями!' \
                  'Это может его убить!')
            self.alive = False

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
a3 = Predator ('Медведь')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
a3.eat(a2)
print(a2.alive)
a3.eat('Кролик')
print(a3.alive)