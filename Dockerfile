FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -o Acquire::ForceIPv4=true && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    libglib2.0-0 \
    libgthread-2.0-0 \
    libsdl2-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libgl1 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /Timberly

COPY assets assets/
COPY audio audio/
COPY fonts fonts/
COPY main.py .
COPY main.spec .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV SDL_AUDIODRIVER=dummy
ENV XDG_RUNTIME_DIR=/tmp/runtime
RUN mkdir -p /tmp/runtime

CMD ["python3", "main.py"]
