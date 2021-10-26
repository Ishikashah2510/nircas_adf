from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def validate_existence(value):
    if FoodItems.objects.filter(name__iexact=value).exists():
        raise ValidationError(
            'Sorry, item already exists'
        )


class FoodItems(models.Model):
    category_choices = [
        ('Punjabi', 'Punjabi'),
        ('Chinese', 'Chinese'),
        ('Sandwich', 'Sandwich'),
        ('Fast food', 'Fast food'),
        ('South Indian', 'South Indian'),
        ('Breakfast', 'Breakfast')
    ]

    name = models.CharField(max_length=100, unique=True, validators=[validate_existence])
    cost = models.FloatField()
    description = models.CharField(max_length=160)
    serves = models.IntegerField()
    rating = models.FloatField(default=5)
    category = models.CharField(max_length=100,
                                choices=category_choices,
                                default='Punjabi')
    photo = models.ImageField(upload_to='food/',
                              default='food/default_food.jfif')

    def __str__(self):
        return self.name


class EverydayOffers(models.Model):
    discount = models.FloatField()
    food_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
