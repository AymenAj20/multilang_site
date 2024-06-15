from django.urls import path
from .views import article_list, chatbot_view, set_language_view

urlpatterns = [
    path('article-list/', article_list, name="article-list"),
    path('set-language/', set_language_view, name='set_language'),
    path('chatbot_view/', chatbot_view, name='chatbot_view'),
]