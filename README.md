# Tesseract-OCR-5-Docker

Docker Image with latest Tesseract OCR Version 5 built from sources

## Usage

Build the docker image locally from scratch:

```bash
docker build -t tesseract .
```

Run tesseract ocr container with test image:

```bash
docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract testocr.png output --oem 1 -l eng
```

## ToDo

- [ ] Add more documentation
- [ ] Make Docker Hub project
- [ ] Add GitHub Actions for CI/CD
  - [ ] Add linter
    - <https://github.com/marketplace/actions/super-linter>
  - [ ] Build Docker image from Dockerfile
  - [ ] Test Docker image with test ocr image
  - [ ] Push Docker image to Docker Hub
    - <https://github.com/marketplace/actions/docker-push>
    - <https://github.com/marketplace/actions/docker-build-push-action>
  - [ ] Add Docker Hub description
    - <https://github.com/marketplace/actions/docker-hub-description>

## Project status

> 02.12.2021: Work in progress - not yet finished
