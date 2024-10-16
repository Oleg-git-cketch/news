from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import NewsCategory, News

def news_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'news.html', context)

def category_news_page(request):
    return render(request, 'category.html')
