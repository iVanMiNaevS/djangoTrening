import json
from os import name
from django.shortcuts import render
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

from .forms import RegisterUserForm
from .models import Sneakers
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
# Create your views here.

def index(request):
    return render(request, "sneakers/index.html", {"title": "main page"})



def register(request):
    return render(request, "sneakers/register.html")

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "sneakers/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse("d")
        # return reverse_lazy("home")

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "sneakers/login.html"
    def get_success_url(self) -> str:
        return reverse_lazy("home")

def aboutSneak(request):
    return render(request, "sneakers/about.html",{"title": "about"})


def categories(request,categId):
    print(request.GET)
    return HttpResponse(f"categories{categId}")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")


# ////////////////////////////////////////////////////////////////////////
@csrf_exempt
def sneak(request):
    if request.method == "GET":
        sneaks = Sneakers.objects.all()
        res = []
        for sneak in sneaks:
            res.append({"name": sneak.name, "description": sneak.description})
        return JsonResponse(res, safe=False)
    elif request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))

        sneaks = Sneakers.objects.create(name = body["name"], description = body["description"])
        # sneaks.save()
        return JsonResponse({"create": True})
    else:
        return JsonResponse(data = {"error":"method not allowed"}, status= 400)

