FROM alpine:3.8

ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk add --no-cache --progress python3 python3-dev build-base libffi-dev openssl-dev \
    && rm -rf /var/cache/apk/

RUN pip3 install -U pip gunicorn

COPY reqs/base.txt /tmp/requirements.txt
RUN pip3 install --upgrade -r /tmp/requirements.txt

ADD ./storage .

CMD gunicorn -w 1 storage.main:application -b 0.0.0.0:7777 --worker-class aiohttp.worker.GunicornWebWorker
EXPOSE 7777