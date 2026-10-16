"""Statistical helpers for smart-home sensor measurements."""

import statistics


def get_average(data_dict):
    """Return the arithmetic mean, or None for an empty dictionary."""
    values = list(data_dict.values())
    return statistics.mean(values) if values else None


def get_min(data_dict):
    """Return the minimum value, or None for an empty dictionary."""
    return min(data_dict.values()) if data_dict else None


def get_max(data_dict):
    """Return the maximum value, or None for an empty dictionary."""
    return max(data_dict.values()) if data_dict else None


def get_median(data_dict):
    """Return the median value, or None for an empty dictionary."""
    values = list(data_dict.values())
    return statistics.median(values) if values else None


def find_jumps(data_dict, threshold):
    """Return adjacent measurements whose absolute difference exceeds threshold."""
    items = list(data_dict.items())
    jumps = []

    for (first_label, first_value), (second_label, second_value) in zip(
        items, items[1:]
    ):
        difference = abs(second_value - first_value)
        if difference > threshold:
            jumps.append((first_label, second_label, difference))

    return jumps


def show_table(data_dict, title):
    """Print a formatted table of measurements."""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<12} | {'Значення':>12}")
    print("-" * 27)
    for label, value in data_dict.items():
        print(f"{label:<12} | {value:>12g}")
