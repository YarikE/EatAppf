from django.db import models


# Сотрудник
class User(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='cотрудник')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'cотрудник'
        verbose_name_plural = 'cотрудники'


# Блюдо
class Dish(models.Model):
    dish_name = models.TextField(null=True, blank=True, verbose_name='название блюда')
    dish_compose = models.TextField(null=True, blank=True, verbose_name='описание блюда')
    dish_price = models.IntegerField(null=False, verbose_name='цена блюда')

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'
        ordering = ['dish_price']


# Заказ
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='имя сотрудника')
    order_date = models.DateField(null=False, verbose_name='дата заказа')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['order_date', 'pk']




# Блюдо заказа
class OrderedDish(models.Model):
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='блюдо')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')
    dish_count = models.IntegerField(null=False, default=1, verbose_name='кол-во блюд')
    dish_now_price = models.IntegerField(null=False, default=50, verbose_name='цена блюда на момент заказа')


    class Meta:
        verbose_name = 'блюдо заказа'
        verbose_name_plural = 'блюда заказов'

    def __str__(self):
        return f'Заказ {self.order_id}'
