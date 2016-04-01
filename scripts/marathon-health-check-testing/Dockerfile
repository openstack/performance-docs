FROM python:2

RUN /bin/sh -c 'mkdir -p /usr/src/app'

ADD server.py /usr/src/app/server.py

WORKDIR /usr/src/app

CMD ["python", "./server.py"]
