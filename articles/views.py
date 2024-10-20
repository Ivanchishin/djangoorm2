from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all().prefetch_related('scope').order_by(ordering)
    context = {'object_list': object_list}
    for a in object_list:
        #print(a.text)
        print(a.scope)


    return render(request, template, context)
