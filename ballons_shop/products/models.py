from django.db import models
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return sef.name


class Product(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(max_length=255, verbose_name='Наименование товара')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение товара')
    description = models.TextField(verbose_name='Описание товара', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена товара')
    category = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BallonsSetProduct(Product):

    class Meta:
        verbose_name = 'Набор из шаров'
        verbose_name_plural = 'Наборы из шаров'

    first_value = models.CharField(max_length=255, verbose_name='Первая характеристика')
    second_value = models.CharField(max_length=255, verbose_name='Вторая характеристика')
    third_value = models.PositiveIntegerField(verbose_name='Третья характеристика')


class SomeOtherProduct(Product):

    class Meta:
        verbose_name = 'Другой продукт'
        verbose_name_plural = 'Другие продукты'

    first_value = models.CharField(max_length=255, verbose_name='Первая характеристика')
    second_value = models.CharField(max_length=255, verbose_name='Вторая характеристика')
    third_value = models.PositiveIntegerField(verbose_name='Третья характеристика')






