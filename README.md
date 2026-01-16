# QR Code Generator & Decoder App

A Python-based desktop application for QR code generation and decoding, built with PySide6 and OpenCV. Supports live preview, customizable styling, and executable builds via PyInstaller.

## ✨ Features

- Generate QR codes with:
  - custom foreground and background colors,
  - adjustable box size,
  - selectable error correction level (L / M / Q / H).
- 👁️ Live preview while editing parameters.
- Decode QR codes from image files (PNG, JPG, JPEG, BMP).
- 🖱️ Drag & drop support for decoding.
- 📋 Copy decoded results to clipboard.
- ⚠️ Automatic validation of input size based on error correction level.
- 🎚️ Contrast check before generate QR Code with user warning for low-contrast QR codes.

## 🧩 Tech Stack

- Python 3.12+
- PySide6 (Qt for Python) – GUI
- qrcode + Pillow – QR generation
- OpenCV – QR decoding
- PyInstaller – executable packaging

### Why OpenCV instead of pyzbar?

QR decoding is implemented using OpenCV's `QRCodeDetector`.

This was chosen over `pyzbar` to avoid external native dependencies, which simplifies packaging with PyInstaller and improves cross-platform compatibility.

**Limitations:** Only single QR code detection per image is supported.

## 📦 Requirements - check `requirements.txt` file

- Python 3.10-3.12 [(download Python)](https://www.python.org/)
- PySide6, qrcode[pil,svg], Pillow, opencv-python, pyzbar

```bash
# checking python version
python3 --version
```

## ⬇️ Installation

### Clone repository

```bash
git clone https://github.com/knocek/qr-code-generator.git
cd qr-code-generator
```

### Installation using requirements.txt (recommended)

This is recommended and tested method for local development and building executable.

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
# upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

``` bash
# run app
python -m src.main
```

#### Build executable (Windows)

``` bash
# install pyinstaller
python -m pip install pyinstaller

#create build
python -m PyInstaller
--name "QR Code Generator"
--onefile
--windowed
--icon assets/icons/app-icon.ico
--collect-all PySide6
-m src/main.py
```

After successful build, executable file will be avaible in: `dist/QR Code Generator.exe`

**If `pyinstaller` is not recognized as the name of a cmdlet, function,...:**

1. Check how you wrote `pyinstaller`. It should be: `PyInstaller`
2. Check if PyInstaller is on your computer using command: 'pip list'
3. Edit your system paths: add user path with python scripts and restart PowerShell.

## 🎨 UX Decisions

- Decoded results are left-aligned and scrollable (avaible long text reading).
- Preview updates automatically on any parameter change.
- Cursor is disabled in result view to avoid confusion.

**Demo:**
![Generate QR Code GUI](/assets/gui-view-generate.png)
![Decode QR Code GUI](/assets/gui-view-decode.png)

## 🚨 Error Handling

- Invalid or empty input is handled.
- Input size is validated against QR error correction limits.
- Low contrast combinations trigger user warnings.
- Missing or unreadable images are reported to the user.

## 🛠️ Development Tools

- pre-commit hooks
- Ruff / formatting checks
- Virtual environment based setup
- Manual and pytest testing - see the [TESTING](TESTING) file for details

## 👩‍💻 Author & license

Author: Karolina Nocek
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
App icon: <a href="https://www.flaticon.com/free-icons/qr" title="QR icons">QR icons created by Vector Stall - Flaticon</a>