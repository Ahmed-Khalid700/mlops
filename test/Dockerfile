FROM python

ADD . /app

WORKDIR /app

RUN pip install -r requirement.txt

CMD [ "uvicorn" , "app:app", "--host", "0.0.0.0", "--port", "8000"]