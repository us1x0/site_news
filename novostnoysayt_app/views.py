from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
def news_today(request):
    return render(request, "news_page.html")

def contacts(request):
    return render(request, 'contacts.html')
