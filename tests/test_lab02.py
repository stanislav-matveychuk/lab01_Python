"""Automated checks for both implementations of laboratory work 02."""

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "lab02_modules"
PACKAGE_DIR = ROOT / "lab02_package"


def load_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


module_stats = load_from_path("module_stats", MODULE_DIR / "stats_module.py")
sys.path.insert(0, str(PACKAGE_DIR))
import sensors  # noqa: E402


class StatsContractTests(unittest.TestCase):
    def check_implementation(self, implementation):
        data = {"T1": 18.5, "T2": 20.1, "T3": 27.9, "T4": 23.4, "T5": 16.2}
        self.assertAlmostEqual(implementation.get_average(data), 21.22)
        self.assertEqual(implementation.get_min(data), 16.2)
        self.assertEqual(implementation.get_max(data), 27.9)
        self.assertEqual(implementation.get_median(data), 20.1)
        jumps = implementation.find_jumps(data, 7)
        self.assertEqual([(start, end) for start, end, _ in jumps], [("T2", "T3"), ("T4", "T5")])
        self.assertAlmostEqual(jumps[0][2], 7.8)
        self.assertAlmostEqual(jumps[1][2], 7.2)
        self.assertIsNone(implementation.get_average({}))
        self.assertEqual(implementation.find_jumps({}, 7), [])

    def test_custom_module(self):
        self.check_implementation(module_stats)

    def test_sensors_package(self):
        self.check_implementation(sensors)


if __name__ == "__main__":
    unittest.main()
