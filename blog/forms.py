from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'url')
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Postagem', 'style':'padding: 10px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}),
        }




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'text': forms.Textarea(attrs={'id':'comentario', 'placeholder': 'Comentário', 'style':'padding: 10px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'}),
        }
