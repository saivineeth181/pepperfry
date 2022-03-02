FROM python:3.9.5
ENV PYTHONBUFFRED=1

WORKDIR /task1
ADD . /task1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY  . /task1/

