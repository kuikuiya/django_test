from django.conf import settings
from django.db import models
from django.utils import timezone


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
    trait = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name