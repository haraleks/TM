from django.db import models
from tm.utils import path_to_upload_file
from event_crm.models.utils import PaymemntsTypes
from ckeditor_uploader.fields import RichTextUploadingField


class Event(models.Model):
    name = models.CharField(
        'Название события', blank=False, max_length=200)
    start_at = models.DateTimeField(
        'Дата начала мероприятия', blank=True, null=True)
    end_at = models.DateTimeField(
        'Дата окончания мероприятия', blank=True, null=True)
    description = RichTextUploadingField()
    is_free_event = models.BooleanField(
        'Бесплатное мероприятие', default=False)
    price = models.IntegerField(
        'Стоимость', null=True)
    image = models.ImageField(
        'Картинка', upload_to=path_to_upload_file, height_field=None, width_field=None,
        max_length=None, default='', blank=True)

    is_active = models.BooleanField(
        'Активнен ', null=False, default=True)

    created_at = models.DateTimeField(
        'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Обновлен', auto_now=True)
    deleted_at = models.DateTimeField(
        'Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятий'

    def __str__(self):
        return self.name


class PartEvent(models.Model):
    name = models.CharField(
        'Название события', blank=False, max_length=200)
    start_at = models.DateTimeField(
        'Дата начала мероприятия', blank=True, null=True)
    end_at = models.DateTimeField(
        'Дата окончания мероприятия', blank=True, null=True)
    price = models.IntegerField(
        'Стоимость', null=True)
    description = RichTextUploadingField()
    image = models.ImageField(
        'Картинка', upload_to=path_to_upload_file, height_field=None, width_field=None,
        max_length=None, default='', blank=True)
    event = models.ForeignKey(
        'event_crm.Event',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Блок мероприятия',
        related_name='part_event'
    )
    is_active = models.BooleanField(
        'Активен', null=False, default=True)
    created_at = models.DateTimeField(
        'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Обновлен', auto_now=True)
    deleted_at = models.DateTimeField(
        'Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоков'

    def __str__(self):
        return self.name


class RegistrationEvent(models.Model):
    event = models.ForeignKey(
        'event_crm.Event',
        on_delete=models.DO_NOTHING,
        verbose_name='Мероприятие',
        related_name='registration_event')
    part_event = models.ForeignKey(
        'event_crm.PartEvent',
        on_delete=models.DO_NOTHING,
        null=True,
        verbose_name='Блок',
        related_name='registration_event')
    event_participant = models.ForeignKey(
        'event_crm.EventParticipant',
        on_delete=models.DO_NOTHING,
        null=True,
        verbose_name='Участник мероприятия',
        related_name='registration_event')
    is_free = models.BooleanField('Бесплатный вход', default=False)
    amount = models.IntegerField('Стоимость', null=True)
    is_confirm = models.BooleanField('Подтвердил присутствие', default=False)
    is_payed = models.BooleanField('Оплачено', default=False)
    is_messenger = models.BooleanField('Отправили сообщение в месенджерах', default=False)
    is_sms = models.BooleanField('Отправили сообщение в sms', default=False)
    is_come = models.BooleanField('Пришел', default=False)

    is_active = models.BooleanField(
        'Активен', null=False, default=True)

    created_at = models.DateTimeField(
        'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Обновлен', auto_now=True)
    deleted_at = models.DateTimeField(
        'Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Регистрация на мероприятии'
        verbose_name_plural = 'Регистрации на мероприятии'

    def __str__(self):
        return f'{self.event.name} {self.part_event.name} - {self.person_event.full_name}'


class EventParticipant(models.Model):
    first_name = models.CharField(
        'Имя', max_length=300, blank=True, null=True, default='')
    last_name = models.CharField(
        'Фамилия', max_length=300, blank=True, null=True, default='')
    father_name = models.CharField(
        'Отчество', max_length=300, blank=True, null=True, default='')
    phone = models.CharField(
        'Телефон', max_length=128, blank=False, null=False)
    comment = models.CharField(
        'Комментарий', max_length=500, blank=True)
    is_whatsapp = models.BooleanField('Есть Whatsapp', default=False)
    is_telegram = models.BooleanField('Есть Телеграм', default=False)
    is_nlp_club = models.BooleanField('Есть в общем чате клуба НЛП', default=False)
    is_agree = models.BooleanField('Подписан на рассылку', default=True)

    is_active = models.BooleanField(
        'Активен', null=False, default=True)
    created_at = models.DateTimeField(
        'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Обновлен', auto_now=True)
    deleted_at = models.DateTimeField(
        'Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f'{self.full_name}'


class Payments(models.Model):
    registration_event = models.ForeignKey(
        'event_crm.RegistrationEvent',
        on_delete=models.DO_NOTHING,
        verbose_name='Мероприятие',
        related_name='payments')
    amount = models.IntegerField('Стоимость', null=True)
    payment_method = models.CharField(
        'Тип оплаты',
        max_length=50,
        choices=PaymemntsTypes.CHOISES())
    date_payments = models.DateTimeField(
        'Дата оплаты', blank=True, null=True)

    is_active = models.BooleanField(
        'Активен', null=False, default=True)
    created_at = models.DateTimeField(
        'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Обновлен', auto_now=True)
    deleted_at = models.DateTimeField(
        'Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплат'

    def __str__(self):
        return f'{self.registration_event.person_event.full_name} сумма: {amount/100}'

