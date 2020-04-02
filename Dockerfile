FROM python:3.8-slim
# Get envsubst from gettext-base
RUN apt-get update &&\
    apt-get install gettext-base
RUN pip install requests twitter
WORKDIR /twitter
COPY . .
CMD envsubst < config.json.example > config.json && python tweet.py
