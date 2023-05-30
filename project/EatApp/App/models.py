from django.db import models


# Сотрудник
class User(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='Сотрудник')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# Блюдо
class Dish(models.Model):
    dish_name = models.TextField(null=True, blank=True, verbose_name='Название блюда')
    dish_compose = models.TextField(null=True, blank=True, verbose_name='Описание блюда')
    dish_price = models.IntegerField(null=False, verbose_name='Цена блюда')

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['dish_price']


# Заказ
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Имя сотрудника')
    order_date = models.DateField(null=False, verbose_name='Дата заказа')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['order_date', 'pk']




# Блюдо заказа
class OrderedDish(models.Model):
    dish_id = models.ForeignKey(Dish, on_delete=models.PROTECT, verbose_name='Блюдо')
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    dish_count = models.IntegerField(null=False, default=1, verbose_name='Кол-во блюд')
    dish_now_price = models.IntegerField(null=False, default=50, verbose_name='Цена блюда на момент заказа')


    class Meta:
        verbose_name = 'Блюдо заказа'
        verbose_name_plural = 'Блюда заказов'

    def __str__(self):
        return f'Заказ {self.order_id}'
