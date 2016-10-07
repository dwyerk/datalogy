from django.shortcuts import render
from django.http import HttpResponse
from challenges.models import Challenge

# Create your views here.
def index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', {
        'challenges': challenges
    })
