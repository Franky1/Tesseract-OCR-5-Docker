# Tesseract-OCR-5-Docker

Docker Image with latest Tesseract OCR Version 5.x.x built from sources.

## Usage

Pull the docker image from Docker Hub:

```bash
docker pull franky1/tesseract
```

Run Tesseract OCR container with test image:

```bash
docker run -it -v ${PWD}/testdata:/tmp --rm franky1/tesseract tesseract testocr.png output --oem 1 -l eng
```

## Build Docker Image yourself

Build the docker image locally from scratch:

```bash
docker build -t tesseract .
```

Run Tesseract OCR container with test image:

```bash
docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract testocr.png output --oem 1 -l eng
```

## ToDo

- [ ] Add more documentation to README.md
- [ ] Add documentation to Docker-Hub-Description.md
- [ ] Add dependabot?
- [x] Make Docker Hub project
- [x] Add GitHub Actions for CI/CD
  - [x] Add linter
    - <https://github.com/marketplace/actions/super-linter>
  - [x] Build Docker image from Dockerfile
  - [x] Test Docker image with test ocr image
  - [x] Add secrets to Github Account
    - <https://docs.github.com/en/actions/security-guides/encrypted-secrets>
  - [x] Push Docker image to Docker Hub
    - <https://github.com/docker/build-push-action>
    - <https://github.com/marketplace/actions/docker-push>
    - <https://github.com/marketplace/actions/docker-build-push-action>
  - [x] Update Docker Hub description
    - <https://github.com/marketplace/actions/docker-hub-description>

## Project status

> 03.12.2021: Work in progress - not yet finished
