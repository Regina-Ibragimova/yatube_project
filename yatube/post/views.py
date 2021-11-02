from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Самая лучшая блогерская социальная сеть! Welcome, друг!')


def group_list(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_post(request, slug):
    return HttpResponse(f'Название группы {slug}')