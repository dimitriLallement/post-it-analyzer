# Post-it Analyzer

This tool is designed in order to extract the main information from a picture of a post-it :

* **text:** an OCR will retrieve the text of the post-it
* **color:** the RGB color corresponding of the post-it color
* **type:** if you want, you can list type of post-it according to its color (ex : blue = info, yellow = To do, etc.) in the property file.

## Getting Started

### Prerequisites

* Python 3.6.5 or later
* tesseract 0.2.7 or later (command: `pip install pytesseract`)
* opencv 4.1.0.25 or later (command: `pip install opencv-python`)
* pyyaml 5.1.2 or later (command: `pip install pyyaml`)
* At least one language pack from tesseract (linux command for english pack: `sudo apt-get install tesseract-ocr-eng`)
* *(optionnal)* Others language packs from tesseract (source: <https://github.com/tesseract-ocr/tessdata>)

### Installing

```bash
$ git clone https://github.com/dimitriLallement/post-it-analyzer.git
$ cd post-it-analyzer
#installer les dépendances
$ pip install -r requirements.txt
```

## Usage

```bash
    python post_it_analyzer.py [-h|--help] [-v|--version=] [-l|--language=] <language>
```

The English language is assumed by default. If you want an other language, you have to download the corresponding language pack from this repository :
<https://github.com/tesseract-ocr/tessdata>

The script will prompt the following line :

``` python
File :
```

And then you just have to give the path of the input file(ex: `C:\Users\Example\image\test.png`)

### Edit the configuration file

TODO => Explain how the config file works

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
