# Generated by Django 3.1.3 on 2021-01-19 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210113_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.OneToOneField(help_text='Введите название вакансии', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.vacancyname'),
        ),
    ]