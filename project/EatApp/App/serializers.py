from rest_framework import serializers
from .models import User, Dish

class UserApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'user_name')


class DishApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('pk', 'dish_name', 'dish_compose', 'dish_price')
