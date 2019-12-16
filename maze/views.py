from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Character, NPCharacter, Monster, Spell, \
    Appearance, Getsup, BodyFeatures, Personality, \
    Background, Habit, Belongings, Features, Weapon, FirstName, LastName, \
    NPCJob, Misfortune, Mission, NPCAim, Weakness, Asset, Method, Secret, \
    Fame, Hobby, Relationship, Divinity, Result, \
    MonsterType, MonsterBodyFeature, MonsterFeature, MonsterAbility, \
    MonsterTactics, MonsterWeakness, MaterialEffect, MaterialElement, \
    MaterialForm, SpiritualEffect, SpiritualElement, SpiritualForm, Mutation, \
    Madness, MagicalDisaster, Book, Potion, MagicMaterial, \
    TreasureFeature, PreciousMaterial, Stuff, CityTopic, CityEvent, \
    AreaTopic, HighClassBuilding, DownstreamBuilding, CityAction, \
    BuildingRoom, StreetTactic, BuildingTactic, Faction, FactionFeature, \
    FactionAim, WildArea, WildTerrain, WildArtifact, WildAreaFeature, WildDiscovery, WildAction, WildThreat, \
    Herb, ToxicPlant, MotelNamePrefix, MotelNameSuffix, MotelUniqueness, \
    DungeonEntrance, DungeonForm, DungeonPlacement, WhyDungeonWasAbandoned, \
    DungeonReward, DungeonAction, DungeonRoom, DungeonRoomDetail, \
    DungeonMechanism, DungeonThreat, TrapEffect, TrapActuation              

import random
from . import data_input


def register_data(request):
    data_input.bulk_save()

    return HttpResponse(
        "<p>OK, it's </p>")

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


def make_npcharacter_by_random():
    job = NPCJob.objects.all()
    asset = Asset.objects.all()
    weakness = Weakness.objects.all()
    aim = NPCAim.objects.all()
    misfortune = Misfortune.objects.all()
    mission = Mission.objects.all()
    method = Method.objects.all()  
    appearances = Appearance.objects.all()
    getsup = Getsup.objects.all()
    body_features = BodyFeatures.objects.all()
    personality = Personality.objects.all()
    habit = Habit.objects.all()
    secret = Secret.objects.all()
    fame = Fame.objects.all()
    hobby = Hobby.objects.all()
    relationship = Relationship.objects.all()
    divinity = Divinity.objects.all()
    firstName = FirstName.objects.all()
    lastName = LastName.objects.all()

    name = firstName[random.randint(1, firstName.count() - 1)].name + " " + \
        lastName[random.randint(1, lastName.count() - 1)].name

    data = {
        'hometown': random.randint(1, 3),
        'job':  job[random.randint(1, job.count()) - 1],
        'asset':  asset[random.randint(1, asset.count()) - 1],
        'weakness':  weakness[random.randint(1, weakness.count()) - 1],
        'aim':  aim[random.randint(1, aim.count()) - 1],
        'misfortune':  misfortune[random.randint(1, misfortune.count()) - 1],
        'mission':  mission[random.randint(1, mission.count()) - 1],
        'method': method[random.randint(1, method.count()) - 1],
        'appearance': appearances[random.randint(1, appearances.count()) - 1],
        'getsup': getsup[random.randint(1, getsup.count()) - 1],
        'body_features': body_features[random.randint(1, body_features.count()) - 1],
        'personality': personality[random.randint(1, personality.count()) - 1],
        'habit': habit[random.randint(1, habit.count()) - 1],
        'secret': secret[random.randint(1, secret.count()) - 1],
        'fame': fame[random.randint(1, fame.count()) - 1],
        'hobby': hobby[random.randint(1, hobby.count()) - 1],
        'relationship': relationship[random.randint(1, relationship.count()) - 1],
        'divinity': divinity[random.randint(1, divinity.count()) - 1],
        'armor_bonus': random.randint(1, 6),
        'attack_bonus': random.randint(1, 6),
        'strength_bonus': random.randint(1, 6),
        'dexterity_bonus': random.randint(1, 6),
        'intelligence_bonus': random.randint(1, 6),
        'name': name,
        'level': 1,
        'max_health_point': 6
    }

    return data
    # return HttpResponse(template, {'data': data})
    #return render(request, 'maze/game.html', {'data': data})


