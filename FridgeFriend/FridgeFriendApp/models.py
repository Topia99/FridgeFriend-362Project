from django.db import models
from django.conf import settings

class User(models.Model):
    phone = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Fridge(models.Model):
    fridge_name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class UserFridge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)
    
class Category(models.Model):
    DAIRY = 'D'
    FRUIT = 'F'
    VEGETABLE = 'V'
    MEAT = 'M'
    EGG = 'E'
    SEAFOOD = 'S'
    COOKED_FOOD = 'CF'
    MANUFACTURE_PRODUCT = 'MP'
    OTHERS = 'O'


    CATEGORY_CHOICES = [
       (DAIRY, 'Dairy'),
       (FRUIT, 'Fruit'),
       (VEGETABLE, 'Vegetable'),
       (MEAT, 'Meat'),
       (EGG, 'Egg'),
       (SEAFOOD, 'Seafood'),
       (COOKED_FOOD, 'Cooked food'),
       (MANUFACTURE_PRODUCT, 'Manufacture Profuct'),
       (OTHERS, 'Others'),
    ]

    category_name = models.CharField(max_length=26, choices=CATEGORY_CHOICES, default='Others')
    days_last = models.SmallIntegerField()

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveSmallIntegerField()
    expiry_date = models.DateField(null=True)
    fridge = models.ForeignKey(Fridge, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class ItemStatus(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    freeze = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
