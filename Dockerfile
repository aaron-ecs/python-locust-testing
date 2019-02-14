FROM python:3

WORKDIR /python-locust-testing

COPY . ./

RUN pip install --upgrade pip
RUN pip install locustio