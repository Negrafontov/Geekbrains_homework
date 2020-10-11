class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        go = 'Car is moving'
        return go

    def stop(self):
        stop = 'Car is not moving'
        return stop

    def turn(self, direction):
        turn = ('Car has turned ' + direction)
        return turn

    def show_speed(self):
        show_speed = ('Car is moving with a speed of {}'.format(self.speed))
        return show_speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            speed_break = ('Car is moving with a speed of ' + str(self.speed))
            return speed_break
        else:
            show_speed = 'Speed limit is broken!'
            return show_speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            speed_break = ('Car is moving with a speed of ' + str(self.speed))
            return speed_break
        else:
            show_speed = 'Speed limit is broken!'
            return show_speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'blue', 'Town Car', False)
sport_car = SportCar(120, 'red', 'Sport Car', False)
work_car = WorkCar(30, 'yellow', 'Work Car', False)
police_car = PoliceCar(70, 'white', 'Police Car', True)

car_list = [town_car, sport_car, work_car, police_car]


for car in car_list:
    print('_'*10)
    print(car.name)
    print(car.is_police)
    print(car.go())
    print(car.show_speed())
    print(car.turn('left'))
    print(car.stop())