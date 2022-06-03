from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)



class Drink(models.Model):
    name = models.CharField(max_length=256)
    menu = models.ManyToManyField(Category)


#
# class Category(models.Model):
#     menu = models.ForeignKey(Drink, on_delete=models.CASCADE)