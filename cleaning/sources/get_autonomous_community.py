import requests
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Anexo:Comunidades_y_ciudades_aut%C3%B3nomas_de_Espa%C3%B1a'

def scrape_autonomous_community(url:str):
    '''
    Get autonomous community from wikipedia, given the url 
    https://es.wikipedia.org/wiki/Anexo:Comunidades_y_ciudades_aut%C3%B3nomas_de_Espa%C3%B1a
    '''
    url_call = requests.get(url)
    soup_obj = BeautifulSoup(url_call.text, features="lxml")
    scrape_data = soup_obj.select('tbody')
    return scrape_data[0].text.strip().split('\n')

def clean_autonomous_community(scrape_data:list):
    result = []
    for string in scrape_data:
        if string != '':
            if '\xa0' in string:
                until = string.index('\xa0')
                string = string[:until]
            if '.' in string:
                until = string.index('.')
                string = string[:until]
            result.append(string.replace('&', ''))
    return result

def clean_number_format(scrape_data:list):
    for i,string in enumerate(scrape_data):
        scrape_data[i] = string.replace(',','.')
        if string[0] == '0' and string[1] != '.':
            scrape_data[i] = string[1:]
    return scrape_data
