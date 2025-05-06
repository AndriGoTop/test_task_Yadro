FROM python:3.11-slim

COPY . .

RUN pip install -r requiremets.txt

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8080"]
