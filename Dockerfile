FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python-all-dev \
    libpq-dev \
    libgeos-dev \
    wget \
    curl \
    sqlite3 \
    cmake \
    libtiff-dev \
    libcurl4-openssl-dev \
    pkg-config

RUN curl https://download.osgeo.org/proj/proj-8.2.1.tar.gz | tar -xz &&\
    cd proj-8.2.1 &&\
    mkdir build &&\
    cd build && \
    cmake .. &&\
    make && \
    make install

RUN wget http://download.osgeo.org/gdal/3.4.0/gdal-3.4.0.tar.gz
RUN tar xvfz gdal-3.4.0.tar.gz
WORKDIR ./gdal-3.4.0
RUN ./configure --with-python --with-pg --with-geos &&\
    make && \
    make install && \
    ldconfig

WORKDIR /code
RUN pip install --upgrade pip 
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