def make_monster_by_random():
    
    weakness = Weakness.objects.all()
    body_features = BodyFeatures.objects.all()
    personality = Personality.objects.all()
    monster_type = MonsterType.objects.all()
    body_features = MonsterBodyFeature.objects.all()
    feature = MonsterFeature.objects.all()
    ability = MonsterAbility.objects.all()
    tactics = MonsterTactics.objects.all()
    divinity = Divinity.objects.all()
    firstName = FirstName.objects.all()
    lastName = LastName.objects.all()

    name = firstName[random.randint(1, firstName.count() - 1)].name + " " + \
        lastName[random.randint(1, lastName.count() - 1)].name

    data = {
        'habitat': random.randint(1, 3),
        'monster_type':  monster_type[random.randint(1, monster_type.count()) - 1],
        'weakness':  weakness[random.randint(1, weakness.count()) - 1],
        'body_features': body_features[random.randint(1, body_features.count()) - 1],
        'personality': personality[random.randint(1, personality.count()) - 1],
        'traits': feature[random.randint(1, feature.count()) - 1],
        'ablity': ability[random.randint(1, ability.count()) - 1],
        'tactics': tactics[random.randint(1, tactics.count()) - 1],
        'armor_bonus': random.randint(1,6),
        'attack_bonus': random.randint(1,6),
        'strength_bonus': random.randint(1, 6),
        'dexterity_bonus': random.randint(1, 6),
        'intelligence_bonus': random.randint(1, 6),
        'name': name,
        'level': 1,
        'max_health_point': 6
    }

    return data
    # return HttpResponse(template, {'data': data})
    #return render(request, 'maze/game.html', {'data': data})


def make_spell():
    column = random.randint(1, 6)
    row = random.randint(1, 6)

    prefix = ""
    suffix = ""

    if row == 1:
        if column >= 1 and column <= 3:
            material_effects = MaterialEffect.objects.all()
            material_forms = MaterialForm.objects.all()
            prefix = material_effects[random.randint(1, material_effects.count()) - 1]
            suffix = material_forms[random.randint(1, material_forms.count()) - 1]
        else:
            spiritual_elements = SpiritualElement.objects.all()
            material_forms = MaterialForm.objects.all()
            prefix = spiritual_elements[random.randint(1, spiritual_elements.count()) - 1]
            suffix = material_forms[random.randint(1, material_forms.count()) - 1]       
    elif row == 2:
        if column >= 1 and column <= 3:
            material_effects = MaterialEffect.objects.all()
            spiritual_forms = SpiritualForm.objects.all()
            prefix = material_effects[random.randint(1, material_effects.count()) - 1]
            suffix = spiritual_forms[random.randint(1, spiritual_forms.count()) - 1]
        else:
            spiritual_elements = SpiritualElement.objects.all()
            spiritual_forms = SpiritualForm.objects.all()
            prefix = spiritual_elements[random.randint(1, spiritual_elements.count()) - 1]
            suffix = spiritual_forms[random.randint(1, spiritual_forms.count()) - 1]
    elif row == 3:
        if column >= 1 and column <= 3: 
            spiritual_effects = SpiritualEffect.objects.all()
            material_forms = MaterialForm.objects.all()
            prefix = spiritual_effects[random.randint(1, spiritual_effects.count()) - 1]
            suffix = material_forms[random.randint(1, material_forms.count()) - 1]
        else:            
            material_effects = MaterialEffect.objects.all()
            material_elements = MaterialElement.objects.all()
            prefix = material_effects[random.randint(1, material_effects.count()) - 1]
            suffix = material_elements[random.randint(1, material_elements.count()) - 1]
    elif row == 4:
        if column >= 1 and column <= 3:
            spiritual_effects = SpiritualEffect.objects.all()
            spiritual_forms = SpiritualForm.objects.all()
            prefix = spiritual_effects[random.randint(1, spiritual_effects.count()) - 1]
            suffix = spiritual_forms[random.randint(1, Spiritual_forms.count()) - 1]
        else:
            material_effects = MaterialEffect.objects.all()
            spiritual_elements = SpiritualElement.objects.all()
            prefix = material_effects[random.randint(1, material_effects.count()) - 1]
            suffix = spiritual_elements[random.randint(1, spiritual_elements.count()) - 1]
    elif row == 5:
        if column >= 1 and column <= 3:
            material_elements = MaterialElement.objects.all()
            material_forms = MaterialForm.objects.all()
            prefix = material_elements[random.randint(1, material_elements.count()) - 1]
            suffix = material_forms[random.randint(1, material_forms.count()) - 1]       
        else:
            material_effects = MaterialEffect.objects.all()
            spiritual_elements = SpiritualElement.objects.all()
            prefix = material_effects[random.randint(1, material_effects.count()) - 1]
            suffix = spiritual_elements[random.randint(1, spiritual_elements.count()) - 1]
    elif row == 6:
        if column >= 1 and column <= 3:
            material_elements = MaterialElement.objects.all()
            spiritual_forms = SpiritualForm.objects.all()
            prefix = material_elements[random.randint(1, material_elements.count()) - 1]
            suffix = spiritual_forms[random.randint(1, spiritual_forms.count()) - 1]       
        else:
            spiritual_effects = SpiritualEffect.objects.all()
            spiritual_elements = SpiritualElement.objects.all()
            prefix = spiritual_effects[random.randint(1, spiritual_effects.count()) - 1]
            suffix = spiritual_elements[random.randint(1, spiritual_elements.count()) - 1]

    spell = prefix + " " + suffix

    return spell


def make_place():
    place_type = random.randint(1, 3)
    if place_type == 1:
        make_city()
    elif place_type == 2:
        make_wild()
    else:
        make_dungeon()




def play_game(request):
    data = {}
    data['join_with'] = make_monster_by_random()
    data['spell'] = make_spell()
    return render(request, 'game.html', data)


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
