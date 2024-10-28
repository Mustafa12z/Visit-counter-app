# Build stage
FROM python:3.9-slim as Build

WORKDIR /app

COPY . .

RUN pip install flask redis

EXPOSE 5002

CMD ["python", "app.py"]


