from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
def index(request):
    return render(request,"pages/index.html")


def video(request):
    return render(request,"pages/video.html")