from django.http import HttpResponse


def index(request):
    return HttpResponse('<a href="apis/" >hello apis </a>')
