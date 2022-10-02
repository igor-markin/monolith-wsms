FROM python:3.10.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project

RUN apt update

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .