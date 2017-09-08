from django import forms
from .models import Post, Comment




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'materialize-textarea'}),
        }




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
