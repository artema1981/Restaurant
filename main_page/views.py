from django.shortcuts import render
from .models import DishCategory, Dish
from django.http import HttpResponse
# Create your views here.
def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special': specials_dishes
    })
    # return HttpResponse('\n'.join(map(str, categories)) + '\n'.join(map(str, dishes)))
