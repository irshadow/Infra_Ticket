FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .


RUN apt-get update && apt-get upgrade
RUN rm -rf /var/lib/apt/lists/*

COPY . .


RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]