from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from . import forms
from . import models

# Create your views here.
def index(request):
    challenges = models.Challenge.objects.all()
    return render(request, 'challenges/index.html', {
        'challenges': challenges
    })

def create(request):
    if request.method == 'POST':
        form = forms.ChallengeForm(request.POST)
        if form.is_valid():
            challenger = models.Challenger.objects.filter(user=request.user).get()
            if not challenger:
                challenger = models.Challenger(user=request.user)
                challenger.save()
            new_challenge = form.save(commit=False)
            new_challenge.challenger = challenger
            new_challenge.slug = slugify(new_challenge.name)
            new_challenge.save()
            return HttpResponseRedirect('/')

    elif request.method == 'GET':
        form = forms.ChallengeForm()

    return render(request, 'challenges/create_challenge.html', {'form': form})

def details(request, identifier):
    challenge = get_challenge(identifier)
    return render(request, 'challenges/challenge_details.html', {'challenge': challenge})

def edit(request, identifier):
    challenge = get_challenge(identifier)
    if request.method == 'POST':
        form = forms.ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/challenges/{}'.format(challenge.slug))

    elif request.method == 'GET':
        form = forms.ChallengeForm(instance=challenge)
    return render(request, 'challenges/create_challenge.html',
                  {
                      'form': form,
                      'form_action': '{}/edit'.format(challenge.slug),
                      'submit_text': 'Update'
                  })

def get_challenge(identifier):
    challenge = None
    try:
        pk = int(identifier)
        challenge = models.Challenge.objects.get(pk=pk)
    except ValueError:
        challenge = models.Challenge.objects.get(slug=identifier)
    return challenge

