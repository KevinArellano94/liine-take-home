# syntax=docker/dockerfile:1
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask==2.1.*

WORKDIR /app

COPY . /app

RUN pip3 install flask==2.1.*

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["app.py"]