FROM python:3.8-alpine
COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN apk add --update \
    && pip install --upgrade pip  \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*
COPY ./app /app
EXPOSE 5000
CMD ["python", "app.py"]