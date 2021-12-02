# Debian 11 aka Bullseye
FROM debian:11

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
    make \
    pkg-config \
    wget \
    xsltproc

WORKDIR /src

RUN git clone --depth 1  https://github.com/tesseract-ocr/tesseract.git

WORKDIR /src/tesseract

RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# go to default traineddata directory
WORKDIR /usr/local/share/tessdata/

# add traineddata languages - here eng and deu
RUN wget https://github.com/tesseract-ocr/tessdata_best/blob/main/eng.traineddata?raw=true -O eng.traineddata && \
    wget https://github.com/tesseract-ocr/tessdata_best/blob/main/deu.traineddata?raw=true -O deu.traineddata

# go to user input/output folder
WORKDIR /tmp/

# CMD ["tesseract", "--version"]
CMD ["tesseract", "--list-langs"]

# docker build -t tesseract .
# docker run -it --name tesseract --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract testocr.png output --oem 1 -l eng
