# google-translate-app-with-tkinter
translation  app with tkinter gui laibrary it works only online

# Translator App

A simple GUI-based Translator application built using Python and Tkinter. This app allows users to translate text between multiple languages using Google Translate API. Additionally, it provides an option to download languages for offline translation using `argostranslate`.

## Features

- Translate text between multiple languages.
- User-friendly Tkinter GUI.
- Offline translation support (via `argostranslate`).
- Ability to download language models for offline use.
- Generates an executable `.exe` file using PyInstaller.

## Installation

### Prerequisites
Make sure you have Python 3.7+ installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Run the App
To start the translator, run:

```bash
python translater.py
```

### Build an Executable (.exe)
To create an executable version of the app using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=google_translate_icon.ico \
--add-data "translator/google_translate_icon.png;translator" \
--add-data "translator/arrow.png;translator" translater.py
```

## Offline Translation Support

To enable offline translation, install `argostranslate`:

```bash
pip install argostranslate
```

To download and install a language for offline use:

```python
from argostranslate import package, translate

def download_language(from_lang, to_lang):
    packages = package.get_available_packages()
    for p in packages:
        if p.from_code == from_lang and p.to_code == to_lang:
            package.install_from_path(p.download())

download_language("en", "fr")  # Example: English to French
```

## Folder Structure
```
translator/
│── translater.py            # Main script
│── requirements.txt         # Dependencies
│── google_translate_icon.ico  # App icon
├── google_translate_icon.png  # UI Image
├── arrow.png  # UI Image
│── README.md
```

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.


