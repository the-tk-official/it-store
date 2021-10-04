from django.db import models
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наз-ние продукта')
    content = models.TextField(blank=True, verbose_name='Контент')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse(viewname='view_product', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-added_at']

class Categories(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименовании категории')

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']