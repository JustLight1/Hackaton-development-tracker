# Generated by Django 4.2.7 on 2023-12-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontest',
            name='param',
            field=models.CharField(choices=[('one', 'Один вариант ответа'), ('several', 'Несколько вариантов ответа')], default=1, max_length=10, verbose_name='Тип вопроса'),
            preserve_default=False,
        ),
    ]
