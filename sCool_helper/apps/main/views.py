from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache


def main(request):
    context = {"login": cache.get("login")}
    return render(request, r'main\main.html', context)
