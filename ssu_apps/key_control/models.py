from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    code = models.CharField(max_length=4, primary_key=True)
    usertype = models.CharField(max_length=50)

    def __unicode__(self):
        return self.usertype


class KeyType(models.Model):
    class Meta:
        verbose_name = 'Key Type'
        verbose_name_plural = 'Key Types'

    code = models.CharField(max_length=4, primary_key=True)
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

    def get_absolute_url(self):
        return '/key_control/position/%d/' % self.position


class Sequence(models.Model):
    class Meta:
        verbose_name = 'Sequence'
        verbose_name_plural = 'Sequences'
        unique_together = ('position', 'sequence_num')

    position = models.ForeignKey(Position)
    sequence_num = models.IntegerField()
    issued = models.BooleanField()

    def __unicode__(self):
        return "Position %s, Sequence %d" % (self.position, self.sequence_num)

    def get_current_distribution(self):
        return self.distribution_set.latest('date')


class Distribution(models.Model):
    class Meta:
        verbose_name = 'Distribution'
        verbose_name_plural = 'Distributions'

    position = models.ForeignKey(Position, null=True)
    sequence = models.ForeignKey(Sequence)
    transtype = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)
    usertype = models.ForeignKey(UserType, null=True)
    userID = models.CharField(max_length=15, blank=True)
    fname = models.CharField(max_length=20, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=50, blank=True)
    duedate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    updater = models.ForeignKey(User)

    def __unicode__(self):
        return "%s Distribution, %s" % (self.sequence, self.date)


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
