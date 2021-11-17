FROM python:3.10-slim AS builder

WORKDIR /workspace

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --dev -o requirements-dev.txt


FROM python:3.10-slim AS local

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y gcc gettext libgettextpo-dev libpcre3-dev

WORKDIR /django

COPY --from=builder /workspace/requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt --no-cache-dir

EXPOSE 8000
