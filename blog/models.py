from django.db import models
from django.utils import timezone


#models.Model define que Post é um modelo de Django, assim o django sabe que ele deve ser salvo no banco de dados
class Post(models.Model):
    author = models.ForeignKey('auth.User') #ForeignKey, define link para outro modelo
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(
       blank=True, null=True)
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # __str__ define string com um título do Post na view de Admin
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)




class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self): # __str__ define string com um título do Comentário na view de Admin
        return self.text
