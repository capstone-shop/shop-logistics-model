FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 애플리케이션 실행 명령
CMD ["uvicorn", "is_advertise:app", "--host", "0.0.0.0", "--port", "8000"]
