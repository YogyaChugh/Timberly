FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    pkg-config \
    libfreetype6-dev \
    libffi-dev \
    libgl1 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY assets /Timberly/assets/
COPY audio /Timberly/audio/
COPY fonts /Timberly/fonts/
COPY main.py /Timberly/
COPY main.spec /Timberly/
COPY requirements.txt /Timberly/

WORKDIR /Timberly

ENV XDG_RUNTIME_DIR=/tmp/runtime
ENV SDL_AUDIODRIVER=dummy
RUN mkdir -p /tmp/runtime

RUN pip3 install -r requirements.txt

CMD ["python3","main.py"]