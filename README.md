# Tesseract-OCR-5-Docker

Docker Image with latest Tesseract OCR Version 5.x.x built from sources.

Docker Hub: <https://hub.docker.com/repository/docker/franky1/tesseract>

## Usage

### Pull Docker Image

Pull the docker image from Docker Hub:

```bash
docker pull franky1/tesseract
```

### Run Docker Container

Mount your image data to the `/tmp` directory and run Tesseract OCR container with the required command line options, for example, run Tesseract OCR container with test image:

```bash
docker run -it -v ${PWD}/testdata:/tmp --rm franky1/tesseract tesseract english.png output --oem 1 -l eng
```

For the Tesseract command line options, please refer to the [Tesseract Manual](https://tesseract-ocr.github.io/tessdoc/)

### Mount more languages

Test if the mounted languages from your local subfolder `/tessdata` are available in the Docker container.
Be aware that the local languages overwrite the installed languages in the Docker image. Example here with french language:

```bash
docker run -it -v ${PWD}/testdata:/tmp \
  -v ${PWD}/tessdata:/usr/local/share/tessdata/ \
  --rm franky1/tesseract
```

Test the mounted languages in the Docker container with a sample image. Example here with french language:

```bash
docker run -it -v ${PWD}/testdata:/tmp \
  -v ${PWD}/tessdata:/usr/local/share/tessdata/ \
  --rm franky1/tesseract \
  tesseract french.jpg output --oem 1 -l fra
```

## Build Docker Image yourself

Build the docker image locally from scratch:

```bash
docker build --tag tesseract .
```

Run Tesseract OCR container with test image:

```bash
docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm tesseract tesseract english.png output --oem 1 -l eng
```

## Image conditions

- Only supported target for this docker image currently is `linux/amd64`.
- Working directory for ocr images is `/tmp` inside the container. See example above.
- Directory for trained data is `/usr/local/share/tessdata/` inside the container. See example above.
- This image was built _without_ the Tesseract training tools.
- This image currently includes only the following languages:
  - English: `tessdata_best > eng.traineddata`
  - German: `tessdata_best > deu.traineddata`
  - If you need other languages, you have to build your own image or mount trained data to the `/usr/local/share/tessdata/` directory. See example above.

## Tesseract Trained Data for all available langauges

- Overview of supported languages <https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html>
- Trained models with support for legacy and LSTM OCR engine <https://github.com/tesseract-ocr/tessdata>
- Fast integer versions of trained LSTM models <https://github.com/tesseract-ocr/tessdata_fast>
- Best (most accurate) trained LSTM models <https://github.com/tesseract-ocr/tessdata_best>

## Further documentation

- GitHub Repository for this Docker Image: <https://github.com/Franky1/Tesseract-OCR-5-Docker>
- Original Tesseract Github Repository: <https://github.com/tesseract-ocr/tesseract>
- Original Tesseract Documentation: <https://tesseract-ocr.github.io/>
- Original Tesseract Manual: <https://tesseract-ocr.github.io/tessdoc/>
- More `tessdata_best` languages: <https://github.com/tesseract-ocr/tessdata_best>

## ToDo

- [ ] Add more documentation to `README.md`
- [ ] Add more documentation to `Docker-Hub-Description.md`
- [x] Add dependabot on Github
- [ ] Add vulnerability scanning in Github Actions:
  - [x] Snyk
  - [x] Anchore Container Scan
  - [ ] Trivy
- [ ] Add badges to `README.md`
- [ ] Build Tesseract from release version instead of the main trunk version!
- [ ] Improve GitHub Action to automatically tag the image according to Tesseract Release version
- [ ] Add more languages by default?
- [ ] Building Tesseract with TensorFlow?
- [ ] Building Tesseract with Training tools?
- [ ] Add AWS Lambda function to check original repo for new releases and trigger Github Action?
- [ ] Build image for more targets?

## Issues

If you have any bugs or requests regarding this Docker image, please post an issue in this Github Repository.

## Project status

> 05.12.2021: Work in progress, but docker image is ready for usage.
