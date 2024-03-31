FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip

#RUN pip install Flask PyMySQL flask-sqlalchemy Flask-Migrate cryptography Flask-Testing
RUN pip install --no-cache-dir -r requirements.txt

RUN python test.py