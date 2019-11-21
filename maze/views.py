from django.shortcuts import render
from django.utils import timezone
from .models import Character, Player
from django.http import HttpResponse


# Create your views here.
def make_character(request):
    #Character.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')

    step_title = {
        'step': 0
    }
    return render(request, 'maze/make_character.html', step_title)


def make_character_by_step(request, step):
        
    return HttpResponse(
        "<p>OK, it's " + 
        'step ' + step + "</p>" + 
        '<a href="/make/char/step/' + str(int(step) + 1) + '">' + 
        'next step</a>')


def make_character_by_step_ver_template(request, step):
    result = {}
    result['next'] = str(int(step) + 1)
    result['prev'] = str(int(step) - 1)
    result['now'] = step

    return render(request, 'maze/make_character_step.html', {'data': result})


def make_character_by_step_ver_template_with_user(request, step, user):
    player = Player.objects.filter(id=user)
    playerOne = None
    print('player from db', player)
    if len(player) == 0:
        return HttpResponse('I cannot find you.')
    else:
        playerOne = player[0]
    # if player is None:
    #     return HttpResponse('I cannot find you.')

    result = {}
    result['next'] = str(int(step) + 1)
    result['prev'] = str(int(step) - 1)
    result['now'] = step
    result['user'] = playerOne.name

    # step = playerOne.step
    playerOne.step = step
    playerOne.save()

    return render(request, 'maze/make_character_step.html', {'data': result})

