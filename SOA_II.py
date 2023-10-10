{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install jupyter-dash"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r9CwCIxabomj",
        "outputId": "214fa5fb-6156-4a58-fb91-70e715f5843f"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting jupyter-dash\n",
            "  Downloading jupyter_dash-0.4.2-py3-none-any.whl (23 kB)\n",
            "Collecting dash (from jupyter-dash)\n",
            "  Downloading dash-2.13.0-py3-none-any.whl (10.4 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.4/10.4 MB\u001b[0m \u001b[31m88.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from jupyter-dash) (2.31.0)\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.10/dist-packages (from jupyter-dash) (2.2.5)\n",
            "Collecting retrying (from jupyter-dash)\n",
            "  Downloading retrying-1.3.4-py3-none-any.whl (11 kB)\n",
            "Requirement already satisfied: ipython in /usr/local/lib/python3.10/dist-packages (from jupyter-dash) (7.34.0)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.10/dist-packages (from jupyter-dash) (5.5.6)\n",
            "Collecting ansi2html (from jupyter-dash)\n",
            "  Downloading ansi2html-1.8.0-py3-none-any.whl (16 kB)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.10/dist-packages (from jupyter-dash) (1.5.8)\n",
            "Collecting Werkzeug<2.3.0 (from dash->jupyter-dash)\n",
            "  Downloading Werkzeug-2.2.3-py3-none-any.whl (233 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m233.6/233.6 kB\u001b[0m \u001b[31m28.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.10/dist-packages (from dash->jupyter-dash) (5.15.0)\n",
            "Collecting dash-html-components==2.0.0 (from dash->jupyter-dash)\n",
            "  Downloading dash_html_components-2.0.0-py3-none-any.whl (4.1 kB)\n",
            "Collecting dash-core-components==2.0.0 (from dash->jupyter-dash)\n",
            "  Downloading dash_core_components-2.0.0-py3-none-any.whl (3.8 kB)\n",
            "Collecting dash-table==5.0.0 (from dash->jupyter-dash)\n",
            "  Downloading dash_table-5.0.0-py3-none-any.whl (3.9 kB)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.10/dist-packages (from dash->jupyter-dash) (4.5.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from dash->jupyter-dash) (67.7.2)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from flask->jupyter-dash) (3.1.2)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from flask->jupyter-dash) (2.1.2)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from flask->jupyter-dash) (8.1.7)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.10/dist-packages (from ipykernel->jupyter-dash) (0.2.0)\n",
            "Requirement already satisfied: traitlets>=4.1.0 in /usr/local/lib/python3.10/dist-packages (from ipykernel->jupyter-dash) (5.7.1)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.10/dist-packages (from ipykernel->jupyter-dash) (6.1.12)\n",
            "Requirement already satisfied: tornado>=4.2 in /usr/local/lib/python3.10/dist-packages (from ipykernel->jupyter-dash) (6.3.2)\n",
            "Collecting jedi>=0.16 (from ipython->jupyter-dash)\n",
            "  Downloading jedi-0.19.1-py2.py3-none-any.whl (1.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.6/1.6 MB\u001b[0m \u001b[31m70.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: decorator in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (0.7.5)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (3.0.39)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (2.16.1)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (0.2.0)\n",
            "Requirement already satisfied: matplotlib-inline in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (0.1.6)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.10/dist-packages (from ipython->jupyter-dash) (4.8.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->jupyter-dash) (3.3.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->jupyter-dash) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->jupyter-dash) (2.0.6)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->jupyter-dash) (2023.7.22)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from retrying->jupyter-dash) (1.16.0)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.3 in /usr/local/lib/python3.10/dist-packages (from jedi>=0.16->ipython->jupyter-dash) (0.8.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from Jinja2>=3.0->flask->jupyter-dash) (2.1.3)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.10/dist-packages (from pexpect>4.3->ipython->jupyter-dash) (0.7.0)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from plotly>=5.0.0->dash->jupyter-dash) (8.2.3)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from plotly>=5.0.0->dash->jupyter-dash) (23.2)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.10/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython->jupyter-dash) (0.2.8)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from jupyter-client->ipykernel->jupyter-dash) (5.3.2)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.10/dist-packages (from jupyter-client->ipykernel->jupyter-dash) (23.2.1)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.10/dist-packages (from jupyter-client->ipykernel->jupyter-dash) (2.8.2)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.10/dist-packages (from jupyter-core>=4.6.0->jupyter-client->ipykernel->jupyter-dash) (3.11.0)\n",
            "Installing collected packages: dash-table, dash-html-components, dash-core-components, Werkzeug, retrying, jedi, ansi2html, dash, jupyter-dash\n",
            "  Attempting uninstall: Werkzeug\n",
            "    Found existing installation: Werkzeug 3.0.0\n",
            "    Uninstalling Werkzeug-3.0.0:\n",
            "      Successfully uninstalled Werkzeug-3.0.0\n",
            "Successfully installed Werkzeug-2.2.3 ansi2html-1.8.0 dash-2.13.0 dash-core-components-2.0.0 dash-html-components-2.0.0 dash-table-5.0.0 jedi-0.19.1 jupyter-dash-0.4.2 retrying-1.3.4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "RaG2JFZ1bEZW",
        "outputId": "dcf3aee6-373a-4b61-c9e4-2747b2fcbb25"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: zeep in /usr/local/lib/python3.10/dist-packages (4.2.1)\n",
            "Requirement already satisfied: attrs>=17.2.0 in /usr/local/lib/python3.10/dist-packages (from zeep) (23.1.0)\n",
            "Requirement already satisfied: isodate>=0.5.4 in /usr/local/lib/python3.10/dist-packages (from zeep) (0.6.1)\n",
            "Requirement already satisfied: lxml>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from zeep) (4.9.3)\n",
            "Requirement already satisfied: platformdirs>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from zeep) (3.10.0)\n",
            "Requirement already satisfied: requests>=2.7.0 in /usr/local/lib/python3.10/dist-packages (from zeep) (2.31.0)\n",
            "Requirement already satisfied: requests-toolbelt>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from zeep) (1.0.0)\n",
            "Requirement already satisfied: requests-file>=1.5.1 in /usr/local/lib/python3.10/dist-packages (from zeep) (1.5.1)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.10/dist-packages (from zeep) (2023.3.post1)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from isodate>=0.5.4->zeep) (1.16.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.7.0->zeep) (3.2.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.7.0->zeep) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.7.0->zeep) (2.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.7.0->zeep) (2023.7.22)\n"
          ]
        }
      ],
      "source": [
        "#1\n",
        "pip install zeep"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HWbXbheDbHwk"
      },
      "outputs": [],
      "source": [
        "#2\n",
        "import zeep"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VyPXJBpcVCha"
      },
      "outputs": [],
      "source": [
        "# 3\n",
        "import requests\n",
        "from bs4 import BeautifulSoup"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kVSZl4IEiMjd",
        "outputId": "a74f0595-26df-4d36-98ec-59c36268cc47"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "30.0 Celsius is equal to 86 Fahrenheit\n",
            "74.0 Fahrenheit is equal to 23.3333333333333 Celsius\n"
          ]
        }
      ],
      "source": [
        "wsdl_url1 = \"https://www.w3schools.com/xml/tempconvert.asmx?WSDL\"\n",
        "\n",
        "client = zeep.Client(wsdl_url1)\n",
        "\n",
        "celsius_temperature = 30.0\n",
        "fahrenheit_temperature = client.service.CelsiusToFahrenheit(celsius_temperature)\n",
        "print(f\"{celsius_temperature} Celsius is equal to {fahrenheit_temperature} Fahrenheit\")\n",
        "\n",
        "fahrenheit_temperature = 74.0\n",
        "celsius_temperature = client.service.FahrenheitToCelsius(fahrenheit_temperature)\n",
        "print(f\"{fahrenheit_temperature} Fahrenheit is equal to {celsius_temperature} Celsius\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ds-NfNHFCAA5"
      },
      "outputs": [],
      "source": [
        "#REDESIGN\n",
        "@anvil.server.callable\n",
        "def get_c(temp):\n",
        "  wsdl_url1 = \"https://www.w3schools.com/xml/tempconvert.asmx?WSDL\"\n",
        "  client1 = zeep.Client(wsdl_url1)\n",
        "\n",
        "  if 'F' in temp:\n",
        "    digits = []\n",
        "    for char in temp:\n",
        "      if char.isdigit():\n",
        "        digits += char\n",
        "    s = \"\".join(digits)\n",
        "    s = float(s)\n",
        "    fahrenheit_temperature = s\n",
        "    celsius_temperature = client1.service.FahrenheitToCelsius(fahrenheit_temperature)\n",
        "    res = int(round(float(celsius_temperature)))\n",
        "    return res"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "xs88vKW4DOVk"
      },
      "outputs": [],
      "source": [
        "#REDESIGN\n",
        "\n",
        "@anvil.server.callable\n",
        "def get_f(temp):\n",
        "  wsdl_url1 = \"https://www.w3schools.com/xml/tempconvert.asmx?WSDL\"\n",
        "  client1 = zeep.Client(wsdl_url1)\n",
        "\n",
        "  if 'C' in temp:\n",
        "      #result = anvil.server.call('get_c', self.temperature_label.text)\n",
        "      digits = []\n",
        "      for char in temp:\n",
        "        if char.isdigit():\n",
        "          digits += char\n",
        "      s = \"\".join(digits)\n",
        "      s = float(s)\n",
        "      fahrenheit_temperature = s\n",
        "      celsius_temperature = client1.service.CelsiusToFahrenheit(fahrenheit_temperature)\n",
        "      res = int(round(float(celsius_temperature)))\n",
        "      return res"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zeskFh0qbSBM",
        "outputId": "77c31e5d-fd19-41b7-a0ed-f6e4cd273780"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Country Name: Ukraine\n",
            "Capital City: Kiev\n",
            "Country info: {\n",
            "    'sISOCode': 'UA',\n",
            "    'sName': 'Ukraine',\n",
            "    'sCapitalCity': 'Kiev',\n",
            "    'sPhoneCode': '380',\n",
            "    'sContinentCode': 'EU',\n",
            "    'sCurrencyISOCode': 'UAH',\n",
            "    'sCountryFlag': 'http://www.oorsprong.org/WebSamples.CountryInfo/Flags/Ukraine.jpg',\n",
            "    'Languages': {\n",
            "        'tLanguage': [\n",
            "            {\n",
            "                'sISOCode': 'ukr',\n",
            "                'sName': 'Ukrainian'\n",
            "            }\n",
            "        ]\n",
            "    }\n",
            "}\n",
            "Welcome to the beautiful country of Ukraine ! \n",
            " Visit the capital city, a gorgeous  Kiev , \n",
            "  and spend local currency,  UAH  with fun! \n",
            " Also remember to learn some frases in local language,  \n",
            " Ukrainian , to have the most of experience!\n"
          ]
        }
      ],
      "source": [
        "#\n",
        "\n",
        "# Define the URL of the WSDL for the CountryInfoService\n",
        "wsdl_url = \"http://webservices.oorsprong.org/websamples.countryinfo/countryinfoservice.wso?WSDL\"\n",
        "\n",
        "client = zeep.Client(wsdl_url)\n",
        "\n",
        "# Call the FullCountryInfo operation with a country code (e.g., 'USA')\n",
        "country_code = 'UA'\n",
        "country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "country_name = country_info.sName\n",
        "capital_city = country_info.sCapitalCity\n",
        "\n",
        "languages = country_info.Languages\n",
        "for language in languages.tLanguage:\n",
        "    language_name = language.sName\n",
        "\n",
        "print(f\"Country Name: {country_name}\")\n",
        "print(f\"Capital City: {capital_city}\")\n",
        "print(f\"Country info: {country_info}\")\n",
        "print(\"Welcome to the beautiful country of\", country_info.sName, \"!\", '\\n',\n",
        "      \"Visit the capital city, a gorgeous \", country_info.sCapitalCity,\n",
        "      \",\", '\\n', \" and spend local currency, \", country_info.sCurrencyISOCode, \" with fun!\",\n",
        "      '\\n', \"Also remember to learn some frases in local language, \", '\\n',\n",
        "      language_name, \", to have the most of experience!\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 461
        },
        "id": "SuaTE4MyaXx3",
        "outputId": "abf64e7b-7e3c-46ba-e26e-a15361aa6ae6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Collecting anvil-uplink\n",
            "  Downloading anvil_uplink-0.4.2-py2.py3-none-any.whl (90 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m90.1/90.1 kB\u001b[0m \u001b[31m1.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting argparse (from anvil-uplink)\n",
            "  Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.10/dist-packages (from anvil-uplink) (0.18.3)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from anvil-uplink) (1.16.0)\n",
            "Collecting ws4py (from anvil-uplink)\n",
            "  Downloading ws4py-0.5.1.tar.gz (51 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m51.4/51.4 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Building wheels for collected packages: ws4py\n",
            "  Building wheel for ws4py (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ws4py: filename=ws4py-0.5.1-py3-none-any.whl size=45228 sha256=5ddfb1a72d2265c6e389237d5b199f009cfdb1dd0bc27fe15c3089c04681638d\n",
            "  Stored in directory: /root/.cache/pip/wheels/2e/7c/ad/d9c746276bf024d44296340869fcb169f1e5d80fb147351a57\n",
            "Successfully built ws4py\n",
            "Installing collected packages: ws4py, argparse, anvil-uplink\n",
            "Successfully installed anvil-uplink-0.4.2 argparse-1.4.0 ws4py-0.5.1\n"
          ]
        },
        {
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "argparse",
                  "google"
                ]
              }
            }
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "#4\n",
        "!pip install anvil-uplink"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J7lME3Ryaeqr"
      },
      "outputs": [],
      "source": [
        "#5\n",
        "import anvil.server"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I69nPy21aiw9",
        "outputId": "4b2da8db-5ac2-4e00-f0a6-62200a0cf391"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Connecting to wss://anvil.works/uplink\n",
            "Anvil websocket open\n",
            "Connected to \"Default Environment\" as SERVER\n"
          ]
        }
      ],
      "source": [
        "#6\n",
        "anvil.server.connect(\"server_NFP3KMKGPWVAXG2IGFTSPU4F-C4PB5CTMNPRFX52D\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vFmgXgMSamYG"
      },
      "outputs": [],
      "source": [
        "@anvil.server.callable\n",
        "def get_info(country_name):\n",
        "  country_code = client.service.CountryISOCode(country_name)\n",
        "  country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "  languages = country_info.Languages\n",
        "  for language in languages.tLanguage:\n",
        "    language_name = language.sName\n",
        "\n",
        "  result = (\"Welcome to the beautiful country of\" + country_info.sName + \"!\" + '\\n' +\n",
        "      \"Visit the capital city, a gorgeous \" + country_info.sCapitalCity +\n",
        "      \",\" + '\\n' + \" and spend local currency, \" + country_info.sCurrencyISOCode + \", with fun!\" +\n",
        "      '\\n' + \"Also remember to learn some frases in local language, \" + '\\n' +\n",
        "      language_name + \", to have the most of experience!\")\n",
        "  return result"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f4AiLMmXiGui"
      },
      "outputs": [],
      "source": [
        "#7\n",
        "@anvil.server.callable\n",
        "def get_weather(country_name):\n",
        "  country_code = client.service.CountryISOCode(country_name)\n",
        "  country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "  capital_city = country_info.sCapitalCity\n",
        "\n",
        "  city = capital_city\n",
        "  url = \"https://www.google.com/search?q=\"+\"weather\"+city\n",
        "\n",
        "  html = requests.get(url).content\n",
        "\n",
        "  soup = BeautifulSoup(html, 'html.parser')\n",
        "\n",
        "  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})\n",
        "  if temp_element:\n",
        "    temp = temp_element.text\n",
        "  else:\n",
        "      temp = \"Temperature not found\"\n",
        "\n",
        "  str_element = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})\n",
        "  if str_element:\n",
        "      str = str_element.text\n",
        "      data = str.split('\\n')\n",
        "      if len(data) >= 2:\n",
        "          time = data[0]\n",
        "          sky = data[1]\n",
        "      else:\n",
        "          time = \"Time not found\"\n",
        "          sky = \"Sky description not found\"\n",
        "  else:\n",
        "      time = \"Time and sky description not found\"\n",
        "\n",
        "  listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})\n",
        "\n",
        "  strd = listdiv[5].text\n",
        "\n",
        "  pos = strd.find('Wind')\n",
        "  other_data = strd[pos:]\n",
        "\n",
        "  result = (\"Capital: \" + capital_city + '\\n' +\n",
        "            \"Time: \" + time + '\\n' +\n",
        "            \"Temperature: \" + temp + '\\n' +\n",
        "            \"Sky State: \" + sky + '\\n' +\n",
        "            \"Secondary data: \" + other_data)\n",
        "  return result"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "umrnQ664DqjH"
      },
      "outputs": [],
      "source": [
        "@anvil.server.callable\n",
        "def get_temp(country_name):\n",
        "  country_code = client.service.CountryISOCode(country_name)\n",
        "  country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "  capital_city = country_info.sCapitalCity\n",
        "\n",
        "  city = capital_city\n",
        "  url = \"https://www.google.com/search?q=\"+\"weather\"+city\n",
        "\n",
        "  html = requests.get(url).content\n",
        "\n",
        "  soup = BeautifulSoup(html, 'html.parser')\n",
        "\n",
        "  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})\n",
        "  if temp_element:\n",
        "    temp = temp_element.text\n",
        "  else:\n",
        "      temp = \"Temperature not found\"\n",
        "\n",
        "  return temp"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W_uXk7eoETLh",
        "outputId": "d38561cc-c5aa-4231-d56f-584d557e8ba1"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "23"
            ]
          },
          "execution_count": 64,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "temp = '74F'\n",
        "get_c = get_c(temp)\n",
        "get_c"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "id": "nCoF3lekaze9",
        "outputId": "4bb80977-ad87-435f-b6a8-c483b9c7e116"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n"
          ]
        },
        {
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-25-95cac3476493>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0manvil\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwait_forever\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/anvil/server.py\u001b[0m in \u001b[0;36mwait_forever\u001b[0;34m()\u001b[0m\n\u001b[1;32m    435\u001b[0m     \u001b[0m_get_connection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    436\u001b[0m     \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 437\u001b[0;31m         \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ],
      "source": [
        "anvil.server.wait_forever()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mjKdu7_2Fq7o",
        "outputId": "b3ce0310-990a-41fc-c674-e826abb5c636"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.soap:Forcing soap:address location to HTTPS\n",
            "WARNING:zeep.wsdl.bindings.http:Forcing http:address location to HTTPS\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "73"
            ]
          },
          "execution_count": 66,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "temp = '23C'\n",
        "get_f = get_f(temp)\n",
        "get_f"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4gJjZ-QPDuB_"
      },
      "outputs": [],
      "source": [
        "@anvil.server.callable\n",
        "def get_c(country_name):\n",
        "  country_code = client.service.CountryISOCode(country_name)\n",
        "  country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "  capital_city = country_info.sCapitalCity\n",
        "\n",
        "  city = capital_city\n",
        "  url = \"https://www.google.com/search?q=\"+\"weather\"+city\n",
        "\n",
        "  html = requests.get(url).content\n",
        "\n",
        "  soup = BeautifulSoup(html, 'html.parser')\n",
        "\n",
        "  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})\n",
        "  if temp_element:\n",
        "    temp = temp_element.text\n",
        "  else:\n",
        "      temp = \"Temperature not found\"  # Handle the case when temperature is not found\n",
        "\n",
        "  wsdl_url1 = \"https://www.w3schools.com/xml/tempconvert.asmx?WSDL\"\n",
        "  client1 = zeep.Client(wsdl_url1)\n",
        "\n",
        "  if 'C' in temp:\n",
        "    digits = []\n",
        "    for char in temp:\n",
        "      if char.isdigit():\n",
        "        digits += char\n",
        "    s = \"\".join(digits)\n",
        "    s = float(s)\n",
        "    fahrenheit_temperature = s\n",
        "    celsius_temperature = client1.service.FahrenheitToCelsius(fahrenheit_temperature)\n",
        "    res = celsius_temperature\n",
        "    return res"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rf1wpTm-Dvxv"
      },
      "outputs": [],
      "source": [
        "@anvil.server.callable\n",
        "def get_f(country_name):\n",
        "  country_code = client.service.CountryISOCode(country_name)\n",
        "  country_info = client.service.FullCountryInfo(country_code)\n",
        "\n",
        "  # Access specific information about the country\n",
        "  capital_city = country_info.sCapitalCity\n",
        "\n",
        "  city = capital_city\n",
        "\n",
        "  url = \"https://www.google.com/search?q=\"+\"weather\"+city\n",
        "\n",
        "\n",
        "  html = requests.get(url).content\n",
        "\n",
        "\n",
        "  soup = BeautifulSoup(html, 'html.parser')\n",
        "\n",
        "  temp_element = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})\n",
        "  if temp_element:\n",
        "    temp = temp_element.text\n",
        "  else:\n",
        "      temp = \"Temperature not found\"\n",
        "\n",
        "  wsdl_url1 = \"https://www.w3schools.com/xml/tempconvert.asmx?WSDL\"\n",
        "\n",
        "  client1 = zeep.Client(wsdl_url1)\n",
        "\n",
        "  if 'F' in temp:\n",
        "      #result = anvil.server.call('get_c', self.temperature_label.text)\n",
        "      digits = []\n",
        "      for char in temp:\n",
        "        if char.isdigit():\n",
        "          digits += char\n",
        "      s = \"\".join(digits)\n",
        "      s = float(s)\n",
        "      fahrenheit_temperature = s\n",
        "      celsius_temperature = client1.service.CelsiusToFahrenheit(fahrenheit_temperature)\n",
        "      res = celsius_temperature\n",
        "      return res\n",
        "\n",
        "  #celsius_temperature = temp  # Replace with your desired temperature in Celsius\n",
        "  #fahrenheit_temperature = client1.service.CelsiusToFahrenheit(celsius_temperature)\n",
        "  #res = (fahrenheit_temperature + \"°F\")\n",
        "  #return res"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
