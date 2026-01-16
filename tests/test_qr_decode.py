from pathlib import Path
from src.qr_decode import decode_qr_from_image


def test_decode_light_background_qr():
    project_root = Path(__file__).resolve().parents[1]
    image_path = project_root / "assets" / "testing" / "light-bg-fg-correct-iso.png"

    decoded = decode_qr_from_image(str(image_path))

    assert decoded
    assert decoded[0] == "light FG and BG, but correct with ISO standard"
