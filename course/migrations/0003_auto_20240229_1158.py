# Generated by Django 3.2 on 2024-02-29 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20240229_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher', verbose_name='Спикер'),
        ),
    ]
