# -*- coding: utf-8 -*-
"""SOA-II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OIiQ9VTWfNPQ_005BiFG8VdQCTo4AoT3
"""

!pip install jupyter-dash

#1
pip install zeep

#2
import zeep

# 3
import requests
from bs4 import BeautifulSoup

wsdl_url1 = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"

client = zeep.Client(wsdl_url1)

celsius_temperature = 30.0
fahrenheit_temperature = client.service.CelsiusToFahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is equal to {fahrenheit_temperature} Fahrenheit")

fahrenheit_temperature = 74.0
celsius_temperature = client.service.FahrenheitToCelsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_temperature} Celsius")

#REDESIGN
@anvil.server.callable
def get_c(temp):
  wsdl_url1 = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
  client1 = zeep.Client(wsdl_url1)

  if 'F' in temp:
    digits = []
    for char in temp:
      if char.isdigit():
        digits += char
    s = "".join(digits)
    s = float(s)
    fahrenheit_temperature = s
    celsius_temperature = client1.service.FahrenheitToCelsius(fahrenheit_temperature)
    res = int(round(float(celsius_temperature)))
    return res

#REDESIGN

@anvil.server.callable
def get_f(temp):
  wsdl_url1 = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
  client1 = zeep.Client(wsdl_url1)

  if 'C' in temp:
      #result = anvil.server.call('get_c', self.temperature_label.text)
      digits = []
      for char in temp:
        if char.isdigit():
          digits += char
      s = "".join(digits)
      s = float(s)
      fahrenheit_temperature = s
      celsius_temperature = client1.service.CelsiusToFahrenheit(fahrenheit_temperature)
      res = int(round(float(celsius_temperature)))
      return res

#

# Define the URL of the WSDL for the CountryInfoService
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/countryinfoservice.wso?WSDL"

client = zeep.Client(wsdl_url)

# Call the FullCountryInfo operation with a country code (e.g., 'USA')
country_code = 'UA'
country_info = client.service.FullCountryInfo(country_code)

country_name = country_info.sName
capital_city = country_info.sCapitalCity

languages = country_info.Languages
for language in languages.tLanguage:
    language_name = language.sName

print(f"Country Name: {country_name}")
print(f"Capital City: {capital_city}")
print(f"Country info: {country_info}")
print("Welcome to the beautiful country of", country_info.sName, "!", '\n',
      "Visit the capital city, a gorgeous ", country_info.sCapitalCity,
      ",", '\n', " and spend local currency, ", country_info.sCurrencyISOCode, " with fun!",
      '\n', "Also remember to learn some frases in local language, ", '\n',
      language_name, ", to have the most of experience!")

#4
!pip install anvil-uplink

#5
import anvil.server

#6
anvil.server.connect("server_NFP3KMKGPWVAXG2IGFTSPU4F-C4PB5CTMNPRFX52D")

@anvil.server.callable
def get_info(country_name):
  country_code = client.service.CountryISOCode(country_name)
  country_info = client.service.FullCountryInfo(country_code)

  languages = country_info.Languages
  for language in languages.tLanguage:
    language_name = language.sName

  result = ("Welcome to the beautiful country of" + country_info.sName + "!" + '\n' +
      "Visit the capital city, a gorgeous " + country_info.sCapitalCity +
      "," + '\n' + " and spend local currency, " + country_info.sCurrencyISOCode + ", with fun!" +
      '\n' + "Also remember to learn some frases in local language, " + '\n' +
      language_name + ", to have the most of experience!")
  return result

#7
@anvil.server.callable
def get_weather(country_name):
  country_code = client.service.CountryISOCode(country_name)
  country_info = client.service.FullCountryInfo(country_code)

  capital_city = country_info.sCapitalCity

  city = capital_city
  url = "https://www.google.com/search?q="+"weather"+city

  html = requests.get(url).content

  soup = BeautifulSoup(html, 'html.parser')

  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
  if temp_element:
    temp = temp_element.text
  else:
      temp = "Temperature not found"

  str_element = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
  if str_element:
      str = str_element.text
      data = str.split('\n')
      if len(data) >= 2:
          time = data[0]
          sky = data[1]
      else:
          time = "Time not found"
          sky = "Sky description not found"
  else:
      time = "Time and sky description not found"

  listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

  strd = listdiv[5].text

  pos = strd.find('Wind')
  other_data = strd[pos:]

  result = ("Capital: " + capital_city + '\n' +
            "Time: " + time + '\n' +
            "Temperature: " + temp + '\n' +
            "Sky State: " + sky + '\n' +
            "Secondary data: " + other_data)
  return result

@anvil.server.callable
def get_temp(country_name):
  country_code = client.service.CountryISOCode(country_name)
  country_info = client.service.FullCountryInfo(country_code)

  capital_city = country_info.sCapitalCity

  city = capital_city
  url = "https://www.google.com/search?q="+"weather"+city

  html = requests.get(url).content

  soup = BeautifulSoup(html, 'html.parser')

  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
  if temp_element:
    temp = temp_element.text
  else:
      temp = "Temperature not found"

  return temp

temp = '74F'
get_c = get_c(temp)
get_c

anvil.server.wait_forever()

temp = '23C'
get_f = get_f(temp)
get_f

@anvil.server.callable
def get_c(country_name):
  country_code = client.service.CountryISOCode(country_name)
  country_info = client.service.FullCountryInfo(country_code)

  capital_city = country_info.sCapitalCity

  city = capital_city
  url = "https://www.google.com/search?q="+"weather"+city

  html = requests.get(url).content

  soup = BeautifulSoup(html, 'html.parser')

  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
  if temp_element:
    temp = temp_element.text
  else:
      temp = "Temperature not found"  # Handle the case when temperature is not found

  wsdl_url1 = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
  client1 = zeep.Client(wsdl_url1)

  if 'C' in temp:
    digits = []
    for char in temp:
      if char.isdigit():
        digits += char
    s = "".join(digits)
    s = float(s)
    fahrenheit_temperature = s
    celsius_temperature = client1.service.FahrenheitToCelsius(fahrenheit_temperature)
    res = celsius_temperature
    return res

@anvil.server.callable
def get_f(country_name):
  country_code = client.service.CountryISOCode(country_name)
  country_info = client.service.FullCountryInfo(country_code)

  # Access specific information about the country
  capital_city = country_info.sCapitalCity

  city = capital_city

  url = "https://www.google.com/search?q="+"weather"+city


  html = requests.get(url).content


  soup = BeautifulSoup(html, 'html.parser')

  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
  if temp_element:
    temp = temp_element.text
  else:
      temp = "Temperature not found"

  wsdl_url1 = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"

  client1 = zeep.Client(wsdl_url1)

  if 'F' in temp:
      #result = anvil.server.call('get_c', self.temperature_label.text)
      digits = []
      for char in temp:
        if char.isdigit():
          digits += char
      s = "".join(digits)
      s = float(s)
      fahrenheit_temperature = s
      celsius_temperature = client1.service.CelsiusToFahrenheit(fahrenheit_temperature)
      res = celsius_temperature
      return res

  #celsius_temperature = temp  # Replace with your desired temperature in Celsius
  #fahrenheit_temperature = client1.service.CelsiusToFahrenheit(celsius_temperature)
  #res = (fahrenheit_temperature + "°F")
  #return res