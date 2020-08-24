from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField('Название события', blank=False, max_length=200)
    #TODO сделать поля DateTimeField
    start_at = models.CharField('Открывается', blank=True, null=True, max_length=155)
    end_at = models.CharField('Закрывается', blank=True, null=True, max_length=155)

    is_active = models.BooleanField('Статус программы', null=False, default=True)

    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    deleted_at = models.DateTimeField('Удален', null=True, default=None, blank=True)