FROM ubuntu
RUN sed -i s/http/ftp/ /etc/apt/sources.list && apt-get update
RUN apt-get -y install python-pip python-dev libmysqlclient-dev git nano tzdata
RUN pip install MySQL-python
RUN git clone https://github.com/vsirius/python-project.git 
ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ENTRYPOINT python /python-project/server.py
