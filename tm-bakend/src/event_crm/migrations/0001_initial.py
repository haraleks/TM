# Generated by Django 3.1 on 2020-09-27 11:01

from django.db import migrations, models
import django.db.models.deletion
import tm.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название события')),
                ('start_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала мероприятия')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания мероприятия')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание события')),
                ('is_free_event', models.BooleanField(default=False, verbose_name='Бесплатное мероприятие')),
                ('price', models.IntegerField(null=True, verbose_name='Стоимость')),
                ('image', models.ImageField(blank=True, default='', upload_to=tm.utils.path_to_upload_file, verbose_name='Картинка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активнен ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Удален')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятий',
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=128, verbose_name='Телефон')),
                ('comment', models.CharField(blank=True, max_length=500, verbose_name='Комментарий')),
                ('is_whatsapp', models.BooleanField(default=False, verbose_name='Есть Whatsapp')),
                ('is_telegram', models.BooleanField(default=False, verbose_name='Есть Телеграм')),
                ('is_nlp_club', models.BooleanField(default=False, verbose_name='Есть в общем чате клуба НЛП')),
                ('is_agree', models.BooleanField(default=True, verbose_name='Подписан на рассылку')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Удален')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='PartEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название события')),
                ('start_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала мероприятия')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания мероприятия')),
                ('price', models.IntegerField(null=True, verbose_name='Стоимость')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание события')),
                ('image', models.ImageField(blank=True, default='', upload_to=tm.utils.path_to_upload_file, verbose_name='Картинка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Удален')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='part_event', to='event_crm.event', verbose_name='Блок мероприятия')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоков',
            },
        ),
        migrations.CreateModel(
            name='RegistrationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(default=False, verbose_name='Бесплатный вход')),
                ('amount', models.IntegerField(null=True, verbose_name='Стоимость')),
                ('is_confirm', models.BooleanField(default=False, verbose_name='Подтвердил присутствие')),
                ('is_payed', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('is_messenger', models.BooleanField(default=False, verbose_name='Отправили сообщение в месенджерах')),
                ('is_sms', models.BooleanField(default=False, verbose_name='Отправили сообщение в sms')),
                ('is_come', models.BooleanField(default=False, verbose_name='Пришел')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Удален')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='registration_event', to='event_crm.event', verbose_name='Мероприятие')),
                ('event_participant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='registration_event', to='event_crm.eventparticipant', verbose_name='Участник мероприятия')),
                ('part_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='registration_event', to='event_crm.partevent', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Регистрация на мероприятии',
                'verbose_name_plural': 'Регистрации на мероприятии',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True, verbose_name='Стоимость')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('bank_card', 'карта банка')], max_length=50, verbose_name='Тип оплаты')),
                ('date_payments', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Удален')),
                ('registration_event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='payments', to='event_crm.registrationevent', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплат',
            },
        ),
    ]
