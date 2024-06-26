from django import forms
from django.forms import inlineformset_factory
from .models import Gallery, Image

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'is_published']
        labels = {
            'title': 'Gallery Title',
            'description': 'Description',
            'is_published':'Check the box to publish gallery:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter gallery title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'is_published': forms.CheckboxInput(),

        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption']
        labels = {
            'image': 'Upload image:',
            'caption': 'Image Caption'
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
            }),
            'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
        }

ImageFormSet = inlineformset_factory(Gallery, Image, form=ImageForm, max_num=None, extra=50, can_delete=True)
