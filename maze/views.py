from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Character, Appearance, Getsup, BodyFeatures, Personality, \
    Background, Habit, Belongings, Features, Weapon, FirstName, LastName, \
    NPCJob, Misfortune, Mission, NPCAim, Weakness, Asset, Method, Secret, \
    Fame, Hobby, Relationship, Divinity, Result, \
    AerialAnimal, GroundAnimal, UnderwaterAnimal, MonsterBodyFeature, \
    MonsterFeature, MonsterAbility, MonsterTactics, MonsterWeakness, \
    MaterialEffect, MaterialElement, MaterialForm, SpiritualEffect, \
    SpiritualElement, SpiritualForm, Mutation, Madness, MagicalDisaster, \
    BookTopics, Potion, MagicMaterial, TreasureFeature, PreciousMaterial, \
    Stuff, CityTopic, CityEvent, AreaTopic, HighClassBuilding, \
    DownstreamBuilding, CityAction, BuildingSpace, StreetTactic, \
    BuildingTactic, Faction, FactionFeature, FactionAim
import random


# Create your views here.
def make_character(request):
    #Character.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')

    step_title = {
        'step': 0
    }
    return render(request, 'maze/make_character.html', step_title)


def make_character_by_random(request):
    appearances = Appearance.objects.all()
    getsup = Getsup.objects.all()
    body_features = BodyFeatures.objects.all()
    personality = Personality.objects.all()
    habit = Habit.objects.all()
    background = Background.objects.all()
    features = Features.objects.all()
    weapon = Weapon.objects.all()
    belongings = Belongings.objects.all()
    firstName = FirstName.objects.all()
    lastName = LastName.objects.all()

    name = firstName[random.randint(1, firstName.count() - 1)].name + " " + \
        lastName[random.randint(1, lastName.count() - 1)].name


    data = {
        'appearance': appearances[random.randint(1, appearances.count()) - 1],
        'getsup': getsup[random.randint(1, getsup.count()) - 1],
        'body_features': body_features[random.randint(1, body_features.count()) - 1],
        'personality': personality[random.randint(1, personality.count()) - 1],
        'habit': habit[random.randint(1, habit.count()) - 1],
        'background': background[random.randint(1, background.count()) - 1],
        'weapon': weapon[random.randint(1, weapon.count()) - 1],
        'belongings': belongings[random.randint(1, belongings.count()) - 1],
        'features': features[random.randint(1, features.count()) - 1],
        'strength': random.randint(1, 6),
        'dexterity': random.randint(1, 6),
        'intelligence': random.randint(1, 6),
        'name': name,
        'level': 1,
        'max_health_point': 4
    }

    #return HttpResponse(template, {'data': data})
    return render(request, 'maze/make_character.html', {'data': data})
"""        
    return HttpResponse(
        "<p>OK, it's " + 
        'step ' + step + "</p>" + 
        '<a href="/make/char/step/' + str(int(step) + 1) + '">' + 
        'next step</a>')
"""       

def make_character_by_step_ver_template(request, step):
    result = {}
    result['next'] = str(int(step) + 1)
    result['prev'] = str(int(step) - 1)
    result['now'] = step

    return render(request, 'maze/make_character_step.html', {'data': result})

"""
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
"""

def hello_world(request):
    return render(request, 'maze/hello_world.html')
