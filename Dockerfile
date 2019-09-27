FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential git
RUN apt-get install -y vim

RUN apt-get install -y python3.6 python3-pip

RUN pip3 install numpy 
RUN pip3 install matplotlib

RUN mkdir ~/src

RUN git clone https://github.com/cseydlitz/phys434.git ~/src 


