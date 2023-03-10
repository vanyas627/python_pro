import decimal

from django.db import models

class DishCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for dish in self.dishes.all():
            yield dish


    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ('position',)

class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes',)
    ingredients = models.CharField(max_length=100, unique=True)
    desc = models.TextField(max_length=200,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discounter = models.PositiveSmallIntegerField(default=0)
    is_special = models.BooleanField(default=False)
    is_signature = models.BooleanField(default=False)


    def total_price(self):
        return self.price - (self.price * decimal.Decimal(self.discounter / 100))

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.title}'

class AboutRes(models.Model):
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(max_length=2000, blank=False)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.desc}"


class Services(models.Model):
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.title}'

class Gallery(models.Model):
    title = models.CharField(max_length=50, blank=True)
    photo = models.ImageField()
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.title}'
