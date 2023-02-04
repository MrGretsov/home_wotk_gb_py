# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.
N = int(input('Введите N-мерное пространство: '))
# formula = ((X1-Y1)**2 + (X2-Y2)**2)**0.5
coordinates = []
coordinates_2 = []
print()
while True:
    x = input("Координата числа X: ")
    y = input("Координата числа Y: ")
    coordinates_2.append(y)
    coordinates.append(x)
    N -= 1
    if N == 0:
        break
print()
print('Координаты первого числа: ',coordinates)
print()
print('Координаты второго числа: ',coordinates_2)
n = 0
rezult = 0
while (n < len(coordinates)):
    rezult += (int(coordinates[n]) - int(coordinates_2[n]))**2
    n = n + 1
print(rezult**0.5)