FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

# CMD ["uvicorn", "src.entrypoint.fastapi:app", "--host", "0.0.0.0", "--port", "80"]