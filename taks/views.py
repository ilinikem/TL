from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import downloader, User
import requests


def index(request):
    jsonData_list = downloader.objects.order_by('id').all()
    count_list = downloader.objects.all().count()
    paginator = Paginator(jsonData_list, 100)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(
        request,
        'index.html',
        {'page': page,
         'paginator': paginator,
         'count_list': count_list,
        }
    )


def download_posts(request):
    downloader.objects.all().delete()
    response = requests.get('http://jsonplaceholder.typicode.com/users').json()
    response2 = requests.get('http://jsonplaceholder.typicode.com/posts').json()
    for i in range(len(response)):
        if not User.objects.all().filter(name=response[i]['name']).exists():
            User.objects.create(name=response[i]['name'],
                                username=response[i]['username'],
                                email=response[i]['email'],
                                address=response[i]['address'],
                                phone=response[i]['phone'],
                                website=response[i]['website'],
                                company=response[i]['company'],
                                )
        for post in range(len(response2)):
            if response[i]['id'] == response2[post]['userId']:
                downloader.objects.create(name=User.objects.get(name=response[i]['name']),
                                          topic=response2[post]['title'],
                                          text=response2[post]['body'],
                                          )
    return redirect('index')
