import requests
import click
import re
import weather_icons
from transliterate import translit
from geocoder import ip
from bs4 import BeautifulSoup


# out: ["Tomsk", "Tomsk Republic", "RU"] ↓
CITY, REPUBLIC, COUNTRY = ip("me").address.split(", ")
TEMPERATURE_TYPES = {
    "Закат солнца": None, # ?
    "Восход солнца": None, # ?
    "Преимущественно облачно": None,
    "Преимущественно ясно": None,
    "Преимущественно ясно и слабый дождь": None,
    "Преимущественно ясно и кратковременные осадки": None,
    "Ясно": sun,
    "Частично облачно": None,
    "Частично облачно и слабый дождь": None,
    "Частично облачно и кратковременные осадки": None,
    "Облачно и кратковременные осадки": None,
    "Облачно и временами осадки": None,
    "Облачно и дождь": None,
    "Облачно и кратковременные осадки": None,
    "Облачно и слабый дождь": None,
    "Облачно": None
}


def get_html(url):  # Complete
    response = requests.get(url)
    if response.ok:
        return response.text
    raise Exception(response.status_code)


def get_weather(html):  # Complete
    soup = BeautifulSoup(html, "lxml")

    # out: ["+18", "2 м/с"] ↓
    temperature, wind_speed = soup.find("div", class_="left").find_all("strong")

    # out: "\r\n\t\t\t\t  \tЧастично облачно" ↓
    raw_weather = soup.find("div", class_="right").next_element
    weather = re.sub("\r|\n|\t", "", str(raw_weather)).lstrip()

    # out: "+18°"
    feels_like = soup.find("div", class_="right").find("strong").text

    return temperature.text, wind_speed.text, weather, feels_like


def weather_handling(weather):
    for type in TEMPERATURE_TYPES:
        if weather == type:




def main():
    url = f"https://www.foreca.ru/Russia/{CITY}"
    temperature, wind_speed, weather, feels_like = get_weather(get_html(url))

    print(
    f"""
{translit(CITY, "ru")}
{weather}
    """)


if __name__ == "__main__":
    main()
