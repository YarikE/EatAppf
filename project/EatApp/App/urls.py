from django.urls import path
from .views import UserApiView, DishApiView, get_random_dish, put_users_choice, get_history_by_name, get_date_report

urlpatterns = [
    path('user_view/', UserApiView.as_view()),
    path('dish_view/', DishApiView.as_view()),
    path('random_dish/', get_random_dish),
    path('put_users_choice/', put_users_choice),
    path('history/', get_history_by_name),
    path('report/', get_date_report),
]
