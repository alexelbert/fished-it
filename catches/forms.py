from .models import Comment, Catch
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CatchForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = ['fish_species', 'fish_length', 'fish_weight', 'featured_image', 'public']
        widgets = {
            'fish_species': forms.TextInput(attrs={'class': 'form-control'}),
            'fish_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'fish_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'public': forms.Select(choices=Catch.STATUS, attrs={'class': 'form-control'}),
        }