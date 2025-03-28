from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá, Munplanetado!</h1>")
