
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

# <editor-fold desc="Калькулятор чисел (menu_numbers)">


# TODO подсказки для ввода
def logic_op(): # old: calc_logic
    n = int(input())
    result = 0

    if n == 1:
        first = int(input("Введите первое значение:\n"))
        second = int(input("Введите второе значение:\n"))
        result = first and second
    elif n == 2:
        first = int(input("Введите первое значение:\n"))
        second = int(input("Введите второе значение:\n"))
        result = first or second
    elif n == 3:
        first = int(input("Введите значение:\n"))
        result = not first
    else:
        print("Введено ошибочное значение")

    if 1 <= n <= 3:
        print(bool(result))

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
def dec2other():
    lol=0
    while (lol<1):
        print("1.перевод 10СИ -> 2СИ")

        print("2.перевод 10СИ -> 16СИ")

        print("3.перевод 10СИ -> 8СИ")


        try:
            choice=int(input())
        except ValueError:
            print("надо ввести цифру 1 или 2 или 3")
            dec2other()
        if(choice==1):
            calc_10_2()
            lol += 1
        elif(choice==2):
            calc_10_16()
            lol += 1
        elif(choice==3):
            calc_10_8()
            lol += 1
        else:
            print("надо ввести цифру 1 или 2 или 3")
def calc_10_8():
    print("Введите число:")
    num = int(input())
    eight = list()
    i = 0
    while not num == 0:
        eight.append(num%8)
        num = num//8
        i += 1
    i = 0
    eight.reverse()
    s1 = list()
    for item in eight:
        s1.append(str(item))
    gg = "".join(s1)
    print(gg)
def calc_10_2():
    print("Введите число:")
    num = int(input())
    two = list()
    i = 0
    while not num == 0:
        two.append(num%2)
        num = num//2
        i += 1
    i = 0
    two.reverse()
    s1 = list()
    for item in two:
        s1.append(str(item))
    gg = "".join(s1)
    print(gg)
def calc_10_16():
    print("Введите число:")
    n=int(input())
    alphabet = "0123456789ABCDEF"
    l = list()
    while n > 0 :
        l.append(alphabet[n % 16])
        n //= 16
    l.reverse()
    l2=list()
    for i in l:
        l2.append(str(i))
    lul="".join(l2)
    print(lul)
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
        logic_op()
    elif ch == 6:
        dec2other()
    elif ch == 7:
        check_brackets()

    if ch == 8:
        main()
    else:
        continue_calc()


# </editor-fold>

# <editor-fold desc="Длинная арифметика (menu_long)">

def menu_long(): # old: menu_long_simple
    lol = 0

    while lol < 1:
        print("1. Сложение, вычитание")
        print("2. Умножение")
        print("3. Вернуться в главное меню") # added by Petr

        i = int(input())
        if i == 1:
            long_simple()
            lol += 1
        elif i == 2:
            print("Введите первое число:")
            a = int(input())
            print("Введите второе число:")
            b = int(input())
            print(a * b)
            lol += 1
        elif i == 3:
            main() # added by...
        else:
            print("Такого пункта меню нет! Введите число от 1 до 3")

    continue_calc()


def comp(a, b):
    flag = 0
    if len(a) > len(b):
        flag = 1
    elif len(a) < len(b):
        flag = 2
    else:
        for i in range(len(a)):
            if a[len(a) - i - 1] < b[len(a) - i - 1]:
                flag = 2
                break
            elif a[len(a) - i - 1] > b[len(a) - i - 1]:
                flag = 1
                break
    return flag


def long_simple():
    print('Введите первое число:')
    a = input()
    print('Введите второе число:')
    b = input()
    print('Введите операцию:')
    oper = input()
    first = list()
    second = list()
    for i in range(len(a)):
        first.append(int(a[len(a) - i - 1]))
    for i in range(len(b)):
        second.append(int(b[len(b) - i - 1]))

    while len(first) > 1 and first[-1] == 0:
        first.pop()

    while len(second) > 1 and second[-1] == 0:
        second.pop()
    carry = 0
    result = list()
    if oper == '+':
        result = first[:]
        i = 0
        while i < max(len(result), len(second)) or carry:
            if i == len(result):
                result.append(0)
            tmp = 0
            if i < len(second):
                tmp = second[i]
            result[i] += carry + tmp
            if result[i] >= 10:
                carry = 1
            else:
                carry = 0
            if carry:
                result[i] -= 10
            i += 1
    elif oper == '-':
        if comp(first, second) == 1 or comp(first, second) == 0:
            result = first[:]
            n = len(first) - len(second)
            zer = [0] * n
            second.extend(zer)
            for i in range(len(result)):
                result[i] -= second[i]
                if result[i] < 0:
                    result[i] += 10
                    if i < len(result) - 1:
                        result[i + 1] -= 1
            while len(result) > 1 and result[-1] == 0:
                result.pop()

        elif comp(first, second) == 2:
            result = second[:]
            n = len(second) - len(first)
            zer = [0] * n
            first.extend(zer)
            for i in range(len(result)):
                result[i] -= first[i]
                if result[i] < 0:
                    result[i] += 10
                    if i < len(result) - 1:
                        result[i + 1] -= 1;

            while len(result) > 1 and result[-1] == 0:
                result.pop()
            result.append('-')

    ans = [str(item) for item in result]
    ans = "".join(ans)
    print(ans[::-1])

# </editor-fold>

# <editor-fold desc="Калькулятор строк">

def str_showcenter():
    print("Введите строку: ")

    stroka = str(input())
    dlina_stroki = len(stroka)
    promezh = ' '
    otstup = (80 - dlina_stroki) // 2
    if dlina_stroki % 2 == 0:
        po_gorizontali = promezh * otstup + stroka + otstup * promezh
    else:
        po_gorizontali = promezh * (otstup + 1) + stroka + otstup * promezh
    for i in range(12):
        print(promezh * 80)
    print(po_gorizontali)
    for y in range(12):
        print(promezh * 80)

# </editor-fold>

def continue_calc(msg: str = ""):
    if msg != "":
        print("Ошибка: " + str(msg))
    print("Продолжить считать? [1/0]")
    ch = -1
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
    long_calc_menu_item = MenuItem("Длинная арифметика", menu_long)
    main_menu = Menu(num_calc_menu_item, string_calc_menu_item, long_calc_menu_item)
    main_menu.show()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Программа завершает свою работу по желанию пользователя")
