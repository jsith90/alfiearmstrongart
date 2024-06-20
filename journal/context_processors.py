# myapp/context_processors.py
from .models import Article

def articles_processor(request):
    return {
        'articles': Article.objects.all()
    }