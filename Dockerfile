# FROM python:3.11-slim

# WORKDIR /app

# ENV PYTHONPATH=/app

# RUN pip install --no-cache-dir uv

# COPY . .

# RUN uv pip install --system .


# EXPOSE 8000

# CMD ["python", "src/app/main.py"]


FROM alpine

LABEL des="RUN VS CMD"

RUN echo "Build Time"

CMD ["echo",  "Run Time"]