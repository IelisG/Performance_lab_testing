import sys
import math

if __name__ == "__main__":
    # Ввод пути к файлу 1 (Координаты центра окружности и его радиус)
    path_1 = sys.argv[1]
    # Ввод пути к файлу 2 (Координаты точек)
    path_2 = sys.argv[2]

    # Считываем координаты окружности из файла 1 построчно
    with open(path_1, 'r') as file:
        x_circle, y_circle = map(int, file.readline().strip().split())
        radius = int(file.readline().strip())

    # Считываем координаты точек из файла 2, и записываем их в список из кортежей.
    with open (path_2, 'r') as file:
        dots = [tuple(map(float, line.strip().split())) for line in file]

    # Поиск расстояния относительно координат окружности и точек
    for dot in dots:
        x_dot, y_dot = dot[0], dot[1]
        distance = math.sqrt((x_dot - x_circle) ** 2 + (y_dot - y_circle) ** 2)
        if distance == radius:
            result = 0
        elif distance < radius:
            result = 1
        else:
            result = 2
        print(result)
