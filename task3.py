class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(input('wage')), "bonus": float(input('bonus'))}


class Position(Worker):
    def get_full_name(self):
        full_name = self.surname + ' ' + self.name
        return full_name

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        return total_income


worker = Position('Andrew', 'Negrafontov', 'Programmer')
print(worker.get_full_name())
print(worker.get_total_income())