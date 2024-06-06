from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the ai_meeting_transcript index.")
# Create your views here.
