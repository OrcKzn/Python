import requests # библиотека для взаимодействия с веб-сервисами и выполнения запросов к веб-страницам
from bs4 import BeautifulSoup as BS # библиотека bs4 и ее класс BeautifulSoup производит синтаксический анализ

def get_next_page_url(soup):
    """Получение URL следующей страницы или None, если таковой нет."""
    next_page_button = soup.find('a', text='Далее')
    if next_page_button and 'href' in next_page_button.attrs:
        return next_page_button['href']
    return None

def get_html(url):
    # response(переменная принимающая ответ с сервера) = requests.get(url) используем метод get (метод запроса, получение)
    # url - локальная переменная содержащая адрес сайта, строка
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    elif r.status_code == 404:
        return "Ошибка 404: Ресурс не найден."
    elif r.status_code == 403:
        return "Ошибка 403: Доступ запрещён."
    elif r.status_code == 500:
        return "Ошибка 500: Внутренняя ошибка сервера."
    elif r.status_code == 502:
        return "Ошибка 502: Ошибка шлюза."
    else:
        return f"Необработанный статус-код: {r.status_code}"
    # type(r) - функиця type показывает что "r" это объект Responce библиотеки requests
    # dir(r) - получим список всех атрибутов этого объекта, это свойства методы.
    # Например:
    # r.status_code - возвращает цифру 200 и т.д.
    # r.ok - возвращает булевую True если связь есть
    # r.text - возвращает текст html страницы


def get_data(html):
    # Создаем объект BeautifulSoup, передавая HTML-контент и имя парсера
    soup = BS(html, 'lxml')  # Используем парсер lxml

    ul = soup.find_all('ul', class_="gnm")[0]
    li = ul.find_all('li')[0]




    soup1 = BS(requests.get('http://old.zip-2002.ru/akusticheskie_komponenty/dinamiki/').text, 'lxml')
    divs_obolochka = soup1.find_all('div', class_='obolochka')
    for div_obolochka in divs_obolochka:
        divs_detshow = div_obolochka.find_all('div', class_='detshow')
        for div_detshow in divs_detshow:
            span = div_detshow.find('span', class_='nazvan')
            if span:
                print(span.text.strip())



    # for i in div:
    #     name = i.find('alt').text
    #     urls = i.find('img').get('src')
    #     print(name)
    # print(type(t))
    # print(dir(t))
    # print(len(t))
    # print(p)
    # print(len(p))

    # return t



def main():
    url = 'http://old.zip-2002.ru/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()