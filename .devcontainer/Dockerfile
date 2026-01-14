# Dev container Dockerfile for py_dates
FROM mcr.microsoft.com/devcontainers/python:2-3.14

# Avoid interactive prompts (tzdata) during build
ENV DEBIAN_FRONTEND=noninteractive

# Install commonly needed build tools, system deps and Java (needed for PySpark)
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    tzdata \
    git \
    curl \
    default-jdk \
  && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME to the Debian default-java symlink so tools can find Java
ENV JAVA_HOME=/usr/lib/jvm/default-java

# Ensure pip tooling is up to date
RUN python -m pip install --upgrade pip setuptools wheel

# Set working directory (the workspace will be mounted here)
WORKDIR /workspace
