from django.http import HttpResponse

def index(request):
  return HttpResponse('Here you can find workout suggestions')