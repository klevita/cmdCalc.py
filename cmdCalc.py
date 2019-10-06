# <editor-fold desc="Классы для меню">

class MenuItem:
    def __init__(self, name, f):
        self.name = str(name)
        self.f = f

    def print(self, index):
        print(str(index + 1) + ") " + self.name)


class Menu:
    def __init__(self, *items):
        self.items = items[:]

    def select(self, index: int):
        try:
            if index < 0:
                raise IndexError()
            self.items[index].f()
        except NotImplementedError:
            continue_calc("этот пункт меню ещё не реализован")
        except IndexError:
            continue_calc("не найден пункт меню #" + str(index + 1))

    def print(self):
        for i in range(len(self.items)):
            self.items[i].print(i)

    def show(self):
        self.print()
        try:
            i = int(input()) - 1
        except ValueError:
            continue_calc("номер пункта меню должен быть целым числом")
            return
        self.select(i)


# </editor-fold>

# <editor-fold desc="Чужие меню">

# <editor-fold desc="Калькулятор чисел (menu_numbers)">

def calc_extended():
    print('1. Возведение в степень')
    print('2. Остаток от деления')
    print('3. Корень числа')
    cnt = int(input())
    if cnt == 1:
        print('Введите основание')
        a = int(input())
        print('Введите степень')
        b = int(input())
        print(a ** b)
    elif cnt == 2:
        print('Введите число')
        a = int(input())
        print('Введите делитель')
        b = int(input())
        while b == 0:
            print('Делить на ноль нельзя, введите другое число')
            b = int(input())
        print(a % b)
    elif cnt == 3:
        print('Введите число')
        a = int(input())
        print(a ** 0.5)
    continue_calc()


def check_brackets():
    print('Введите строку с формулой:')
    data = input()
    cnt = 0
    answer = True
    for item in data:
        if item == '(':
            cnt += 1
        elif item == ')':
            cnt -= 1
        if cnt < 0:
            answer = False
    if cnt == 0 or answer:
        print('ДА')
    else:
        print('НЕТ')
    continue_calc()


def menu_numbers():
    print("1. Простые операции")
    print("2. Расширенные операции")
    print("3. Тригонометрические действия с градусами")
    print("4. Тригонометрические действия с радионами")
    print("5. Логические операции")
    print("6. Перевод чисел в различные СС")
    print("7. Проверка скобок")
    print("8. Вернуться в главное меню")
    ch = -99
    try:
        ch = int(input())
    except ValueError:
        print("Введите число от 1 до 8!")
        menu_numbers()
    if ch < 1 or ch > 8:
        print("Введите число от 1 до 8!")
        menu_numbers()
    elif ch == 1:
        not_supported_menu('simple_op')
    elif ch == 2:
        calc_extended()
    elif ch == 3:
        not_supported_menu('trigon_deg')
    elif ch == 4:
        not_supported_menu('trigon_rad')
    elif ch == 5:
        not_supported_menu('logical_op')
    elif ch == 6:
        not_supported_menu('dec2other')
    elif ch == 7:
        check_brackets()
    elif ch == 8:
        main()


# </editor-fold>

# </editor-fold>

def continue_calc(msg: str = ""):
    if msg != "":
        print("Ошибка: " + str(msg))
    print("Продолжить считать? [1/0]")
    try:
        ch = int(input())
    except ValueError:
        exit()
    if ch == 1:
        main()


def not_supported_menu(name: str = ""):
    if name != "":
        print(name)
    raise NotImplementedError()


def main():
    num_calc_menu_item = MenuItem("Калькулятор чисел", menu_numbers)
    string_calc_menu_item = MenuItem("Калькулятор строк", not_supported_menu)
    long_calc_menu_item = MenuItem("Длинная арифметика", not_supported_menu)

    main_menu = Menu(num_calc_menu_item, string_calc_menu_item, long_calc_menu_item)
    main_menu.show()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Программа завершает свою работу по желанию пользователя")
