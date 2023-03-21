from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


AVAI = (
    ('В наличии', 'yes'),
    ('Нет в наличии', 'no')
)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.CharField(max_length=50, choices=AVAI)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
