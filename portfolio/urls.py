from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('portfolio/about', views.about, name='about'),
	path('portfolio/add_gallery', views.add_gallery, name='add_gallery'),
	path('portfolio/gallery_summary/<int:pk>', views.gallery_summary, name='gallery_summary'),
	path('portfolio/gallery/<int:pk>', views.gallery, name='gallery'),
	path('portfolio/draft_gallery/<int:pk>', views.draft_gallery, name='draft_gallery'),
	path('portfolio/delete_gallery/<int:pk>', views.delete_gallery, name='delete_gallery'),
	path('portfolio/login_user', views.login_user, name="login_user"),
    path('portfolio/logout_user', views.logout_user, name="logout"),
]