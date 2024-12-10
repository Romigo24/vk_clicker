import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv


def get_shorten_link(token, link):
    url = 'https://api.vk.ru/method/utils.getShortLink'
    params = {
        'url': link,
        'access_token': token,
        'v': '5.199'
    }
    response = requests.get(url, params)
    response.raise_for_status()
    short_link = response.json()['response']['short_url']
    return short_link


def count_clicks(token, link):
    key_link = urlparse(link).path.split('/')[-1]
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    params = {
        'key': key_link,
        'access_token': token,
        'interval': 'forever',
        'v': '5.199'
    }
    response = requests.get(url, params)
    response.raise_for_status()
    number_of_clicks = response.json()['response']['stats'][0]['views']
    return number_of_clicks


def is_shorten_link(token, link):
    key_link = urlparse(link).path.split('/')[-1]
    url = "https://api.vk.com/method/utils.getLinkStats"
    params = {
        'key': key_link,
        'access_token': token,
        'interval': 'forever',
        'v': '5.199'
    }
    response = requests.get(url, params=params)
    if response.ok:
        api_answer = response.json()
        if 'response' in api_answer:
            return True
        else:
            return False
 
  
def main():
    load_dotenv()
    token = os.environ['VK_API_KEY']
    link = input('Введите ссылку: ')
    if is_shorten_link(token, link):
        print(count_clicks(token, link))
    else:
        print(get_shorten_link(token, link))


if __name__ == '__main__':
    main()