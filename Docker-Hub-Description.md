<!-- markdownlint-disable MD026 MD029 MD041 -->
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Franky1/Tesseract-OCR-5-Docker)
![Issues](https://img.shields.io/github/issues/Franky1/Tesseract-OCR-5-Docker?logo=github)
![Docker](https://img.shields.io/docker/v/franky1/tesseract?logo=docker)
![Docker](https://img.shields.io/docker/v/franky1/tesseract?sort=semver&logo=docker)

# Tesseract OCR :scroll:

Docker Image with latest Tesseract OCR Version 5.x.x built from sources.

The sources are pulled from the latest `main` branch and latest `releases` of the [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) project.

GitHub Repository: <https://github.com/Franky1/Tesseract-OCR-5-Docker>

## Tags

`latest` : Whenever there is a change in the sources, the `main` branch is pulled and the image is rebuilt. Changes are checked on a daily basis.

`5.x.x` : Whenever there is a new release of Tesseract OCR 5.x.x., the sources from this release are pulled and the image is built and tagged accordingly. Checking for new releases is done on a daily basis.

## Usage :hammer_and_wrench:

### Pull Docker Image

Pull the docker image from Docker Hub:

```bash
docker pull franky1/tesseract
```

### Run Docker Container

```text
see GitHub Repository for better understanding of the steps below
```

Mount your image data to the `/tmp` directory and run Tesseract OCR container with the required command line options, for example, run Tesseract OCR container with test image:

```bash
docker run -it -v ${PWD}/testdata:/tmp --rm franky1/tesseract \
  tesseract english.png output --oem 1 -l eng
```

For the Tesseract command line options, please refer to the [Tesseract Manual](https://tesseract-ocr.github.io/tessdoc/)

### Mount more languages :speaking_head:

```text
see GitHub Repository for better understanding of the steps below
```

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

## Image conditions

- Only supported target for this docker image currently is `linux/amd64`.
- Working directory for ocr images is `/tmp` inside the container. See example above.
- Directory for trained data is `/usr/local/share/tessdata/` inside the container. See example above.
- This image was built _without_ the Tesseract training tools.
- This image currently includes only the following languages from `tessdata_best` repository:
  - English: `tessdata_best > eng.traineddata`
  - German: `tessdata_best > deu.traineddata`
  - If you need other languages, you have to build your own image or mount trained data to the `/usr/local/share/tessdata/` directory. See example above.

## Tesseract Trained Data for all available languages

- Overview of supported languages <https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html>
- Trained models with support for legacy and LSTM OCR engine <https://github.com/tesseract-ocr/tessdata>
- Fast integer versions of trained LSTM models <https://github.com/tesseract-ocr/tessdata_fast>
- Best (most accurate) trained LSTM models <https://github.com/tesseract-ocr/tessdata_best>

## Further documentation :link:

- GitHub Repository for this Docker Image: <https://github.com/Franky1/Tesseract-OCR-5-Docker>
- Original Tesseract Github Repository: <https://github.com/tesseract-ocr/tesseract>
- Original Tesseract Documentation: <https://tesseract-ocr.github.io/>
- Original Tesseract Manual: <https://tesseract-ocr.github.io/tessdoc/>

## Issues :bug:

If you have any bugs or requests regarding this Docker image, please post an issue in the Github Repository:
<https://github.com/Franky1/Tesseract-OCR-5-Docker>

## Project status :heavy_check_mark:

```text
22.03.2022: Docker Image is ready for usage, still some slight improvements possible (see GitHub Repo)
```
