FROM python:3.11

WORKDIR /app

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

CMD ["python", "manage.py", "runserver"]
# ENTRYPOINT ["/app/entrypoint.sh"]