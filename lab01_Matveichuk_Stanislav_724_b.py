# Програма для аналізу температурних показів за день

print("=== Аналіз температурних показів за день ===")
print("Введіть до 24 значень температур (через пробіл):")

# Введення температур
data = input("Температури: ").strip().split()

# Перевірка кількості значень
if len(data) == 0 or len(data) > 24:
    print("Помилка: неправильна кількість значень.")
    raise SystemExit

# Перетворення температур у числа
temperatures = []

for item in data:
    try:
        temp = float(item)

        if temp < -40 or temp > 40:
            print("Помилка: температура повинна бути від -40 до 40.")
            raise SystemExit

        temperatures.append(temp)

    except ValueError:
        print("Помилка: введено не число.")
        raise SystemExit

# Перевірка кількості температур
if len(temperatures) < 2:
    print("Помилка: потрібно ввести хоча б два значення.")
    raise SystemExit


# Введення часових міток
print("\nВведіть часові мітки для кожного показу у форматі година:хвилина:")

times = input("Мітки часу: ").strip().split()

# Перевірка кількості міток
if len(times) != len(temperatures):
    print("Помилка: кількість міток не відповідає кількості температур.")
    raise SystemExit

# Перевірка часу
for time in times:
    parts = time.split(":")

    if len(parts) != 2:
        print("Помилка у форматі часу:", time)
        raise SystemExit

    if not parts[0].isdigit() or not parts[1].isdigit():
        print("Помилка у форматі часу:", time)
        raise SystemExit

    hour = int(parts[0])
    minute = int(parts[1])

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        print("Помилка у значенні часу:", time)
        raise SystemExit


# Створення словника
temperature_data = {}

for i in range(len(temperatures)):
    temperature_data[times[i]] = temperatures[i]


# Отримання значень зі словника
values = list(temperature_data.values())
time_list = list(temperature_data.keys())

# Середня температура
average = sum(values) / len(values)

# Мінімальна та максимальна температура
minimum = min(values)
maximum = max(values)

# Кількість додатних і від'ємних температур
positive = 0
negative = 0

for temp in values:
    if temp > 0:
        positive += 1
    elif temp < 0:
        negative += 1


# Пошук різких змін
changes = []

for i in range(len(values) - 1):
    difference = values[i + 1] - values[i]

    if abs(difference) > 7:
        changes.append(
            (time_list[i], time_list[i + 1], difference)
        )


# Виведення результатів
print("\n=== РЕЗУЛЬТАТ АНАЛІЗУ ===")
print("Температурні дані (час → температура):")

for time in temperature_data:
    print(time, "→", temperature_data[time], "°C")

print("\nЗагальна кількість вимірювань:", len(values))
print("Середня температура:", round(average, 2), "°C")
print("Максимальна температура:", maximum, "°C")
print("Мінімальна температура:", minimum, "°C")
print("Кількість додатних температур:", positive)
print("Кількість від’ємних температур:", negative)


# Виведення різких змін
if len(changes) > 0:
    print("\nВиявлено різкі зміни температури:")

    for change in changes:
        print(
            "між", change[0], "та", change[1],
            ": зміна на", change[2], "°C"
        )
else:
    print("\nРізких змін температури не виявлено.")

print("\n=== Кінець аналізу ===")
