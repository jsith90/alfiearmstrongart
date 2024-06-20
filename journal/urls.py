from django.urls import path
from . import views

urlpatterns = [
	path('journal/article_create', views.article_create, name='article_create'),
	path('journal/article_summary/<int:pk>', views.article_summary, name='article_summary'),
	path('journal/draft_article/<int:pk>', views.draft_article, name='draft_article'),
	path('journal/article/<int:pk>', views.article, name='article'),
	path('journal/delete_article/<int:pk>', views.delete_article, name='delete_article'),
]