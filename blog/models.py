from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Predio(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(
       blank=True, null=True)
    created_date = models.DateTimeField(
        default = timezone.now)
    on = models.TimeField(null = False, blank = False, default='08:00')
    off = models.TimeField(null = False, blank = False, default='22:00')
    # published_date = models.DateTimeField(
    #     blank=True, null=True)


    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)
    def predio(self):
        return self.predios.filter()


class Agendamento(models.Model):
    predio = models.ForeignKey('blog.Predio', related_name='predios')
    on = models.TimeField()
    off = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return "%s | Liga às %s e Desliga às %s | na data de %s"% (self.predio, self.on, self.off, self.date)
#
#
#
# class Comment(models.Model):
#     post = models.ForeignKey('blog.Post', related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.text
