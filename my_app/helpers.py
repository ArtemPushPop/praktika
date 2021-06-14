import random
from .models import Picture

random.seed()


def get_random_picture(pictures: [Picture]):
    if Picture.objects.count() - 1 >= 0:
        rand = random.randint(0, Picture.objects.count() - 1)
        return Picture.objects.all()[rand].picture.name
    else:
        return None
