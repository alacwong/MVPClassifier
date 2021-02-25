FROM python:3.7-slim

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update && \
    pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/:/usr/src/app/data:/usr/src/app/server"

EXPOSE 5000

ENTRYPOINT ["gunicorn","--workers=2", "wsgi:application", "-b", "0.0.0.0:5000"]