FROM alpine:3.8
WORKDIR /opt/pipwa

ENV LIBRARY_PATH=/lib:/usr/lib \
    PROJECT_DIR=/opt/pipwa \
    APP_DIR=/opt/pipwa/uploader \
    PYTHONPATH=/opt/pipwa \
    WORKER_COUNT=3

RUN apk add --no-cache --progress python3 python3-dev build-base jpeg-dev zlib-dev \
    && rm -rf /var/cache/apk/

RUN pip3 install -U pip gunicorn

COPY reqs/base.txt /tmp/requirements.txt
RUN pip3 install --upgrade -r /tmp/requirements.txt

ADD uploader ${APP_DIR}/

CMD gunicorn -w ${WORKER_COUNT} uploader.main:app -b 0.0.0.0:7777 --worker-class aiohttp.worker.GunicornWebWorker
EXPOSE 7777