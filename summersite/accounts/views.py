from django.shortcuts import render

def base(request):
    return render(request, "base.html", {})

def home_page(request):
    return render(request, "home_page.html", {})

def join(request):
    return render(request, "join.html", {})
