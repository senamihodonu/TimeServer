FROM ubuntu

RUN apt-get update

RUN apt-get remove default-jdk default-jre

RUN apt-get install -y python3

RUN apt-get update

RUN apt-get install -y git

RUN apt-get install -y net-tools

RUN (git clone https://github.com/senamihodonu/PythonProjects.git)

RUN /usr/sbin/ifconfig

CMD ["python3", "./PythonProjects/timeserver/time_server.py"]









