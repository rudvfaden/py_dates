# Dev container Dockerfile for py_dates
FROM mcr.microsoft.com/devcontainers/python:2-3.14

# Avoid interactive prompts (tzdata) during build
ENV DEBIAN_FRONTEND=noninteractive

# Install commonly needed build tools and system deps
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    tzdata \
    git \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Ensure pip tooling is up to date
RUN python -m pip install --upgrade pip setuptools wheel

# Set working directory (the workspace will be mounted here)
WORKDIR /workspace
