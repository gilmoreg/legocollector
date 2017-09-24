FROM python:3.6.2-alpine3.6
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Install dev dependencies
RUN apk update && apk add build-base postgresql-dev

# Install app dependencies
COPY ./requirements.txt src/
RUN pip install -r /src/requirements.txt

# Set env vars for development
ENV FLASK_APP /src/server.py
ENV FLASK_DEBUG 1
ENV SETTINGS config.py
ENV DATABASE_URL postgresql://db/legocollector

EXPOSE 5000

# Copy source
COPY . /src

CMD ["flask", "run", "--host=0.0.0.0"]