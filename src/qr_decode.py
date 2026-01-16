# src/qr_decode.py
import cv2


def decode_qr_from_image(path: str) -> list[str]:
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Cannot load image")

    # preprocessing for light colours
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    threshold_value, binary_image = cv2.threshold(
        blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(binary_image)

    if not data:
        return []

    return [data]
