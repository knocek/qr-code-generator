# qr-code-generator
A simple and customizable Python application for generating QR codes from text, URLs, or other data inputs.

## 📦 Requirements
- Python 3.10-3.12 [(download Python)](https://www.python.org/)
- Recommended: PySide6, qrcode, Pillow, OpenCV

```bash
# checking python version
python3 --version
```

## Installation Methods #
### 1. Installation using requirements.txt - classic

#### Install
```bash
# create a virtual enviroment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

```bash
# install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

``` bash
# run app
python main.py
```

#### Build executable (Windows/macOS/Linux)
``` bash
pip install pyinstaller
pyinstaller --name "QR Code Generator" --onefile --windowed main.py
```

### 2. Installation using pyproject.toml
This method allows installing the project like a normal package using pip.
It also creates a global command (qr-gui) that runs the app.

#### Install
``` bash
pip install .
```

#### Run
``` bash
qr-gui
```

## Author & license

