from django.db import models


# Create your models here.

class User(models.Model):
    full_name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class EventParticipatingGroup(models.Model):
    group_id = models.IntegerField()
    ride_member = models.ManyToManyField('User')

    def get_group_members(self):
        return ', '.join([g.full_name for g in self.ride_member.all()])

    def __str__(self):
        return str(self.group_id)


class CyclingEvent(models.Model):
    cycling_event_image = models.ImageField(null=True, upload_to='upload', blank=True)
    event_name = models.TextField(verbose_name='Cycling Event')
    event_description = models.TextField()
    distance = models.TextField()
    prize_pool = models.FloatField()
    event_date = models.DateField()
    participating_group = models.ForeignKey('EventParticipatingGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
