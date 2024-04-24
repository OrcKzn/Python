from bs4 import BeautifulSoup as BS
import requests


def get_next_page_url(soup):
    """Получение URL следующей страницы или None, если таковой нет."""
    next_page_button = soup.find('a', string='Далее')
    if next_page_button and 'href' in next_page_button.attrs:
        return next_page_button['href']
    return None


def process_page(url):
    """Обработка одной страницы и извлечение данных."""
    while url:
        response = requests.get(url)
        soup = BS(response.text, 'lxml')

        divs_obolochka = soup.find_all('div', class_='obolochka')
        print(len(divs_obolochka))
        # for div_obolochka in divs_obolochka:
        #     divs_detshow = div_obolochka.find_all('div', class_='detshow')
        #     for div_detshow in divs_detshow:
        #         span = div_detshow.find('span', class_='nazvan')
        #         if span:
        #             print(span.text.strip())

        # Пытаемся получить URL следующей страницы
        url = get_next_page_url(soup)


# Начальный URL
start_url = 'http://old.zip-2002.ru/akusticheskie_komponenty/dinamiki/'
process_page(start_url)
