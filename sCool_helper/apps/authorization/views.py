from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.cache import cache

import sqlite3


def main(request):
    submitbutton = request.POST.get("submit")
    log = request.POST.get("login")
    password = request.POST.get("password")

    if log is None:
        log = ''
    if password is None:
        password = ''

    if submitbutton is not None:
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        print(log)
        result = cur.execute(f"""SELECT * FROM main_user""").fetchall()

        for elem in result:
            if elem[1] == log and elem[2] == password:
                cache.set('login', log)
                return redirect('/main')
            else:
                pass

    context = {
        "login": log,
        "password": password,
        'submitbutton': submitbutton,
    }
    return render(request, r'authorization\auth.html', context)
