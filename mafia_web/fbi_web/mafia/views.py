from django.http.response import HttpResponse


def index(request):
    return HttpResponse("You're viewing Mafia Section")
