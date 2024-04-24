import requests # библиотека для взаимодействия с веб-сервисами и выполнения запросов к веб-страницам
from bs4 import BeautifulSoup as BS, \
    BeautifulSoup  # библиотека bs4 и ее класс BeautifulSoup производит синтаксический анализ



# функция для получения html код страницы
def get_html(url):
    r = requests.get(url)
    # print(type(r)) # type - показывает какого типа объект, типа Response в данном случае
    # print(dir(r))  # dir - показывает список всех атрибутов объекта (r), это свойства, методы
    # # например воспользуемся свойством status_code, возвращает код ответа сервера типа 200(все хорошо)
    # # или вернет 403(доступ запрещен) 404 405 503(внутр ошибка сервера ) и т.п.
    # print(r.status_code)
    # print(r.ok) # True или False - ответ сервера
    # print(r.text) # свойство text - выдаст весь html код страницы
    return r.text

def get_data(html):
    s = BeautifulSoup(html, 'lxml')
    tr = s.find('table').find_all('b')
    return tr


def main():
    # Начальный URL
    url = 'http://old.zip-2002.ru/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()




















    # while url:
    #     response = requests.get(url)
    #     soup = BS(response.text, 'lxml')
    #
    #     divs_obolochka = soup.find_all('div', class_='obolochka')
    #     print(len(divs_obolochka))
    #     for div_obolochka in divs_obolochka:
    #         divs_detshow = div_obolochka.find_all('div', class_='detshow')
    #         for div_detshow in divs_detshow:
    #             span = div_detshow.find('span', class_='nazvan')
    #             if span:
    #                 print(span.text.strip())
    #
    #     # Пытаемся получить URL следующей страницы
    #     url = get_next_page_url(soup)


# def get_next_page_url(soup):
#     next_page_button = soup.find('a', string='Далее')
#     if next_page_button and 'href' in next_page_button.attrs:
#         return next_page_button['href']
#     return None
#
