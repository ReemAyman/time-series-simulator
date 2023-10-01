FROM python:3
WORKDIR /simulator
COPY requirements.txt /simulator
RUN pip install -r requirements.txt

COPY . /simulator
