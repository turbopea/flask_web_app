FROM python
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=pass
WORKDIR /home/app

COPY docker/requirements.txt .

RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "server.py"]
