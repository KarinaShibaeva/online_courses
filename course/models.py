from django.db import models

class Teacher(models.Model):
    surname = models.CharField(max_length=128, verbose_name='Фамилия')
    name = models.CharField(max_length=128, verbose_name='Имя')
    patronymic = models.CharField(max_length=128, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.surname


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена курса')
    level = models.CharField(max_length=128, verbose_name='Уровень сложности')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    age = models.CharField(max_length=128, verbose_name='Возрастная категория')
    image = models.ImageField(upload_to="%Y/%m/%d", verbose_name='Изображение')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Спикер')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

