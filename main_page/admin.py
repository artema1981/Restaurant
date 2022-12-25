from django.contrib import admin
from .models import DishCategory, Dish, Events, Gallery, Whuus
# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(Whuus)
admin.site.register(Gallery)