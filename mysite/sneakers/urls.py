from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('categ/<slug:categId>/', categories),
    path('about/', aboutSneak, name="about"),
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path("api/sneakers", sneak)
]
