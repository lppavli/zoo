from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    # Семейсвто - медведь
    name = models.CharField(max_length=64, unique=True)

    # Основные типы полей
    # Int
    # models.IntegerField()
    # models.PositiveIntegerField()
    # models.PositiveSmallIntegerField()
    # Boolean
    # models.BooleanField()
    # Text
    # models.TextField()
    # Array (связь)
    # Datetime, time, date
    # models.DateTimeField
    # models.DateField
    # models.TimeField
    # jsonb
    # models.JSONField
    # Float
    # models.FloatField
    # models.DecimalField
    # Url, Email
    # models.URLField
    # models.UUIDField
    # bites, blob
    # models.BinaryField
    # Картинка
    # models.ImageField()
    # models.FileField()

    def __str__(self):
        return self.name


class Kind(models.Model):
    # Вид - Бурый (медведь)
    name = models.CharField(max_length=64)
    family = models.ForeignKey(Family, on_delete=models.PROTECT, db_index=True)
    image = models.ImageField(upload_to='kind', blank=True, null=True)

    unique_together = [['name', 'family']]

    def __str__(self):
        return self.name


class AnimalCard(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Food(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT)
    card = models.OneToOneField(AnimalCard, on_delete=models.CASCADE, blank=True, null=True)
    foods = models.ManyToManyField(Food)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=True, null=True)

    def __str__(self):
        return self.name


# class AnimalImage(models.Model):
#     image = models.ImageField(upload_to='animal')
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

