print("Kalkulator BMI")
print()

height = input("Podaj swój wzrost w centymetrach: ")
weight = input("Podaj swoją wagę w kilogramach: ")

bmi = int(weight) / (int(height) / 100) ** 2

print("Twoje BMI wynosi: " + str(bmi))

if bmi < 18.5:
    print("Masz niedowagę! Zacznij jeść.")
if bmi > 18.5 and bmi < 24.9:
    print("Twoja waga jest w normie. Trzymaj tak dalej!")
if bmi > 25 and bmi < 29.9:
    print("Masz nadwagę! Odżywiaj się zdrowiej!")
if bmi > 30:
    print("Jesteś otyły! Musisz przejść na dietę.")