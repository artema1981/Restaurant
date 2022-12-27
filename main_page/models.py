import os.path
from django.db import models
from django.core.validators import RegexValidator
import uuid
from datetime import date


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    def get_file_name(self, filname: str):
        ext = filname.strip().split('.')[-1]
        filname = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filname)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position',)


class Whuus(models.Model):
    title = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=400, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}: {self.position}'

    class Meta:
        ordering = ('position', )


class Events(models.Model):
    def get_file_name(self, filname: str):
        ext = filname.strip().split('.')[-1]
        filname = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events', filname)

    title = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=400, blank=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name)
    date_event = models.DateField(default=date.today)
    def __str__(self):
        return f'{self.title}: {self.position} date: {self.date_event}'

    class Meta:
        ordering = ('position', )


class Gallery(models.Model):
    def get_file_name(self, filname: str):
        ext = filname.strip().split('.')[-1]
        filname = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery', filname)

    photo = models.ImageField(upload_to=get_file_name)
    desc = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)

class UserReservation(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Phone number should be in +380xx xxx xxx xx format')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=259, blank=True)
    date = models.DateField(auto_now_add=True)
    manager_date_processed = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name} {self.phone}: {self.message[:20]}'

class ContactForm(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Phone number should be in +380xx xxx xxx xx format')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=259, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name} {self.phone}: {self.subject[:20]}'