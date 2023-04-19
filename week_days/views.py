from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!',}


def todo(request, day: str):
    week_day = dic_week_day.get(day)
    if week_day:
        return HttpResponse(week_day)
    return HttpResponseNotFound(f"Нет такого дня недели - {day}")


def todo_number(request, day: int):
    days = list(dic_week_day)
    if 0 < day < 8:
        day_number = days[day-1]
        redirect_url = reverse('day-name', args=(day_number,))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f"Нет такого дня недели - {day}")


def start_page(request):
    return render(request, 'week_days/greeting.html')
