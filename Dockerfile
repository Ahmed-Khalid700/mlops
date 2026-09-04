FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY . .

RUN uv pip install --system .


EXPOSE 8000

CMD ["python", "src/app/main.py"]