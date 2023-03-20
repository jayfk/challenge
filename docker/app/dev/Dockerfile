FROM python:3.9.7-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # packages to build other Python packages
  && apt-get install -y build-essential \
  # postgres requirements
  && apt-get install -y libpq-dev \
  # pango // weasyprint
  && apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev \
  && apt-get install -y socat \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# app entrypoint
COPY ./docker/app/dev/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

RUN mkdir -p /data/media

# install requirements here to make sure they are cached
COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt

WORKDIR /app
ENTRYPOINT ["/entrypoint"]
