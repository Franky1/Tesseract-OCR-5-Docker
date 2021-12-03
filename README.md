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
docker build --tag tesseract .
```

Run Tesseract OCR container with test image:

```bash
docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract testocr.png output --oem 1 -l eng
```

## ToDo

- [ ] Add more documentation to `README.md`
- [ ] Add more documentation to `Docker-Hub-Description.md`
- [ ] Add dependabot on Github?
- [ ] Add badges to `README.md`
- [ ] Build Tesseract from release version instead of the main trunk version!
- [ ] Improve GitHub Action to automatically tag the image according to Tesseract Release version
- [ ] Add more languages by default?
- [ ] Mount tessdata folder to add more languages?
- [ ] Building Tesseract with TensorFlow?
- [ ] Building Tesseract with Training tools?
- [ ] Add AWS Lambda function to check original repo for new releases?
- [ ] Build image for more targets?

## Project status

> 03.12.2021: Work in progress, but docker image is ready for usage.

## Issues

If you have any bugs or requests regarding this Docker image, please post an issue in this Github Repository.
