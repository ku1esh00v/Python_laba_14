#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_area(type=0):
    def inner_func():
        if type == 0:
            a = float(input("Введите значение первой стороны треугольника: "))
            b = float(input("Введите значение второй стороны треугольника: "))
            c = float(input("Введите значение третьей стороны треугольника: "))

            # Расчитаем  площадь треугольника по формуле Герона
            p = (a + b + c) / 2
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

            return area
        else:
            a = float(input("Введите значение первой стороны прямоугольника: "))
            b = float(input("Введите значение второй стороны прямоугольника: "))

            # Расчет площади прямоугольника
            area = a * b

            return area

    return inner_func


if __name__ == '__main__':
    type = int(input("Введите тип фигуры (0 - треугольник, 1 - прямоугольник): "))
    calculate = calculate_area(type)
    area = calculate()
    print("Площадь фигуры:", area)
