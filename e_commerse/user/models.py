from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=False, max_length=2)
    secondary_email = models.EmailField(blank=True)
    Address = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.user.username


ADDRESS_CHOICES = (
    ('H', 'Home address'),
    ('W', 'Work Address'),
)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
