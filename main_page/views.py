from django.shortcuts import render
from .models import DishCategory, Dish, Events, Gallery, Whuus
from django.http import HttpResponse
import random
# Create your views here.
def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    gallery_photos = list(Gallery.objects.filter(is_visible=True))
    gallery_photos = random.sample(gallery_photos, 8)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special': specials_dishes,
        'events': events,
        'gallery_photos': gallery_photos,
    })
    # return HttpResponse('\n'.join(map(str, categories)) + '\n'.join(map(str, dishes)))
