FROM node:8.5-alpine
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Update
RUN apk add --update python py-pip

# Install app dependencies
COPY ./requirements.txt src/
RUN pip install -r /src/requirements.txt

# Set env vars
ENV FLASK_APP ./src/server/server.py
ENV FLASK_DEBUG 1
ENV SETTINGS ./src/settings.py

EXPOSE 5000

# Copy source
COPY . /src

CMD ["flask", "run"]

