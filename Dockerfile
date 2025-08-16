FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

WORKDIR /api

COPY main.py .
COPY requirements.txt .

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

RUN touch names.txt

ENTRYPOINT [ "flask", "--app", "main", "run", "--host=0.0.0.0"]