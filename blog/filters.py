from .models import Post
import django_filters

class TitleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['title']
