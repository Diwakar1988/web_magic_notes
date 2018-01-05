from django.http import HttpResponse


def index(request):
    response = HttpResponse("<h1>Hello from Authorize app</h1>")
    return response
