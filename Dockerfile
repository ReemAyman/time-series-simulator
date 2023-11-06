FROM python:3.8
WORKDIR /simulator
COPY requirements.txt /simulator
RUN python3 -m pip install -r requirements.txt

COPY . /simulator
