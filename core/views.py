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


def articlecreate(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        author = request.POST["author"]

        article = Article.objects.create(title=title, content=content, author=author)  # 인스턴스 만들고 save까지 한 번에 처리

        ctx = {
            "article": article
        }

        return render(request, "core/articlecreate.html", ctx)
    return render(request, "core/articlecreate.html")