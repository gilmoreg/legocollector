FROM node:8.5.0-alpine
LABEL maintainer="Grayson Gilmore (gilmoreg@live.com)"

# Prevent npm install from running unless package.json changes
COPY ./package.json src/
RUN cd src && npm install --quiet

COPY . /src
WORKDIR src/

CMD ["npm", "run", "build"]