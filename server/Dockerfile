FROM python:3.6.2-alpine3.6
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Install dev dependencies
RUN apk update && apk add build-base postgresql-dev libxml2-dev libxslt-dev py-lxml

# Install app dependencies
COPY ./requirements.txt src/
RUN pip install -r /src/requirements.txt

# Set env vars for development
ENV FLASK_APP /src/api
ENV SETTINGS /src/api/config.py

EXPOSE 5000

# Copy source
COPY . /src

WORKDIR /src

CMD ["python", "run.py"]