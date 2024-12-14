import requests
from datetime import datetime
from Util_Functions import (
    get_wind_direction,
    convert_unix_to_local_time,
    convert_temp_units,
)


def get_weather_data(api_key, city_name):
    """
    Fetches weather data from OpenWeatherMap API for a specific city.

    Parameters:
    api_key (str): API key for OpenWeatherMap.
    city_name (str): The name of the city to fetch the weather for.

    Returns:
    dict: The parsed JSON response from the API, or None if an error occurs.
    """
    try:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(api_url)
        data = response.json()
        return data

    except requests.exceptions.RequestException as error:
        print(f"Error fetching weather data: {error}")
        return None


def save_weather_info(weather_data, unit_of_temp):
    """
    Saves weather details into a text file.

    Parameters:
    weather_data (dict): The weather data in JSON format.
    unit_of_temp (str): The unit for temperature ('C' for Celsius or 'F' for Fahrenheit).
    """
    try:
        with open("weather_report.txt", "w+") as file:
            current_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            if "name" in weather_data and "sys" in weather_data and "country" in weather_data["sys"]:
                file.write(f"Weather Info for {weather_data['name']}, {weather_data['sys']['country']} - {current_time}\n")
                file.write("-" * 60 + "\n")

            if "main" in weather_data:
                file.write(f"Temperature: {convert_temp_units(weather_data['main']['temp'], unit_of_temp)}\n")

            if "weather" in weather_data:
                file.write(f"Weather: {weather_data['weather'][0]['description']}\n")

            if "main" in weather_data:
                file.write(f"Humidity: {weather_data['main']['humidity']}%\n")

            if "wind" in weather_data:
                file.write(f"Wind Speed: {weather_data['wind']['speed']} km/h\n")
                file.write(f"Wind Direction: {get_wind_direction(weather_data['wind']['deg'])}\n")

            if "sys" in weather_data:
                if "sunrise" in weather_data["sys"] and "timezone" in weather_data:
                    file.write(f"Sunrise: {convert_unix_to_local_time(weather_data['sys']['sunrise'], weather_data['timezone'])}\n")

                if "sunset" in weather_data["sys"] and "timezone" in weather_data:
                    file.write(f"Sunset: {convert_unix_to_local_time(weather_data['sys']['sunset'], weather_data['timezone'])}\n")

        print("Weather data saved to weather_report.txt")

    except IOError as error:
        print(f"Error saving file: {error}")


def main():
    """
    Main function to interact with the user and fetch weather data.
    """
    print("Welcome to the Weather Info App!")
    print("Get your OpenWeatherMap API key by signing up at https://home.openweathermap.org/users/sign_up")

    api_key = input("Enter your OpenWeatherMap API key: ")
    city_name = input("Enter the city name: ")
    unit_of_temp = input("Enter temperature unit ('C' for Celsius or 'F' for Fahrenheit): ")

    if unit_of_temp.upper() not in ["C", "F"]:
        print("Invalid temperature unit. Please choose either 'C' or 'F'.")
        return

    weather_data = get_weather_data(api_key, city_name)

    if weather_data:
        if weather_data.get("cod") == "401":
            print("Invalid API key.")
            return
        elif weather_data.get("cod") == "404":
            print("City not found.")
            return

        save_weather_info(weather_data, unit_of_temp)

        print(f"City: {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Temperature: {convert_temp_units(weather_data['main']['temp'], unit_of_temp)}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} km/h")
        print(f"Wind Direction: {get_wind_direction(weather_data['wind']['deg'])}")
        print(f"Sunrise: {convert_unix_to_local_time(weather_data['sys']['sunrise'], weather_data['timezone'])}")
        print(f"Sunset: {convert_unix_to_local_time(weather_data['sys']['sunset'], weather_data['timezone'])}")

    else:
        print("Failed to retrieve weather data. Please check your inputs.")


if __name__ == "__main__":
    main()
