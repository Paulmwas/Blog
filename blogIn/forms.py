from django import forms
from .models import BlogModel 

class CreateBlog(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','author','content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'time': forms.DateTimeInput(attrs={'class':'form-control'}),
        }

