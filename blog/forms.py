from django import forms
from .models import Comment, Post


class ContributeForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('contribute', 'title','image', 'content',)
        widgets = {
            'contribute' : forms.TextInput(attrs={'class':'form-control textinputclass','placeholder':'Name' }),
            'title' : forms.TextInput(attrs={'class':'form-control textinputclass','placeholder':'Title' }),
            'content' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
    
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','image', 'content', )
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control textinputclass','placeholder':'Title' }),
            'content' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


