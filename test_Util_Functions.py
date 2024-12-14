import unittest
from Util_Functions import (
    convert_wind_degree_to_direction,
    convert_unix_to_local_time,
    convert_kelvin_to_temp,
)


class WeatherFunctionsTestCase(unittest.TestCase):
    
    def test_convert_wind_degree_to_direction(self):
        self.assertEqual("ENE", convert_wind_degree_to_direction("60"))
        self.assertEqual("SE", convert_wind_degree_to_direction("130"))
        self.assertEqual("W", convert_wind_degree_to_direction("280"))

    def test_convert_wind_degree_to_direction_invalid_input(self):
        self.assertEqual(
            "Invalid wind degree format!", convert_wind_degree_to_direction("abc")
        )

    def test_convert_unix_to_local_time(self):
        self.assertEqual(
            "2024-06-07 07:11:56", convert_unix_to_local_time("1717715516", "28800")
        )

    def test_convert_unix_to_local_time_invalid_timestamp(self):
        self.assertEqual(
            "Invalid sunset/sunrise timestamp format!",
            convert_unix_to_local_time("abc", "28800"),
        )

    def test_convert_unix_to_local_time_invalid_timezone(self):
        self.assertEqual(
            "Invalid timezone offset format!",
            convert_unix_to_local_time("1717715516", "abc"),
        )

    def test_convert_kelvin_to_temp_celsius(self):
        self.assertEqual("15.44 °C", convert_kelvin_to_temp("288.59", "C"))

    def test_convert_kelvin_to_temp_fahrenheit(self):
        self.assertEqual("59.79 °F", convert_kelvin_to_temp("288.59", "F"))

    def test_convert_kelvin_to_temp_invalid_input(self):
        self.assertEqual(
            "Invalid temperature format!", convert_kelvin_to_temp("abc", "F")
        )

    def test_convert_kelvin_to_temp_invalid_unit(self):
        self.assertEqual(
            "Temperature unit must be either 'C' or 'F'!",
            convert_kelvin_to_temp("288.59", "H"),
        )


if __name__ == "__main__":
    unittest.main()
