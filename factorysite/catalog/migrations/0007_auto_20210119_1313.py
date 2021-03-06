# Generated by Django 3.1.3 on 2021-01-19 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210119_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='name',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='name',
            field=models.ForeignKey(help_text='Выберите название вакансии', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.vacancyname'),
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='vacancy_desc',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='vacancy_desc',
            field=models.ForeignKey(help_text='Описание вакансии', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.vacancydescribe'),
        ),
    ]
