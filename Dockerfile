# Debian 11 aka Bullseye
FROM debian:11

ARG TESSERACT_VERSION="main"
ARG TESSERACT_URL="https://api.github.com/repos/tesseract-ocr/tesseract/tarball/$TESSERACT_VERSION"

# install basic tools
RUN apt-get update && apt-get install --no-install-recommends --yes \
    apt-transport-https \
    asciidoc \
    automake \
    bash \
    ca-certificates \
    curl \
    docbook-xsl \
    g++ \
    git \
    libleptonica-dev \
    libtool \
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    make \
    pkg-config \
    wget \
    xsltproc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

RUN wget -qO tesseract.tar.gz $TESSERACT_URL && \
    tar -xzf tesseract.tar.gz && \
    rm tesseract.tar.gz && \
    mv tesseract-* tesseract

WORKDIR /src/tesseract

RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# go to default traineddata directory
WORKDIR /usr/local/share/tessdata/

# copy language script and list to image
COPY get-languages.sh .
COPY languages.txt .

# make script executable
RUN chmod +x ./get-languages.sh
# download traineddata languages
RUN ./get-languages.sh

# go to user input/output folder
WORKDIR /tmp/

# CMD ["tesseract", "--version"]
CMD ["tesseract", "--list-langs"]

# docker pull debian:11
# docker build --tag tesseract:latest --build-arg TESSERACT_VERSION=main .
# docker build --tag tesseract:5.0.0 --build-arg TESSERACT_VERSION=5.0.0 .
# docker run -it --rm tesseract:latest
# docker run -it --rm tesseract:5.0.0
# docker run -it --name tesseract --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract english.png output --oem 1 -l eng
