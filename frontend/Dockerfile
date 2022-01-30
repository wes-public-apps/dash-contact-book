
FROM python:3.8-slim

RUN apt update
RUN apt upgrade -y
RUN apt -y install libpq-dev gcc
WORKDIR /
COPY requirements.txt /
RUN pip install -r /requirements.txt && rm -rf /root/.cache
COPY app /app
ENTRYPOINT ["python3", "-m", "app.contact_app"]