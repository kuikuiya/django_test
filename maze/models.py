from django.conf import settings
from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=400, default='')
    register_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.register_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Character(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    level = models.IntegerField()
    exp = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    intelligence = models.IntegerField()
    str_power = models.IntegerField()
    def_power = models.IntegerField()
    health_point = models.IntegerField()
    max_health_point = models.IntegerField(default='4')
    trait = models.TextField()
    appearance = models.CharField(max_length=40, default='')
    getsup = models.CharField(max_length=40, default='')
    body_features = models.CharField(max_length=40, default='')
    personality = models.CharField(max_length=40, default='')
    habit = models.CharField(max_length=40, default='')
    background = models.CharField(max_length=40, default='')
    weapon = models.CharField(max_length=40, default='')
    beloings = models.CharField(max_length=40, default='')
    features = models.CharField(max_length=40, default='')
    spells = models.TextField(default='')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class NPCharacter(models.Model):
    name = models.CharField(max_length=40, default='')
    max_health_point = models.IntegerField(default='4')
    health_point = models.IntegerField()
    armor = models.IntegerField()
    attack_bonus = models.IntegerField()
    strength_bonus = models.IntegerField()
    dexterity_bonus = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    spells = models.TextField(default='')
    hometown = models.CharField(max_length=40, default='')
    job = models.CharField(max_length=40, default='')
    asset = models.CharField(max_length=40, default='')
    weakness = models.CharField(max_length=40, default='')
    aim = models.CharField(max_length=40, default='')
    misfortune = models.CharField(max_length=40, default='')
    mission = models.CharField(max_length=40, default='')
    method = models.CharField(max_length=40, default='')
    appearance = models.CharField(max_length=40, default='')
    body_features = models.CharField(max_length=40, default='')
    getsup = models.CharField(max_length=40, default='')
    personality = models.CharField(max_length=40, default='')
    fame = models.CharField(max_length=40, default='')
    habit = models.CharField(max_length=40, default='')
    relationship = models.CharField(max_length=40, default='')
    divinity = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(max_length=40, default='')
    max_health_point = models.IntegerField(default='4')
    health_point = models.IntegerField()
    armor = models.IntegerField()
    attack_bonus = models.IntegerField()
    strength_bonus = models.IntegerField()
    dexterity_bonus = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    spells = models.TextField(default='')
    habitat = models.IntegerField()
    monster_type = models.CharField(max_length=40, default='')
    body_features = models.CharField(max_length=40, default='')
    traits = models.CharField(max_length=40, default='')
    ablity = models.CharField(max_length=40, default='')
    tactics = models.CharField(max_length=40, default='')
    personality = models.CharField(max_length=40, default='')
    weakness = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name


class Spell(models.Model):
    material_effect = models.CharField(max_length=40, default='')
    material_element = models.CharField(max_length=40, default='')
    material_form = models.CharField(max_length=40, default='')
    spiritual_effect = models.CharField(max_length=40, default='')
    spiritual_elelment = models.CharField(max_length=40, default='')
    spiritual_form = models.CharField(max_length=40, default='')
    mutation = models.CharField(max_length=40, default='')
    madness = models.CharField(max_length=40, default='')
    magical_disaster = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name

"""
class City(models.Model):
    city_topic = models.CharField(max_length=40, default='') 
    building_room = models.CharField(max_length=40, default='')
    street_tactic = models.CharField(max_length=40, default='')
    building_tactic = models.CharField(max_length=40, default='')
    faction = models.CharField(max_length=40, default='')
    faction_feature = models.CharField(max_length=40, default='')
    faction_aim = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.city_topic + "/" + self.building_room + "/" \
        + self.street_tactic + "/" + self.building_tactic + "/" + self.faction + "/" \
        + self.faction_feature + "/" + self.faction_aim    



class Wild(models.Model):
    wild_area = models.CharField(max_length=40, default='')
    wild_terrain = models.CharField(max_length=40, default='')
"""
class Dungeon(models.Model):
    pass


class Appearance(models.Model):
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class Getsup(models.Model):
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class BodyFeatures(models.Model):
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class Personality(models.Model):
    personality_type = models.IntegerField(default=1)
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class Background(models.Model):
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class Habit(models.Model):
    word = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.word


class Belongings(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Features(models.Model):
    bigword = models.CharField(max_length=40, default='')
    smallword = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.bigword + " " + self.smallword


class Weapon(models.Model):
    bigword = models.CharField(max_length=40, default='')
    smallword = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.bigword + " " + self.smallword


class FirstName(models.Model):
    gender = models.IntegerField()
    name = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name + "(" + str(self.gender) + ")"


class LastName(models.Model):
    social_class = models.IntegerField()
    name = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.name + "(" + str(self.social_class) + ")"


class NPCJob(models.Model):
    job_type = models.IntegerField()
    job = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.job + "(" + str(self.job_type) + ")"


class Misfortune(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Mission(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class NPCAim(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Weakness(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Asset(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Method(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Secret(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Fame(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Hobby(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Relationship(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Divinity(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Result(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MonsterType(models.Model):
    habitat = models.IntegerField()
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word + "(" + str(self.habitat) + ")"


class MonsterBodyFeature(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MonsterFeature(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MonsterAbility(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MonsterTactics(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word

class MonsterWeakness(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MaterialEffect(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MaterialElement(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MaterialForm(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class SpiritualEffect(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class SpiritualElement(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class SpiritualForm(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Mutation(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Madness(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MagicalDisaster(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Book(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Potion(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MagicMaterial(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class TreasureFeature(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class PreciousMaterial(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Stuff(models.Model):
    use_type1 = models.IntegerField()
    use_type2 = models.IntegerField()
    weight = models.IntegerField()
    point = models.IntegerField()
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word + "(" + use_type1 + "/" + use_type2 + "/" + point + "/" + weight + ")"


class CityTopic(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word

class CityEvent(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class AreaTopic(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class HighClassBuilding(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word

class DownstreamBuilding(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class CityAction(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class BuildingRoom(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class StreetTactic(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class BuildingTactic(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Faction(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class FactionFeature(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class FactionAim(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildArea(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildTerrain(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildArtifact(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildAreaFeature(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildDiscovery(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildAction(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WildThreat(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class Herb(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class ToxicPlant(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MotelNamePrefix(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MotelNameSuffix(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class MotelUniqueness(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonEntrance(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonForm(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonPlacement(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class WhyDungeonWasAbandoned(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonReward(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonAction(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonRoom(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonRoomDetail(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonMechanism(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class DungeonThreat(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class TrapEffect(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word


class TrapActuation(models.Model):
    word = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.word





















