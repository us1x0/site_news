from django.shortcuts import render
from .models import News, OptionsNews

# Create your views here.
def home_page(request):
    types_of_news = News.objects.all()
    context = {'typesOfnews':types_of_news}
    return render(request, 'home.html', context)

def news_today(request):
    all_options_news = OptionsNews.objects.all()
    context = {'all_options_news': all_options_news}
    return render(request, "news_page.html", context)



def contacts(request):
    return render(request, 'contacts.html')
