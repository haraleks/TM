############################
# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add additional alpine download url in dockerfile
RUN echo -e "http://dl-4.alpinelinux.org/alpine/v3.12/main\nhttp://dl-4.alpinelinux.org/alpine/v3.12/community" > /etc/apk/repositories

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN apk --no-cache add build-base \
                       # dev dependencies
                       py3-pip \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
#RUN pipenv lock --requirements > requirements.txt
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

# copy enrtypoint
COPY ./entrypoint.sh .

# copy project
COPY . .


# migrate
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]