# Generated by Django 4.2.7 on 2023-12-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_last_evaluation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test_unavailable_until',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Тест недоступен до'),
        ),
    ]
