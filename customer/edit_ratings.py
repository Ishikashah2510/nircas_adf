from .models import *
from manager.models import *


def edit_ratings(ratings):
    for item, rating in ratings.items():
        old_rating = float(item.rating)
        rating = float(rating)
        n = ItemQuantity.objects.filter(food_id=item)
        n = len(n)
        new_rating = (old_rating * n + rating) / (n + 1)
        item.rating = new_rating
        item.save()
