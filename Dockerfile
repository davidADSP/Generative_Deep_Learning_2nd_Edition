FROM python:3.9.0-slim

RUN apt-get update
RUN apt-get install -y unzip

RUN pip install --upgrade pip

RUN useradd -m gdl
ENV PATH="/home/gdl/.local/bin:${PATH}"

WORKDIR /app

RUN chown -R gdl:gdl /app

USER gdl

COPY ./requirements.txt /app
RUN pip install --user -r /app/requirements.txt

COPY /models/. /app/models
COPY /utils/. /app/utils
COPY /notebooks/. /app/notebooks
COPY /scripts/. /app/scripts

COPY /setup.cfg /app

ENV PYTHONPATH="${PYTHONPATH}:/app"