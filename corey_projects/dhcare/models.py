from django.db import models
from django.utils import timezone


class department(models.Model):
    code = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    # This is required to show the name attribute of the database instead of 'department object (code)'
    # in the drop-down
    def __str__(self):
        return self.name


class provider(models.Model):
    ohp = models.CharField(max_length=100, primary_key=True)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return self.ohp


class appointment(models.Model):
    name = models.CharField(max_length=100)
    nid = models.IntegerField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    # This is better than 'CHOICES' because 'CHOICES' need static values for the drop-down but this is
    # polled from the database department
    department_code = models.ForeignKey('department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


FINGERPRINT_CHOICES_X = (
    (1, 3.11),
    (2, 4.11),
    (3, 3.05),
    (4, 4.21)
)
FINGERPRINT_CHOICES_Y = (
    (1, 3.11),
    (2, 4.11),
    (3, 3.05),
    (4, 4.21)
)


class fingerprints(models.Model):
    x = models.IntegerField(choices=FINGERPRINT_CHOICES_X, default=1)
    y = models.IntegerField(choices=FINGERPRINT_CHOICES_Y, default=1)

    def __str__(self):
        return self.x
