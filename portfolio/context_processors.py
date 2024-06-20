# myapp/context_processors.py
from .models import Gallery

def galleries_processor(request):
    return {
        'galleries': Gallery.objects.all()
    }