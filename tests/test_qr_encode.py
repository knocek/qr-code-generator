from src.qr_encode import generate_qr


def test_generate_qr_returns_image():
    img = generate_qr(
        data="test",
        box_size=10,
        error_correction="M (15%)",
        fg_color="#000000",
        bg_color="#ffffff",
    )
    assert img is not None
