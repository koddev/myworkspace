FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir logs 
RUN mkdir data 
VOLUME /data

COPY *.py ./

CMD ["python", "-u", "/usr/src/app/test.py"]
