from django.urls import path
from . import views

app_name = "core"  # 앱이름 지정

urlpatterns = [
    path("", views.home),
    path("article/", views.articlelist, name="articlelist"),
    path("article/<int:pk>", views.articledetial, name="articledetail"),  # <int:pk> = int 형태로 온 pk는 바로 받을 수 있게
    path("article/create/", views.articlecreate, name="articlecreate"),
]