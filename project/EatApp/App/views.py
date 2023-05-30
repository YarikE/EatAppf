from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .serializers import UserApiViewSerializer, DishApiViewSerializer
from .models import User, Dish, Order, OrderedDish

import json
import random


# API User
class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserApiViewSerializer


# API Dish
class DishApiView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishApiViewSerializer


# Случайные блюда для режима "Мне повезет"
@csrf_exempt
def get_random_dish(request):

    if request.method == 'POST':
        json_data = []
        data = json.loads(request.body)
        dish_count_choice = data['dish_count_choice']  # Кол-во случайных блюд, которое выбрал пользователь

        while len(json_data) != dish_count_choice:
            max_size = Dish.objects.all().count()
            random_id = random.randint(1, max_size)
            current_dish = Dish.objects.get(pk=random_id)

            data = {
             'dish_name': current_dish.dish_name,
             'dish_compose': current_dish.dish_compose,
             'dish_price': current_dish.dish_price,
             'dish_count': 1,
             'pk': current_dish.pk
            }
            if data not in json_data:
                json_data.append(data)

        return JsonResponse({'dish_list': json_data})
    
    else: 
        return HttpResponse('Страница не найдена', status=404)

# Оформление заказа, который сформировал пользователь (сохранение заказа)
@csrf_exempt
def put_users_choice(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user_id = User.objects.get(user_name=data['user_name'])
        order_date = data['order_date']

        order_object = Order.objects.create(user_id=user_id, order_date=order_date)

        for dish_item in data['dish_list']:
            order_id = order_object
            dish_id = Dish.objects.get(pk=dish_item['pk'])
            dish_count = dish_item['dish_count']
            dish_now_price = dish_item['dish_price']

            OrderedDish.objects.create(dish_id=dish_id, order_id=order_id, dish_count=dish_count, dish_now_price=dish_now_price)

        return HttpResponse('Good')

    else:
        return HttpResponse('Страница не найдена', status=404)

# Получение истории заказов пользователя
@csrf_exempt
def get_history_by_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_name = data['user_name']  # Имя, которое выбрал пользователь

        user = User.objects.get(user_name=user_name)

        orders = Order.objects.filter(user_id=user)

        json_data = {'orders': []}

        full_orders_price: int = 0

        for order in orders:

            current_ordered_dish = OrderedDish.objects.filter(order_id=order.pk)
            orders_price = 0

            dish_list = []

            for dish in current_ordered_dish:
                orders_price += dish.dish_now_price * dish.dish_count  # Цена 1 заказа

                count_dish = {'dish_name': dish.dish_id.dish_name,     # Имя продукта
                              'dish_count': dish.dish_count,           # Кол-во продукта
                              'dish_now_price': dish.dish_now_price}   # Цена еды на момент заказа
                dish_list.append(count_dish)

            full_orders_price += orders_price  # Цена всех заказов вместе

            order_count = {'order_date': str(order.order_date),
                           'dishes': dish_list,
                           'order_price': orders_price}
            json_data['orders'].append(order_count)

        # json_data -
        # {'orders': [{'order_date': '2023-05-05',
        #               'dishes': [{'dish_name': 'Аши',
        #                           'dish_count': 1,
        #                           'dish_now_price': 1000}],
        #               'order_price': 1000},

        #               {'order_date': '2023-05-05',
        #               'dishes': [{'dish_name': 'Блины готовые',
        #                           'dish_count': 2,
        #                           'dish_now_price': 100}],
        #                'order_price': 200},
        #
        #                {'order_date': '2023-05-05',
        #                'dishes': [{'dish_name': 'Блины готовые',
        #                            'dish_count': 3,
        #                            'dish_now_price': 50}],
        #                            'order_price': 150}]}

        return JsonResponse(json_data)

    else:
        return HttpResponse('Страница не найдена', status=404)


# Отчет "заказы на дату"
@csrf_exempt
def get_date_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data['data_choice']  # Дата пользователя

        current_orders = Order.objects.filter(order_date=date)

        result_json = {}

        for order in current_orders:
            current_dishes = OrderedDish.objects.filter(order_id=order.pk)
            for dish in current_dishes:
                if dish.dish_id.dish_name not in result_json.keys():
                    result_json[dish.dish_id.dish_name] = {'dish_count': dish.dish_count, 'dish_now_price': dish.dish_id.dish_price}
                else:
                    result_json[dish.dish_id.dish_name]['dish_count'] += dish.dish_count

        return JsonResponse(result_json)
    
    else:
        return HttpResponse('Страница не найдена', status=404)
