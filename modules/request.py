import requests
from modules.countries_alpha_code import countries_code
from modules.emoji_flags import flags


def get_country_by_name(country_name):
    url = f'https://restcountries.eu/rest/v2/name/{country_name}'
    response = requests.get(url)

    if response.status_code == 200:
        country = response.json()[0]
        country_facts = f"Country: {country['name']}\nNative name: {country['nativeName']}\nCapital: {country['capital']}\nRegion: {country['region']}\nSub-Region: {country['subregion']}\nDemonym: {country['demonym']}\nLanguages:"

        for language in country['languages']:
            country_facts = ' '.join([country_facts, language['name']])

        if country['borders']:
            country_facts = '\n'.join([country_facts, 'Borders:'])
            for border in country['borders']:
                country_facts = ' '.join([country_facts, border])

        country_facts = ' '.join([
            country_facts, '\nSee the flag:',
            country['flag']
        ])
        return country_facts


def translate_text_into_flags(text):
    i = 0
    translate_text = ''

    while i < len(text):

        if i + 1 < len(text):
            code = text[i] + text[i + 1]

            if code.upper() in countries_code.keys():
                country_name = countries_code[code.upper()]

                for key, country in flags.items():
                    if country == country_name:
                        translate_text += key

                i += 2
                continue

        translate_text += text[i]
        i += 1

    return translate_text


def translate_flags_into_text(text):
    i = 0
    translated_text = ''

    while i < len(text):

        if i + 1 < len(text):
            flag = text[i] + text[i + 1]

            if flag.upper() in flags.keys():
                country_name = flags[flag]

                for key, country in countries_code.items():
                    if country_name == country:
                        translated_text += key.lower()
                        break

                i += 2
                continue

        translated_text += text[i]
        i += 1

    return translated_text
