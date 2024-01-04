<a id="anchor"></a>
<div align=center>

  # Проект Трекер развития

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
  
</div>

## Описание проекта

Проект для образовательной платформы Яндекс Практикум.

Этот проект добавляет новый функционал к сервису карьерный трекер. Благодаря этому проекту можно узнать свой текущий уровень навыков и грейд, посмотреть список навыков необходимых для развития, ознакомится с рекомендациями курсов, проектами Мастерской и ресурсами Базы знаний.

Пользователям доступна возможность выбора специальности и прохождение теста, чтобы узнать текущий уровень навыков, а также ознакомиться с рекомендациями, чтобы в дальнейшем повысить свой уровень компетенций.

Кроме того, на основе выбранной специальности и результатах пройденного теста формируются рекомендации на курсы яндекс практикума, проекты мастерской и ресурсы базы знаний.

Для доступа к функционалу требуется пройти бесплатную регистрацию.

### Технологии

[**Backend**](https://github.com/Hackaton-development-tracker/tracker-backend)

* Python 3.9.10
* Django 4.2
* djangorestframework 3.14.0
* Djoser 2.2

### Инфраструктура: 

* Docker
* NGINX
* GUNICORN
* база даннных POSTGRESQL

### Основные библиотеки:

- аутентификация Djoser
- документация drf-yasg

### Запуск проекта:

1. Cклонировать проект:
```bash
git clone git@github.com:JustLight1/Hackaton-development-tracker.git
```

2. При первом запуске для функционирования проекта обязательно установить виртуальное окружение, установить зависимости, выполнить миграции:
```bash
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
```

3. Установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

4. Выполните миграции БД. Из папки tracker-backend с файлом manage.py выполните команду:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Для создания суперюзера из папки tracker-backend с файлом manage.py выполните команду:
```bash
python manage.py createsuperuser
```

6. Для запуска сервера из папки backend с файлом manage.py выполните команду:
```bash
python manage.py runserver
```

7. Проект будет доступен по адресу `http://localhost:8000/`


### Документация

Доступна после запуска сервиса:

**swagger** - `http://localhost:8000/swagger/`  
**redoc** - `http://localhost:8000/redoc/`

### Заполнение бд
Для грейдов обязательные названия **Джуниор**, **Мидл**, **Сеньор**.
Остальные данные заполняются по своему усмотрению.

## Сервис разрабатывал:

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)


_[Вверх](#anchor)_
