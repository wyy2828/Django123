from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    主页视图
    """
    return render(request, 'home.html', {
        'title': '欢迎来到我的Django网站',
        'message': '这是一个使用Django框架构建的网站。'
    })