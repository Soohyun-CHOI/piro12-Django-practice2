from django.shortcuts import render

from core.models import Article


def home(request):
    return render(request, "base.html")


def articlelist(request):
    articles = Article.objects.all()
    ctx = {
        "articles": articles
    }
    return render(request, "core/articlelist.html", ctx)


def articledetial(request, pk):  # pk = 아이디 값
    article = Article.objects.get(pk=pk)
    ctx = {
        "article": article
    }
    return render(request, "core/articledetail.html", ctx)
