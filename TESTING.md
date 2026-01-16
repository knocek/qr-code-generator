# Short testing description

## 🧪 Quick Manual Tests

- Launch application without errors.
- Generate QR code with default settings.
- Change:
  - foreground color,
  - background color,
  - error correction level,
  - box size.
- Verify live preview updates correctly.
- Generate QR with long input (expect validation warning).
- Decode QR code from image file.
- Drag & drop QR image into decoder.
- Copy decoded result to clipboard.

## 🧪 Pytest

The project includes lightweight automated tests focused on core functionality:

- QR code generation test verifies that a valid image is created for given input data.
- QR decoding test validates decoding of a real test image stored in `assets/testing`.

Tests are implemented using **pytest** and can be executed with:

```bash
python -m pytest
```

![Pytest results - all passed](/assets/pytest-results.png)

Before running tests, see your pytest version or install if pytest doesn't exists.

```bash
# see if pytest installed
pytest --version

# if no pytest exists
pip install pytest
```