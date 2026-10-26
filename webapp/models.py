from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Название",
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Название'
    )

    description = models.TextField(
        null=False,
        blank=True,
        verbose_name='Описание'
    )

    category = models.ForeignKey(
        'webapp.Category',
        related_name='products',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Категория'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Стоимость'
    )

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.name
    