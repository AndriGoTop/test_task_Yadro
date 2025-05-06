FROM python:3.11-slim

COPY . .

RUN pip install -r requiremets.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
