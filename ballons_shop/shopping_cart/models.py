from django.db import models
from products.models import Product
from users.models import Customer
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class CartProduct(models.Model):

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    user = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey('ShoppingCart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return f'Продукт {self.product.title} (для корзины)'


class ShoppingCart(models.Model):

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    owner = models.ForeignKey(Customer, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_cart_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена корзины')

    def __str__(self):
        return str(self.id)