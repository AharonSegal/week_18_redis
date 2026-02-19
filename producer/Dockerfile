FROM python:3.12-slim

WORKDIR /app

COPY producer/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY producer/ ./

COPY data/ ./data/

CMD ["python", "main.py"]