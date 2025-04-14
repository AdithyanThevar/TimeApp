FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 9000

CMD ["python", "app.py"]
