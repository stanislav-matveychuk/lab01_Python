"""Task 1: process smart-home measurements using a custom module."""

import stats_module as sm


UNITS = {
    "Температура": "°C",
    "Вологість": "%",
    "Тиск": "Па",
}


def parse_input(input_str):
    """Convert a whitespace-separated string to floats, skipping invalid tokens."""
    values = []
    for token in input_str.split():
        try:
            values.append(float(token.replace(",", ".")))
        except ValueError:
            print(f"Попередження: значення «{token}» пропущено (це не число).")
    return values


def create_data_dict(temp_list, hum_list, pres_list):
    """Build the nested measurement dictionary with T1, T2, ... labels."""
    labels = [f"T{index}" for index in range(1, len(temp_list) + 1)]
    return {
        "temperature": dict(zip(labels, temp_list)),
        "humidity": dict(zip(labels, hum_list)),
        "pressure": dict(zip(labels, pres_list)),
    }


def process_measurements(title, data_dict, threshold):
    """Print a table, statistics, and adjacent jumps for one measurement type."""
    sm.show_table(data_dict, title)
    print(f"Середнє значення: {sm.get_average(data_dict):.2f}")
    print(f"Мінімум: {sm.get_min(data_dict):g}")
    print(f"Максимум: {sm.get_max(data_dict):g}")
    print(f"Медіана: {sm.get_median(data_dict):g}")

    jumps = sm.find_jumps(data_dict, threshold)
    if jumps:
        unit = UNITS[title]
        descriptions = [
            f"між {start} → {end} ({difference:g}{unit})"
            for start, end, difference in jumps
        ]
        print("Різкі перепади: " + ", ".join(descriptions))
    else:
        print("Різкі перепади: не виявлено")


def main():
    """Read, validate, organize, and process all measurements."""
    print("=== Обробка показів системи 'Розумний будинок' ===")

    temperatures = parse_input(input("Введіть температури (°C): "))
    humidity = parse_input(input("Введіть вологість (%): "))
    pressure = parse_input(input("Введіть тиск (Па): "))

    lengths = (len(temperatures), len(humidity), len(pressure))
    if 0 in lengths:
        print("Помилка: кожен ряд вимірювань має містити хоча б одне число.")
        return
    if len(set(lengths)) != 1:
        print(
            "Помилка: кількість значень не збігається "
            f"(температура — {lengths[0]}, вологість — {lengths[1]}, "
            f"тиск — {lengths[2]})."
        )
        return

    data = create_data_dict(temperatures, humidity, pressure)
    process_measurements("Температура", data["temperature"], 7)
    process_measurements("Вологість", data["humidity"], 20)
    process_measurements("Тиск", data["pressure"], 5000)


if __name__ == "__main__":
    main()
