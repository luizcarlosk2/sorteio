FROM python:3.11-rc-alpine3.15
#FROM python:3.10.7-buster
WORKDIR /
ADD ./app /app
#RUN pip install xx
WORKDIR /app
#CMD ["pwd"]
#CMD ["ls"]
ENTRYPOINT ["python","-u", "./main.py"]

