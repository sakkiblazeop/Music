FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN sudo apt update -y && sudo apt upgrade -y \
    && sudo apt install -y --no-install-recommends ffmpeg \
    && sudo apt clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
