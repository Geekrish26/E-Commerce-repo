from django.conf import settings
from django.db import models
# from django.db.models import Sum
from django.shortcuts import reverse
import uuid
from django.contrib.auth import get_user_model


# User
User = get_user_model()
from user.models import Profile
import datetime


class Slides(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.ImageField(help_text="Size: 1920x570")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    mrp_price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    description_short = models.CharField(max_length=100)
    description_long = models.TextField()
    image = models.ImageField(upload_to="media")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:product-detail", kwargs={'pk': self.pk})

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    add_date = models.DateField(default=datetime.datetime.today)

    # def __str__(self):
    #     return str(self.profile)

    def get_cart_details(profile):
        return Cart.objects.filter(profile=profile).order_by('-add_date')