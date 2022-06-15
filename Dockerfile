FROM ubuntu

RUN apt-get update

RUN apt-get remove default-jdk default-jre

RUN apt-get install -y python3

RUN apt-get update

RUN apt-get install -y git

RUN apt-get install -y net-tools

RUN (git clone https://github.com/senamihodonu/TimeServer_Python.git)

RUN /usr/sbin/ifconfig

CMD ["python3", "./TimeServer_Python/time_server.py"]









