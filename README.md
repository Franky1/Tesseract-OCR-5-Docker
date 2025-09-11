<!-- markdownlint-disable MD026 MD029 MD041 -->
![License](https://img.shields.io/github/license/Franky1/Tesseract-OCR-5-Docker?logo=github)
![Issues](https://img.shields.io/github/issues/Franky1/Tesseract-OCR-5-Docker?logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Franky1/Tesseract-OCR-5-Docker?logo=github)

[![Docker](https://img.shields.io/badge/Go%20To-Docker%20Hub-blue?logo=docker)](https://hub.docker.com/repository/docker/franky1/tesseract)
![Docker](https://img.shields.io/docker/v/franky1/tesseract?logo=docker)
![Docker](https://img.shields.io/docker/v/franky1/tesseract?sort=semver&logo=docker)

# Tesseract-OCR-5-Docker :scroll:

Docker Image with latest Tesseract OCR Version 5.x.x built from sources.

The sources are pulled from the latest `main` branch and latest `releases` of the [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) project.

Docker Hub: <https://hub.docker.com/r/franky1/tesseract>

## Usage :hammer_and_wrench:

### Pull Docker Image :keyboard:

Pull the docker image from Docker Hub:

```bash
docker pull franky1/tesseract
```

### Run Docker Container :keyboard:

Mount your image data to the `/tmp` directory and run Tesseract OCR container with the required command line options, for example, run Tesseract OCR container with test image:

```bash
docker run -it -v ${PWD}/testdata:/tmp --rm franky1/tesseract \
  tesseract english.png output --oem 1 -l eng
```

For the Tesseract command line options, please refer to the [Tesseract Manual](https://tesseract-ocr.github.io/tessdoc/)

### Mount more languages :speaking_head:

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

Alternatively, you can build a new Docker image if you want other languages, see next section.

## Build Docker Image yourself :whale:

For details have a look into the [Dockerfile](Dockerfile).

1. Git clone this repo.
2. Add your required languages to the [languages.txt](languages.txt) file.
3. Build the docker image.
    - To build with the `main` branch of Tesseract:
      ```bash
      docker build --progress=plain --tag tesseract .
      ```
    - To build with a specific `release` version of Tesseract:
      ```bash
      docker build --progress=plain --tag tesseract --build-arg TESSERACT_VERSION=5.0.0 .
      ```
4. Run Tesseract OCR container with test image:

```bash
docker run -it --name tesseract -v ${PWD}/testdata:/tmp --rm \
  tesseract tesseract english.png output --oem 1 -l eng
```

## Image conditions :ballot_box_with_check:

- Only supported target for this docker image currently is `linux/amd64`.
- Working directory for ocr images is `/tmp` inside the container. See example above.
- Directory for trained data is `/usr/local/share/tessdata/` inside the container. See example above.
- This image was built _without_ the Tesseract training tools.
- This image currently includes only the following languages:
  - English: `tessdata_best > eng.traineddata`
  - German: `tessdata_best > deu.traineddata`
  - If you need other languages, you have to build your own image or mount trained data to the `/usr/local/share/tessdata/` directory. See example above.

## Tesseract Trained Data for all available languages :weight_lifting:

- Overview of supported languages <https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html>
- Trained models with support for legacy and LSTM OCR engine <https://github.com/tesseract-ocr/tessdata>
- Fast integer versions of trained LSTM models <https://github.com/tesseract-ocr/tessdata_fast>
- Best (most accurate) trained LSTM models <https://github.com/tesseract-ocr/tessdata_best>

## Further documentation :link:

- Docker Hub: <https://hub.docker.com/repository/docker/franky1/tesseract>
- Original Tesseract Github Repository: <https://github.com/tesseract-ocr/tesseract>
- Original Tesseract Documentation: <https://tesseract-ocr.github.io/>
- Original Tesseract Manual: <https://tesseract-ocr.github.io/tessdoc/>
- More `tessdata_best` languages: <https://github.com/tesseract-ocr/tessdata_best>

## ToDo :white_check_mark:

- [x] Update `README.md` to latest Dockerfile and Usage
- [x] Add dependabot on Github
- [x] Add vulnerability scanning in Github Actions with Snyk
- [x] Use multi-stage build in Dockerfile and clone from git
- [ ] Add GitHub Action for check container efficiency with Dive <https://github.com/MartinHeinz/dive-action>
- [ ] Add documentation for GitHub Actions Workflow
- [ ] Add more inline comments in GitHub Actions related files
- [ ] Build image for more targets
- [ ] Building Tesseract with TensorFlow?
- [ ] Building Tesseract with Training tools?

## Issues :bug:

If you have any bugs or requests regarding this Docker image, please post an issue in this Github Repository.

## Project status :heavy_check_mark:

> 11.09.2025: Docker Image is ready for usage, still some slight improvements possible, sometimes build issues
