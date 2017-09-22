FROM node:8.5-alpine
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Install Python3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

# Install app dependencies
COPY ./requirements.txt src/
RUN pip install -r /src/requirements.txt

# Set env vars
ENV FLASK_APP ./src/server/server.py
ENV FLASK_DEBUG 1
ENV SETTINGS settings.py

EXPOSE 5000

# Copy source
COPY . /src

CMD ["flask", "run", "--host=0.0.0.0"]

