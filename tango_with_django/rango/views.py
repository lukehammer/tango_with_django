from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says you and still love it!")