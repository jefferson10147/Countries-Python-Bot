import requests
from emoji_flags import flags


def get_country_by_flag(emoji):
    if emoji in flags.keys():
        country_name = flags[emoji]
        url = f'https://restcountries.eu/rest/v2/name/{country_name}?fullText=true'
        response = requests.get(url)

        if response.status_code == 200:
            obj = response.json()
            #print(obj[0])
    else:
        raise NameError('No country related to that emoji...')


    #get_country_by_flag('')