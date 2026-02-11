#!/bin/bash
# Build APK script for WSL/Linux

echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y \
    openjdk-11-jdk \
    git \
    wget \
    unzip \
    build-essential \
    libffi-dev \
    libssl-dev

echo "Installing Python dependencies..."
python3 -m pip install --upgrade pip setuptools wheel cython
python3 -m pip install buildozer kivy kivymd

echo "Building APK..."
buildozer android debug

echo "APK should be in the bin/ directory"