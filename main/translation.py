from modeltranslation.translator import TranslationOptions, register
from .models import Article

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)  # Ajoutez 'content' ici s'il n'est pas encore présent
