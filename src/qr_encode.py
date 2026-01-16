# src/qr_encode.py
import qrcode
from PIL import Image
from io import BytesIO

EC_MAP = {
    "L (7%)": qrcode.constants.ERROR_CORRECT_L,
    "M (15%)": qrcode.constants.ERROR_CORRECT_M,
    "Q (25%)": qrcode.constants.ERROR_CORRECT_Q,
    "H (30%)": qrcode.constants.ERROR_CORRECT_H,
}


def generate_qr(
    data: str, box_size: int, error_correction: str, fg_color: str, bg_color: str
) -> Image.Image:
    if not data.strip():
        raise ValueError("Input data is empty")

    qr = qrcode.QRCode(
        version=None,
        error_correction=EC_MAP[error_correction],
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert("RGB")

    return img


def pil_to_qpixmap(pil_img):
    buffer = BytesIO()
    pil_img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
