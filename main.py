from tkinter import *


def draw_color(color):
    """
    Функция создает прямоугольник нужного цвета
    :param color:
    :return:
    """
    root = Tk()
    canvas = Canvas(root)
    canvas.pack()
    canvas.create_rectangle(10, 10, 200, 200, fill=color, width=1)
    root.mainloop()


def is_grey(color):
    """
    Фукнкция проверяет серый цвет или нет
    :param color:
    :return:
    """
    return color[1:3] == color[3:5] == color[5:]


def to_grey(color):
    """
    Функция возращет значения необходимые для получения серого
    :param color:
    :return:
    """
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:7], 16)
    if is_grey(color):
        return [0, 0, 0]
    average = int((red + green + blue) / 3)
    new_red = hex(average - red).replace('0x', '')
    new_green = hex(average - green).replace('0x', '')
    new_blue = hex(average - blue).replace('0x', '')
    return [new_red, new_green, new_blue]


def check_input(text):
    """
    Фукнция для проверки ввода цвета
    :param text:
    :return:
    """
    check = '0123456789abcdef'
    if text[0] != '#':
        return False
    if len(text) < 7 or len(text) > 7:
        return False
    for i in text[1:]:
        if i not in check:
            return False
    return True


def menu():
    """
    Меню
    :return:
    """
    while True:
        print('1 - Ввести цвет\n'
              '2 - Инструкция\n'
              '3 - Завершить работу')
        choice = input()
        if choice == '1':
            color = input('Введите цвет: ')
            if not check_input(color):
                print('Ошибка ввода')
                continue
            while True:
                print('1 - Цвет серый?\n'
                      '2 - Сколько до серого?\n'
                      '3 - Вывод цвета\n'
                      '4 - Вернуться к меню')
                choice2 = input()
                if choice2 == '1':
                    if is_grey(color):
                        print('Серый')
                    else:
                        print('Не серый')
                elif choice2 == '2':
                    print('Чтобы получить серый нужно добавить:')
                    red, green, blue = to_grey(color)
                    print(f'крансый:{red} зеленый:{green} синий:{blue}')
                elif choice2 == '3':
                    draw_color(color)
                elif choice2 == '4':
                    break
                else:
                    print('Ошибка ввода')
        elif choice == '2':
            print('Введите число в формате #ababab, где ab - '
                  'число от 0 до 255 в 16-ричной системе счисления')
        elif choice == '3':
            break


menu()
