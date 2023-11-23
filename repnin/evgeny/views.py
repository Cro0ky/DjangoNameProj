from django.shortcuts import render
from django.http import HttpResponse


def info(request, fio, age, hobby):
    return HttpResponse(f'<h1> Имя {fio} <br> {age} лет <br>Интересы: {hobby}</h1>')


def about(request, town, ball, teaching):
    return HttpResponse(f'<h1>Я из города {town}<br>Балл отестата {ball}<br>{teaching} учться</h1>')


def contacts(request, github, tg, phone):
    return HttpResponse(f'<h1>GitHub: {github}<br>Tg: {tg}<br>Phone: {phone}</h1>')
