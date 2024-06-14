from django.urls import path
from .views import article_list, set_language_view

urlpatterns = [
    path('article-list/', article_list, name="article-list"),
    path('set-language/', set_language_view, name='set_language'),
]