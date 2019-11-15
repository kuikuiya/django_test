from django.shortcuts import render
from django.utils import timezone
from .models import Character
from django.http import HttpResponse



# Create your views here.
def make_character(request):
    #Character.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'maze/make_character.html', {})


def make_character_by_step(request, step):


    return HttpResponse(
        "<p>OK, it's " + 
        'step ' + step + "</p>" + 
        '<a href="/make/char/step/' + str(int(step) + 1) + '">' + 
        'next step</a>')
