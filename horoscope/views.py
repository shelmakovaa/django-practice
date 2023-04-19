from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

elements = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

zodiac_dates = {3: {(1, 20): 'pieces', (21, 31): 'aries'},
                4: {(1, 20): 'aries', (21, 30): 'taurus'},
                5: {(1, 21): 'taurus', (22, 31): 'gemini'},
                6: {(1, 21): 'gemini', (22, 30): 'cancer'},
                7: {(1, 22): 'cancer', (23, 31): 'leo'},
                8: {(1, 21): 'leo', (22, 31): 'virgo'},
                9: {(1, 23): 'virgo', (24, 30): 'libra'},
                10: {(1, 23): 'libra', (24, 31): 'scorpio'},
                11: {(1, 22): 'scorpio', (23, 30): 'sagittarius'},
                12: {(1, 22): 'sagittarius', (23, 31): 'capricorn'},
                1: {(1, 20): 'capricorn', (21, 31): 'aquarius'},
                2: {(1, 19): 'aquarius', (20, 28): 'pisces'}
                }


def date(request, day: int, month: int):
    zodiac_month = list(zodiac_dates.get(month))
    for start, stop in zodiac_month:
        if day in range(start, stop+1):
            temp = zodiac_dates[month][(start, stop)]
            redirect_path = reverse('horoscope-name', args=(temp,))
            return HttpResponseRedirect(redirect_path)
    return HttpResponseNotFound("Страница не найдена")


def zodiac_type(request):
    types = list(elements)
    temp = ''
    for elem in types:
        redirect_path = reverse('zodiac_elem', args=(elem,))
        temp += f"<li><h3> <a href='{redirect_path}'>{elem.title()}</a></h3></li>"
    temp = f"""
        <ul>{temp}</ul>
    """
    return HttpResponse(temp)


def get_elements(request, element: str):
    if not elements.get(element):
        return HttpResponseNotFound("Страница не найдена")
    response = ""
    for i in elements[element]:
        redirect_path = reverse('horoscope-name', args=(i,))
        response += f"<li><h3> <a href='{redirect_path}'>{i.title()}</a> </h3></li>"
    response = f"""<ul>{response}</ul>"""
    return HttpResponse(response)


def index(request):
    zodiacs = list(zodiac_dict)
    """
    <ol>
        <li>aries</li>
    </ol>
    """
    li_elements = ''
    for elem in zodiacs:
        redirect_path = reverse('horoscope-name', args=(elem,))
        li_elements += f"<li> <a href='{redirect_path}'>{elem.title()}</a> </li>"

    response = f"""
    <ol>
    {li_elements}
    </ol>
    """
    return HttpResponse(response)


def get_info_about_zodiac(request, sign_zodiac: str):
    # description = zodiac_dict.get(sign_zodiac)
    response = render_to_string('horoscope/info_zodiac.html')
    # if description:
    #     return HttpResponse(description)
    # else:
    #     return HttpResponseNotFound('Page not found')
    return HttpResponse(response)


def get_info_about_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac < 1 or sign_zodiac > len(zodiac_dict):
        return HttpResponseNotFound('Page not found')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
