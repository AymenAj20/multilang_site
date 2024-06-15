from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.i18n import set_language
from django.http import HttpResponse, JsonResponse

import openai, os
from dotenv import load_dotenv
load_dotenv() 
api_key = os.getenv("OPENAI_API_KEY" , None)

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

def chatbot_view(request):
    chatbot_response = None
    print(api_key)
    if api_key is not None and request.method == 'POST':
        print("in")
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine ='gpt-3.5-turbo-instruct',
            # prompt = prompt,
            prompt = "Bonjour",
            maw_tokens = 265,
            temperature = 0.5
        )
        
       
        chatbot_response = response['choices'][0]['text']
    return render(request, 'chatbot.html',{"response":chatbot_response})