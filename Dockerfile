FROM python:3.9

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 7777

WORKDIR /app

CMD ["python", "server.py"]
