from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Gallery, Image
from .forms import GalleryForm, ImageFormSet
from django.contrib.auth import authenticate, login, logout


# login page
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_user')
    else:
        return render(request, 'portfolio/login.html', {})

# logs users out
def logout_user(request):
    logout(request)
    return redirect('home')


def add_gallery(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        if request.method == "POST":
            gallery_form = GalleryForm(request.POST)
            image_formset = ImageFormSet(request.POST, request.FILES)

            if gallery_form.is_valid() and image_formset.is_valid():
                gallery = gallery_form.save()
                images = image_formset.save(commit=False)
                for image in images:
                    image.gallery = gallery
                    image.save()
                return redirect('home')  # Redirect to a success page or similar
            else:
                return render(request, 'portfolio/add_gallery.html', {
                    'gallery_form': gallery_form,
                    'image_formset': image_formset
                })
        else:
            gallery_form = GalleryForm()
            image_formset = ImageFormSet()
            return render(request, 'portfolio/add_gallery.html', {
                'gallery_form': gallery_form,
                'image_formset': image_formset
            })
    else:
        return redirect('home')


def gallery_summary(request, pk):
    user = request.user
    galleries = Gallery.objects.get(id=pk)
    return render(request, 'portfolio/gallery_summary.html', {'galleries':galleries})


def gallery(request, pk):
    gallery = Gallery.objects.get(id=pk)
    images = gallery.image.all()
    if gallery.is_published:
        return render(request, 'portfolio/gallery.html', {'gallery':gallery, 'images':images})
    else:
        return redirect('home')


# def draft_gallery(request, pk):
#     user = request.user
#     gallery = Gallery.objects.get(id=pk)
#     images = gallery.image.all()
#     gallery_form = GalleryForm(request.POST or None, instance=gallery)
#     if user.is_superuser:
#         if gallery_form.is_valid():
#             gallery_form.save()
#             return redirect('home')
#         return render(request, 'portfolio/draft_gallery.html', {'gallery':gallery, 'images':images, 'gallery_form':gallery_form})
#     else:
#         return redirect('home')


def draft_gallery(request, pk):
    user = request.user
    gallery = get_object_or_404(Gallery, id=pk)
    images = gallery.image.all()
    if user.is_superuser:
        if request.method == 'POST':
            # Handle the entire article form but only save is_published
            gallery_form = GalleryForm(request.POST, instance=gallery)
            if gallery_form.is_valid():
                # Update only the is_published field
                gallery_form.is_published = gallery_form.cleaned_data['is_published']
                gallery.save(update_fields=['is_published'])
                return redirect('home')
        else:
            gallery_form = GalleryForm(instance=gallery)
        
        return render(request, 'portfolio/draft_gallery.html', {
            'gallery': gallery,
            'images': images,
            'gallery_form': gallery_form,
        })
    else:
        return redirect('home')


def delete_gallery(request, pk):
    user = request.user
    gallery = Gallery.objects.get(id=pk)
    if user.is_superuser:
        Gallery.objects.get(id=pk).delete()
        return redirect('home')
    else:
        return redirect('home')


def home(request):
	return render(request, 'portfolio/home.html', {})

def about(request):
    return render(request, 'portfolio/about.html', {})