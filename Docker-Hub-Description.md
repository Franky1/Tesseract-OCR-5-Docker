# Tesseract OCR

Docker Image with latest Tesseract OCR Version 5.x.x built from sources.

## Usage

### Pull Docker Image

Pull the docker image from Docker Hub:

```bash
docker pull franky1/tesseract
```

### Run Docker Container

Mount your image data to the `/tmp` directory and run Tesseract OCR container with the required command line options, for example, run Tesseract OCR container with test image:

```bash
docker run -it -v ${PWD}/testdata:/tmp --rm franky1/tesseract tesseract testocr.png output --oem 1 -l eng
```

For the Tesseract command line options, please refer to the [Tesseract Manual](https://tesseract-ocr.github.io/tessdoc/)

## Image conditions

- Only supported target for this docker image currently is `linux/amd64`.
- Working directory is `/tmp` inside the container. See example above.
- This image was built _without_ the Tesseract training tools.
- This image currently includes only the following languages:
  - English: `tessdata_best > eng.traineddata`
  - German: `tessdata_best > deu.traineddata`
  - If you need other languages, you have to build your own image.

## Further documentation

- GitHub Repository for this Docker Image: <https://github.com/Franky1/Tesseract-OCR-5-Docker>
- Original Tesseract Github Repository: <https://github.com/tesseract-ocr/tesseract>
- Original Tesseract Documentation: <https://tesseract-ocr.github.io/>
- Original Tesseract Manual: <https://tesseract-ocr.github.io/tessdoc/>
- More `tessdata_best` languages: <https://github.com/tesseract-ocr/tessdata_best>

## Issues

If you have any bugs or requests regarding this Docker image, please post an issue in the Github Repository:
<https://github.com/Franky1/Tesseract-OCR-5-Docker>
