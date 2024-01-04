# Generated by Django 4.2.7 on 2023-12-10 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('career_toolbox', '0002_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Почта')),
                ('last_evaluation_date', models.DateField(blank=True, null=True, verbose_name='Дата последней оценки')),
                ('course', models.ManyToManyField(blank=True, related_name='user_course', to='career_toolbox.course', verbose_name='Курсы пользователя')),
                ('grades', models.ManyToManyField(related_name='user_grades', to='career_toolbox.grade', verbose_name='Грейды пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0, verbose_name='Уровень навыка')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career_toolbox.skill', verbose_name='Навык')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skills', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(related_name='users', through='users.UserSkill', to='career_toolbox.skill', verbose_name='Навыки пользователя'),
        ),
        migrations.AddField(
            model_name='user',
            name='specializations',
            field=models.ManyToManyField(related_name='user_specializations', to='career_toolbox.specialization', verbose_name='Специализации пользователя'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
