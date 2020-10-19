import random


class Card:
    def __init__(self, whose_card):
        self.first_row = []
        self.second_row = []
        self.third_row = []
        self.whose_card = whose_card
        self.win_condition = 0

    def get_random_number(self, low_end, high_end):
        random_number = int(random.uniform(low_end, high_end))
        return random_number

    def generation(self):
        gen_count = 0
        for i in range(9):
            initial_check = True
            while initial_check is True:
                first_in_column = self.get_random_number(gen_count, gen_count + 8)
                if first_in_column != 0:
                    self.first_row.append(first_in_column)
                    initial_check = False
            first_check = True
            while first_check is True:
                second_in_column = self.get_random_number(gen_count, gen_count + 9)
                if second_in_column > first_in_column:
                    self.second_row.append(second_in_column)
                    first_check = False
            second_check = True
            while second_check is True:
                third_in_column = self.get_random_number(gen_count, gen_count + 10)
                if third_in_column > second_in_column:
                    self.third_row.append(third_in_column)
                    second_check = False
            gen_count += 10
        last_check = True
        while last_check is True:
            last_digit = self.get_random_number(80, 91)
            if last_digit > self.second_row[8]:
                self.third_row[8] = last_digit
                last_check = False
        for i in range(4):
            repeat_check_1 = True
            while repeat_check_1 is True:
                first_row_delete_index = self.get_random_number(0, 9)
                if self.first_row[first_row_delete_index] != '  ':
                    self.first_row[first_row_delete_index] = '  '
                    repeat_check_1 = False
            repeat_check_2 = True
            while repeat_check_2 is True:
                second_row_delete_index = self.get_random_number(0, 9)
                if self.second_row[second_row_delete_index] != '  ':
                    self.second_row[second_row_delete_index] = '  '
                    repeat_check_2 = False
        for i in range(4):
            empty_column_check = True
            while empty_column_check is True:
                empty_index = self.get_random_number(0, 9)
                if (self.first_row[empty_index] != '  ' or self.second_row[empty_index] != '  ') and self.third_row[empty_index] != '  ':
                    self.third_row[empty_index] = '  '
                    empty_column_check = False

    def card_print(self):
        print(' ' * 7, self.whose_card)
        print('-' * 26)
        print(*self.first_row)
        print(*self.second_row)
        print(*self.third_row)
        print('_' * 26)


class Computer(Card):
    def digit_check(self, digit):
        if self.first_row.count(digit) != 0:
            self.first_row[self.first_row.index(digit)] = '--'
            self.win_condition += 1
        elif self.second_row.count(digit) != 0:
            self.second_row[self.second_row.index(digit)] = '--'
            self.win_condition += 1
        elif self.third_row.count(digit) != 0:
            self.third_row[self.third_row.index(digit)] = '--'
            self.win_condition += 1


class Player(Card):
    def digit_check(self, digit):
        if self.first_row.count(digit) != 0:
            return True
        elif self.second_row.count(digit) != 0:
            return True
        elif self.third_row.count(digit) != 0:
            return True
        else:
            return False

    def digit_cross(self, digit):
        if self.first_row.count(digit) != 0:
            self.first_row[self.first_row.index(digit)] = '--'
        elif self.second_row.count(digit) != 0:
            self.second_row[self.second_row.index(digit)] = '--'
        elif self.third_row.count(digit) != 0:
            self.third_row[self.third_row.index(digit)] = '--'


digit_count = []
for i in range(1, 91):
    digit_count.append(i)


def get_digit():
    digit = random.choice(digit_count)
    digit_count.remove(digit)
    return digit


computer = Computer('Computer')
computer.generation()
player = Player('Player')
player.generation()
computer.card_print()
player.card_print()

while True:
    current_digit = get_digit()
    print('Current digit is {}. Digits left: {}'.format(current_digit, len(digit_count)))
    computer.digit_check(current_digit)
    computer.card_print()
    player.card_print()
    player_choice = input('Is {} in your card? y/n'.format(current_digit))
    if player.digit_check(current_digit) is True and player_choice == 'y':
        player.digit_cross(current_digit)
        player.win_condition += 1
    elif player.digit_check(current_digit) is True and player_choice == 'n':
        print('This digit was in your card! You lose.')
        break
    elif player.digit_check(current_digit) is False and player_choice == 'y':
        print('This digit was not in your card! You lose.')
        break

    if computer.win_condition == 15 and player.win_condition == 15:
        print('It is a tie!')
        break
    elif computer.win_condition == 15:
        print('Computer won!')
    elif player.win_condition == 15:
        print('Player won!')