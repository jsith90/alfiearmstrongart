from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Article
from .forms import CreateArticle
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def article_create(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        if request.method == 'POST':
            article_form = CreateArticle(request.POST, request.FILES)
            
            if article_form.is_valid():
                # save article to db
                article = article_form.save()
                return redirect('home')
            else:
                return render(request, 'journal/article_create.html', { 'article_form': article_form })
        else:
            article_form = CreateArticle()
            return render(request, 'journal/article_create.html', { 'article_form': article_form })
    else:
        return redirect('home')


def article_summary(request, pk):
    user = request.user
    articles = Article.objects.get(id=pk)
    return render(request, 'journal/article_summary.html', {'articles':articles})


def draft_article(request, pk):
    user = request.user
    article = get_object_or_404(Article, id=pk)
    
    if user.is_superuser:
        if request.method == 'POST':
            # Handle the entire article form but only save is_published
            article_form = CreateArticle(request.POST, instance=article)
            if article_form.is_valid():
                # Update only the is_published field
                article.is_published = article_form.cleaned_data['is_published']
                article.save(update_fields=['is_published'])
                return redirect('home')
        else:
            article_form = CreateArticle(instance=article)
        
        return render(request, 'journal/draft_article.html', {
            'article': article,
            'article_form': article_form
        })
    else:
        return redirect('home')


def article(request, pk):
    article = Article.objects.get(id=pk)
    if article.is_published:
        return render(request, 'journal/article.html', {'article':article})
    else:
        return redirect('home')


def delete_article(request, pk):
    user = request.user
    article = Article.objects.get(id=pk)
    if user.is_superuser:
        Article.objects.get(id=pk).delete()
        return redirect('home')
    else:
        return redirect('home')