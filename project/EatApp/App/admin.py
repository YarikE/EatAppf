from django.contrib import admin

from .models import User, Dish, Order, OrderedDish

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name']
    search_fields = ['user_name']

class DishAdmin(admin.ModelAdmin):
    list_display = ['dish_name', 'dish_compose', 'dish_price']
    list_display_links = ['dish_name', 'dish_compose']
    search_fields = ['dish_name', 'dish_compose']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_id', 'order_date']
    search_fields = ['pk', 'order_date']


class OrderedDishAdmin(admin.ModelAdmin):
    list_display = ['dish_id', 'order_id', 'dish_count', 'dish_now_price']
    search_fields = ['dish_id', 'order_id']


admin.site.register(User, UserAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedDish, OrderedDishAdmin)
