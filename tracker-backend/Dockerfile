FROM python:3.9

WORKDIR /app

RUN pip3 install gunicorn==20.1.0 
COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .


CMD ["gunicorn", "tracker_app.wsgi", "--bind", "0.0.0.0:8000"]
