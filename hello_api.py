import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

def shorten_link(token, link):
    url = 'https://api.vk.ru/method/utils.getShortLink'
    params = {
        'url': link,
        'access_token': token,
        'v': '5.199'
    }
    response = requests.get(url, params)
    response.raise_for_status()
    try:
        short_link = response.json()['response']['short_url']
    except KeyError:
        return response.text
        SystemExit
    return short_link


def count_clicks(token, link):
    u = urlparse(link).path.split('/')[-1]
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    params = {
        'key': u,
        'access_token': token,
        'interval': 'week',
        'v': '5.199'
    }
    response = requests.get(url, params)
    response.raise_for_status()
    return response.text


def is_shorten_link(link):
    url = urlparse(link)
    shortened_netloc = ['vk.cc']
    if url.netloc in shortened_netloc:
        return count_clicks(token, link)
    else:
        return shorten_link(token, link)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['VK_API_KEY']
    link = input('Введите ссылку: ')
    print(is_shorten_link(link))