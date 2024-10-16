from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name='news'),
    path('category/<int:pk>', views.category_news_page)

]