# TimeServer 

* Author: Senami Hodonu


## Overview

The goal of this project is to build a time server application over a network
using socket programming. This project includes a server program and client
program. Once the server is deployed, a client can request the current time
from this server. Additionally a Docker recipe is included to aid in the 
deployment of the server.

## Building the code

### Server

For the server, run the server using the command:

$ python3 time-server.py

	OR

$ ./run-server

### Using Docker image:

From the directory containing the Dockerfile create the docker image
using the command:

$ sudo docker build -t <YourDockerImageName> .

The images can be listed with the following command:

$ sudo docker image ls

Run the docker Timeserver with the following command:

$ sudo docker run -it --rm --name <instance name> <YourDockerImageName>


A running instance can be stopped with the following command:

$ sudo docker stop <instance name>

A running instance can be killed with the following command:

$ sudo docker kill <instance name>

The list of the running instances can be got with the following command:

$ sudo docker ps

### Client

For the client, run the client (on same or another machine):

$ python3 time-client.py <serverhost> 

	OR

$ ./run-client <serverhost>
