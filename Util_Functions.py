from datetime import datetime, timedelta


def convert_wind_degree_to_direction(wind_degree):
    """
    Converts wind degree to a cardinal direction.

    Parameters:
    wind_degree (int): Wind degree from the API (0 to 360).

    Returns:
    str: The corresponding wind direction (e.g., N, NE, E, etc.) 
         or "Invalid wind degree format!" if the conversion fails.
    """
    try:
        wind_degree = int(wind_degree)
    except ValueError:
        return "Invalid wind degree format!"

    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", 
        "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    index = (wind_degree + 11.25) // 22.5 % 16
    return directions[int(index)]


def convert_unix_to_local_time(unix_timestamp, timezone_offset):
    """
    Converts a Unix timestamp to local time based on the provided timezone offset.

    Parameters:
    unix_timestamp (str): The Unix timestamp (e.g., "1717715516").
    timezone_offset (str): The timezone offset in seconds (e.g., "28800" for UTC+8).

    Returns:
    str: The local time (e.g., "2024-06-07 07:11:56") or error messages.
    """
    try:
        unix_timestamp = int(unix_timestamp)
    except ValueError:
        return "Invalid sunset/sunrise timestamp format!"

    try:
        timezone_offset = int(timezone_offset)
    except ValueError:
        return "Invalid timezone offset format!"

    # Convert Unix timestamp to UTC time and apply the timezone offset
    utc_time = datetime.utcfromtimestamp(unix_timestamp)
    local_time = utc_time + timedelta(seconds=timezone_offset)

    return local_time.strftime("%Y-%m-%d %H:%M:%S")


def convert_kelvin_to_temp(temperature_kelvin, unit):
    """
    Converts temperature in Kelvin to Celsius or Fahrenheit.

    Parameters:
    temperature_kelvin (str): Temperature in Kelvin (e.g., "291.19").
    unit (str): Unit to convert to ("C" for Celsius, "F" for Fahrenheit).

    Returns:
    str: The temperature in the requested unit (e.g., "21.07 °C" or "67.12 °F").
         Or an error message if the conversion fails.
    """
    try:
        kelvin_temp = float(temperature_kelvin)
    except ValueError:
        return "Invalid temperature format!"

    if unit.upper() not in ["C", "F"]:
        return "Temperature unit must be either 'C' or 'F'!"

    if unit.upper() == "C":
        return f"{kelvin_temp - 273.15:.2f} °C"
    elif unit.upper() == "F":
        return f"{kelvin_temp * 9 / 5 - 459.67:.2f} °F"
