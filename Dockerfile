FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# Install system dependencies in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jdk-headless \
    git wget unzip build-essential libffi-dev libssl-dev ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install pip packages with retries
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip install --no-cache-dir cython

RUN pip install --no-cache-dir buildozer

RUN pip install --no-cache-dir kivy

WORKDIR /app

COPY main.py .
COPY buildozer.spec .

RUN mkdir -p bin

CMD ["buildozer", "android", "debug"]
