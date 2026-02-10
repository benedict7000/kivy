FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    android-sdk \
    android-sdk-build-tools \
    git \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install buildozer and dependencies
RUN pip3 install buildozer cython kivy kivymd

# Set Android SDK path
ENV ANDROID_SDK_ROOT=/usr/lib/android-sdk
ENV ANDROID_NDK_ROOT=/opt/android-ndk

# Create app directory
WORKDIR /app

# Copy app files
COPY main.py .
COPY buildozer.spec .

# Build APK
CMD ["buildozer", "android", "debug"]
