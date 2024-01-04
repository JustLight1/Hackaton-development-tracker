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
  ![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
  ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white)
  ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

</div>

## Описание проекта

Проект выпускников _Яндекс.Практикум_ 

Этот проект добавляет новый функционал к сервису карьерный трекер. Благодаря этому проекту можно узнать свой текущий уровень навыков и грейд, посмотреть список навыков необходимых для развития, ознакомится с рекомендациями курсов, проектами Мастерской и ресурсами Базы знаний.

Пользователям доступна возможность выбора специальности и прохождение теста, чтобы узнать текущий уровень навыков, а также ознакомиться с рекомендациями, чтобы в дальнейшем повысить свой уровень компетенций.

Кроме того, на основе выбранной специальности и результатах пройденного теста формируются рекомендации на курсы яндекс практикума, проекты мастерской и ресурсы базы знаний.

Для доступа к функционалу требуется пройти бесплатную регистрацию.

### Технологии

[**Backend**](https://github.com/JustLight1/Hackaton-development-tracker/tree/main/tracker-backend)

* Python 3.9.10
* Django 4.2
* djangorestframework 3.14.0
* Djoser 2.2

[**Frontend**](https://github.com/JustLight1/Hackaton-development-tracker/tree/main/tracker-frontend)

* CSS BEM
* HTML
* React
* JS
* TypeScript

### Инфраструктура: 

* Docker
* NGINX
* GUNICORN
* база даннных POSTGRESQL

### Запуск проекта:

1. Cклонировать проект:

```bash
git clone git@github.com:JustLight1/Hackaton-development-tracker.git
```

2. В корне папки tracker-backend поместить файл .env, заполнить его по шаблону

```env
ENVIRONMENT=<production OR testing>    # testing use sqlite, pruduction use PostgreSQL

POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...
    
DB_HOST=...
DB_PORT=...
```
3. Из корневой дирректории tracker-backend запустить сборку приложения:

```bash
sudo docker compose up -d
```

4. Выполнить миграции:
```bash
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate
```

5. Сбор статики:
```bash
sudo docker compose exec backend python manage.py collectstatic
sudo docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

6. Создать суперюзера:
```bash
sudo docker-compose exec backend python manage.py createsuperuser
```

### Документация

Доступна после запуска сервиса:

**swagger** - `http://localhost:8000/swagger/`
**redoc** - `http://localhost:8000/redoc/`

### Заполнение бд
Для грейдов обязательные названия **Джуниор**, **Мидл**, **Сеньор**.
Остальные данные заполняются по своему усмотрению.