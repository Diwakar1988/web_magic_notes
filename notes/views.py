from django.http import HttpResponse


def index(request):
    response = HttpResponse("<h1>Your Notes</h1>")
    return response


def details(request, note_id):
    response = HttpResponse("<h1>Details for Note id: {}</h1>".format(note_id))
    return response
