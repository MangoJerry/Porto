from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField('Название', max_length=50)
    content = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/')
    photo1 = models.ImageField('Фото1', upload_to='photos/%Y/%m/', null=True,)
    photo2 = models.ImageField('Фото2', upload_to='photos/%Y/%m/', null=True,)
    price = models.CharField('Цена', max_length=10)
    subcat = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True, verbose_name='Подкатегория')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_id': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    name = models.CharField('Подкатегория', max_length=15)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcat', kwargs={'subcat_id': self.pk})

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
