from django.conf import settings
from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=200, default='')
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
    health_point = models.IntegerField(2)
    max_health_point = models.IntegerField(default='4')
    trait = models.TextField()
    appearance = models.CharField(max_length=200, default='')
    getsup = models.CharField(max_length=200, default='')
    body_features = models.CharField(max_length=200, default='')
    personality = models.CharField(max_length=200, default='')
    habit = models.CharField(max_length=200, default='')
    background = models.CharField(max_length=200, default='')
    weapon = models.CharField(max_length=200, default='')
    beloings = models.CharField(max_length=200, default='')
    features = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Appearance(models.Model):
    word = models.CharField(max_length=100, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return self.word


class Getsup(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class BodyFeatures(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Personality(models.Model):
    personality_type = models.IntegerField(default=1)
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Background(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Habit(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Belongings(models.Model):
    word = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word


class Features(models.Model):
    bigword = models.CharField(max_length=100, default='')
    smallword = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.bigword + " " + self.smallword


class Weapon(models.Model):
    bigword = models.CharField(max_length=100, default='')
    smallword = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.bigword + " " + self.smallword


class FirstName(models.Model):
    gender = models.IntegerField()
    name = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name + "(" + str(self.gender) + ")"


class LastName(models.Model):
    social_class = models.IntegerField()
    name = models.CharField(max_length=10, default='')
    
    def __str__(self):
        return self.name + "(" + str(self.social_class) + ")"


class NPCJob(models.Model):
    job_type = models.IntegerField()
    job = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.job + "(" + str(self.job_type) + ")"


class Misfortune(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Mission(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class NPCAim(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Weakness(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Asset(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Method(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Secret(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Fame(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Hobby(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Relationship(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Divinity(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Result(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class AerialAnimal(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class GroundAnimal(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class UnderwaterAnimal(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MonsterBodyFeature(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MonsterFeature(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MonsterAbility(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MonsterTactics(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word

class MonsterWeakness(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MaterialEffect(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MaterialElement(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MaterialForm(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class SpiritualEffect(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class SpiritualElement(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class SpiritualForm(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Mutation(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Madness(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MagicalDisaster(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class BookTopics(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Potion(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class MagicMaterial(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class TreasureFeature(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class PreciousMaterial(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Stuff(models.Model):
    use_type1 = models.IntegerField()
    use_type2 = models.IntegerField()
    weight = models.IntegerField()
    point = models.IntegerField()
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word + "(" + use_type1 + "/" + use_type2 + "/" + point + "/" + weight + ")"


class CityTopic(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word

class CityEvent(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class AreaTopic(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class HighClassBuilding(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word

class DownstreamBuilding(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class CityAction(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class BuildingSpace(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class StreetTactic(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class BuildingTactic(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class Faction(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class FactionFeature(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word


class FactionAim(models.Model):
    word = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.word
















