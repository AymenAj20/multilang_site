from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.i18n import set_language
from django.http import HttpResponse


# Create your views here.

@api_view(['GET'])
def article_list(request):
    articles = [{"title": "Article 1", "content": "Content of article 1"}, 
                {"title": "Article 2", "content": "Content of article 2"}]
    return render(request, 'article_list.html', {'articles': articles})


def set_language_view(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            response = set_language(request)
            # Vous pouvez ajouter un comportement supplémentaire ici après le changement de langue si nécessaire
            return response
    # Gérer le cas où la méthode HTTP n'est pas POST ou si language est manquant
    return HttpResponse(status=400) 