from django import forms
from .models import Comment, Post


class ContributeForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('contribute', 'title', 'content',)
        # widgets = {
        #     'contribute' : forms.TextInput(attrs={'class':'input-text','placeholder':'Contributors Name' }),
        #     'title' : forms.TextInput(attrs={'class':'input-text','placeholder':'Title' }),
        #     'image' : forms.FileInput(attrs={'class':'input-text','placeholder':'Title' }),
            # 'content' : forms.Textarea(attrs={'class':'input-textarea editable medium-editor-textarea'})
        # }
    
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','image', 'content', )
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control textinputclass','placeholder':'Title' }),
            'content' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


