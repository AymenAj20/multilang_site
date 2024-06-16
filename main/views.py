from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.i18n import set_language
from django.http import HttpResponse, JsonResponse

from .models import Article

import openai, os
from dotenv import load_dotenv
load_dotenv() 
api_key = os.getenv("OPENAI_API_KEY" , None)

# Create your views here.

@api_view(['GET'])
def api_links_view(request):
    api_links = [
        {"name": "Article List", "url": "/article-list/"},
        {"name": "Set Language", "url": "/set-language/"},
        {"name": "Chatbot View", "url": "/chatbot_view/"},
        {"name": "Search View", "url": "/search/"}
    ]
    return JsonResponse(api_links, safe=False)

# Méthode qui retourne les deux articles  
@api_view(['GET'])
def article_list(request):
    articles = [
        {"title": "Article 1", "content": "Content of article 1", "publication_date": "2024-06-01"},
        {"title": "Article 2", "content": "Content of article 2", "publication_date": "2024-06-15"}
    ]
    return render(request, 'article_list.html', {'articles': articles})

# Méthode qui fait la traduction des éléments statiques du site   
def set_language_view(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            response = set_language(request)
            
            return response
    # Gérer les erreurs ( si la méthode n'est pas POST )
    return HttpResponse(status=400) 


# Méthode qui envoie les requêtes avec les questions des utilisateurs a l'API de GPT   
def chatbot_view(request):
    chatbot_response = None
    # print(api_key)
    # Vérification si la méthode de la requête est POST et une clé API est disponible
    if api_key is not None and request.method == 'POST':
        print("I am in")
        # Clé API pour OpenAI
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        # Création de la requête pour GPT
        response = openai.Completion.create(
            engine ='gpt-3.5-turbo-instruct',
            prompt = prompt,
            maw_tokens = 265,
            temperature = 0.5
        )
        
        chatbot_response = response['choices'][0]['text']
        # Afficher la réponse de GPT dans la page chatbot.html
    return render(request, 'chatbot.html',{"response":chatbot_response})

# Méthode de recherche des articles   
def search_view(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(content__icontains=query)

    augmented_results = []
    # Vérification si on a une requête et une clé API est disponible
    if query and api_key:
        # Clé API pour OpenAI
        openai.api_key = api_key
        documents = "\n".join([article.content for article in articles])
        # Création de la requête pour GPT
        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=f"Find articles related to: {query}\nDocuments:\n{documents}",
            max_tokens=100,
            temperature=0.5
        )
        augmented_results = response['choices'][0]['text'].strip().split('\n')

    # Rendre la page avec les résultats trouvés 
    return render(request, 'base.html', {'query': query, 'articles': articles, 'augmented_results': augmented_results})