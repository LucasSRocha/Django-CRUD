from django.db import models


class Categories(models.Model):

    category = models.CharField(unique=True, max_length=254)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"

        verbose_name_plural = "Categories"


class Shoes(models.Model):

    price = models.FloatField()

    size = models.CharField(max_length=20)

    color = models.CharField(max_length=254)

    shoes_stock = models.IntegerField(default=0)

    shoes_bought = models.IntegerField(default=0)

    shoe_model = models.CharField(max_length=254)

    shoe_brand = models.CharField(max_length=254, blank=True)

    class_category = models.ManyToManyField('Categories')

    @property
    def remaining_shoes(self):
        return self.shoes_stock - self.shoes_bought

    def __str__(self):
        return self.shoe_model

    class Meta:
        verbose_name = "Shoe"

        verbose_name_plural = "Shoes"

        unique_together = ['shoe_model', 'color', 'size']
