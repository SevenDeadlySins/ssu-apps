from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    usertype = models.CharField(max_length=50)

    def __unicode__(self):
        return self.usertype


class KeyType(models.Model):
    class Meta:
        verbose_name = 'Key Type'
        verbose_name_plural = 'Key Types'

    keytype = models.CharField(max_length=50)

    def __unicode__(self):
        return self.keytype


class KeyStatus(models.Model):
    class Meta:
        verbose_name = 'Key Status'
        verbose_name_plural = 'Key Statuses'

    status = models.CharField(max_length=10)

    def __unicode__(self):
        return self.status


class Position(models.Model):
    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    position = models.IntegerField(primary_key=True)
    keytype = models.ForeignKey(KeyType)
    keyway = models.CharField(max_length=25)
    status = models.ForeignKey(KeyStatus)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.position)


class Sequence(models.Model):
    class Meta:
        verbose_name = 'Sequence'
        verbose_name_plural = 'Sequences'

    position = models.ForeignKey(Position)

    def __unicode__(self):
        pass


class Distribution(models.Model):
    class Meta:
        verbose_name = 'Distribution'
        verbose_name_plural = 'Distributions'

    position = models.ForeignKey(Position)
    sequence = models.ForeignKey(Sequence)
    transtype = models.CharField(max_length=15)
    date = models.DateField(auto_now=True)
    usertype = models.ForeignKey(UserType)
    userID = models.CharField(max_length=15)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    duedate = models.DateField()
    notes = models.TextField()

    def __unicode__(self):
        pass


class Location(models.Model):
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    position = models.ForeignKey(Position)
    suffix = models.CharField(max_length=2)
    room = models.CharField(max_length=50)
    propnum = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __unicode__(self):
        pass
