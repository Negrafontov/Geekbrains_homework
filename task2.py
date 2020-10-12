class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def mass(self):
        mass_for_count = input('Наверное, я должен спросить массу асфальта для покрытия одного квадратного метра '
                               'дороги асфальтом(кг)?')
        thickness = input('Введите желаемую толщину полотна, см')
        mass_count = self._length * self._width * float(mass_for_count) * float(thickness)
        return mass_count


my_road = Road(5000, 20)
print(my_road.mass())