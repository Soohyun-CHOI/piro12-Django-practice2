from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home),
    path("article/", views.articlelist),
    path("article/<int:pk>", views.articledetial),  # <int:pk> = int 형태로 온 pk는 바로 받을 수 있게
]