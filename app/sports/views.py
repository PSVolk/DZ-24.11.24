from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime
import time
import math

from .form import UserForm, PrimeNumbersForm



def index(request):
    template = loader.get_template("sports/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))


def sport(request, sport_name):
    template = loader.get_template("sports/sport.html")
    d = {'text': f'Новости {sport_name}'}
    context = get_context(sport_name, d)
    return HttpResponse(template.render(context, request))


def daytime(request):
    template = loader.get_template("sports/daytime.html")
    if datetime.datetime.now().time().hour <= 6:
        text = 'Доброй ночи'
    elif datetime.datetime.now().time().hour <= 12:
        text = 'Доброе утро'
    elif datetime.datetime.now().time().hour <= 18:
        text = 'Добрый день'
    else:
        text = 'Добрый вечер'

    t = {'time': time.strftime("%H:%M:%S", time.localtime()),
         'daytime': text}
    context = get_context('Время', t)
    return HttpResponse(template.render(context, request))

def user_age(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        u = {'name': name, 'age': age}
        content = get_context('Пользователь', u)
    else:
        userform = UserForm()
        content = get_context('Пользователь', {"form": userform})
    return render(request, "user.html", content)

def prime(request):
    if request.method == "POST":
        start = int(request.POST.get("start"))
        stop = int(request.POST.get("stop"))
        u = {'numbers': [n for n in range(start, stop+1) if is_prime(n)]}
        content = get_context('Простые числа', u)
    else:
        userform = PrimeNumbersForm()
        content = get_context('Простые числа', {"form": userform})
    return render(request, "prime.html", content)


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),
                         ('basketball/', 'Баскетбол'),
                         ('hockey/', 'Хоккей'),
                         ('daytime/', 'Время'),
                         ('user_age/', 'Пользователь'),
                         ('prime/', 'Простые числа')
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context

def is_prime(number):
    # список простых чисел начинается с 2, всё остальное можно сразу отмести
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители.
    for element in divisors:
        if number % element == 0:
            return False
    return True