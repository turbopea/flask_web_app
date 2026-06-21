FROM python

WORKDIR /home/app

COPY . . 

RUN pip install -r docker/requirements.txt
COPY . .

CMD ["python3", "server.py"]
