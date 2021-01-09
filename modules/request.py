import requests


def get_country_by_name(country_name):
    url = f'https://restcountries.eu/rest/v2/name/{country_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        country = response.json()[0]
        country_facts = f"Country: {country['name']}\nNative name: {country['nativeName']}\nCapital: {country['capital']}\nRegion: {country['region']}\nSub-Region: {country['subregion']}\nDemonym: {country['demonym']}\nLanguages:"
        
        for language in country['languages']:
            country_facts = ' '.join([country_facts,language['name']])
        
        if country['borders']:
            country_facts = '\n'.join([country_facts,'Borders:'])
            for border in country['borders']:
                country_facts = ' '.join([country_facts,border])

        country_facts = ' '.join([country_facts,'\nSee the flag:',country['flag']])
        return country_facts