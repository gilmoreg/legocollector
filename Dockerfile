FROM node:8.5-alpine
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Update
RUN apk add --update python py-pip

# Install app dependencies
COPY ./requirements.txt src/
RUN pip install -r /src/requirements.txt

# Copy source
COPY . /src

CMD ["python", "/src/server/server.py"]

