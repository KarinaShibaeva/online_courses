from django.db import models

class Appeal(models.Model):
    TYPES = (
        ('Основы бизнеса и предпринимательства', 'Основы бизнеса и предпринимательства'),
        ('Цифровой маркетинг и реклама в Интернете', 'Цифровой маркетинг и реклама в Интернете'),
        ('Финансовый рынок и инвестиционные стратегии', 'Финансовый рынок и инвестиционные стратегии'),
        ('Искусство цвета и композиции', 'Искусство цвета и композиции'),
        ('Python для начинающих', 'Python для начинающих'),
        ('Французский язык и культура', 'Французский язык и культура'),
        ('Психология управления временем и эффективности', 'Психология управления временем и эффективности'),
    )

    STATUS_CHOICE = (
        ("a", "В обработке"),
        ("b", "Выполнено"),
        ("c", "Отклонено")
    )

    course_name = models.CharField(choices=TYPES, max_length=128, verbose_name='Название курса')
    contact = models.CharField(max_length=128, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта", blank=False)
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICE)
    uid = models.CharField(max_length=64, blank=False, null=False, db_index=True, unique=True)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name, field.value_to_string(self)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'