FROM python:3-alpine3.10

RUN python -m pip install dnspython

ENV ADDRESS_LIST "google.com|twitter.com|some.garbage.web.site"
ENV NAME_SERVER_LIST "1.1.1.1|8.8.8.8"

WORKDIR /app
COPY . /app

ENTRYPOINT ["python", "main.py"]