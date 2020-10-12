class Stationary:
    title = 'Some stationary'

    def __init__(self):
        pass

    def draw(self):
        draw_result = 'Запуск отрисовки'
        return draw_result


class Pen(Stationary):
    title = 'Pen'

    def __init__(self):
        pass

    def draw(self):
        draw_result = 'Запуск отрисовки ручкой'
        return draw_result


class Pencil(Stationary):
    title = 'Pencil'

    def __init__(self):
        pass

    def draw(self):
        draw_result = 'Запуск отрисовки карандашом'
        return draw_result


class Handle(Stationary):
    title = 'Handle'

    def __init__(self):
        pass

    def draw(self):
        draw_result = 'Запуск отрисовки маркером'
        return draw_result


pen = Pen()
pencil = Pencil()
handle = Handle()
stationary = Stationary()

test_list = [stationary, pen, pencil, handle]

for stationary in test_list:
    print(stationary.title)
    print(stationary.draw())