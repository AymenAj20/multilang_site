from modeltranslation.translator import TranslationOptions, register
from .models import Article

# Fiare un register du modéle Article pour la traduction de titre et content
@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)  
