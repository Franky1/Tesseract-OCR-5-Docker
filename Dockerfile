# Stage 1: Build Tesseract
FROM debian:13 AS builder

ARG TESSERACT_VERSION="main"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    automake \
    ca-certificates \
    g++ \
    git \
    libtool \
    libleptonica-dev \
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    make \
    pkg-config \
    asciidoc \
    docbook-xsl \
    xsltproc

# Clone Tesseract repository
WORKDIR /src
RUN git clone --depth 1 --branch ${TESSERACT_VERSION} https://github.com/tesseract-ocr/tesseract.git tesseract-ocr

# Build and install Tesseract
WORKDIR /src/tesseract-ocr
RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# Stage 2: Final image
FROM debian:13

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    liblept5 \
    libicu72 \
    libpango-1.0-0 \
    libcairo2 \
    ca-certificates \
    libgomp1 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy Tesseract from builder stage
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY --from=builder /usr/local/share/ /usr/local/share/

# Update library cache
RUN ldconfig

# Download language data
WORKDIR /usr/local/share/tessdata/
COPY languages.txt .
COPY get-languages.sh .
RUN chmod +x ./get-languages.sh && ./get-languages.sh

# Set user input/output folder
WORKDIR /tmp/

CMD ["tesseract", "--version"]

# Some examples how to use this image
# docker pull debian:12
# docker build --progress=plain --tag tesseract:latest --build-arg TESSERACT_VERSION=main .
# docker build --progress=plain --tag tesseract:5.0.0 --build-arg TESSERACT_VERSION=5.0.0 .
# docker run -it --rm tesseract:latest
# docker run -it --rm tesseract:5.0.0
# docker run -it --name tesseract --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract /bin/bash
# docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract english.png output --oem 1 -l eng
