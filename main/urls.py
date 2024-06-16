from django.urls import path
from .views import api_links_view, article_list, chatbot_view, set_language_view , search_view

urlpatterns = [
    path('article-list/', article_list, name="article-list"),
    path('set-language/', set_language_view, name='set_language'),
    path('chatbot_view/', chatbot_view, name='chatbot_view'),
    path('search/', search_view, name='search_view'),
    path('', api_links_view, name='api_links'),
]