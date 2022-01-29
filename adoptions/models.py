from django.db import models


# This is the pet model

class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
