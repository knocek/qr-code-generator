# src/main_window.py
import io
from PySide6.QtWidgets import QMainWindow, QFileDialog, QColorDialog, QApplication
from PySide6.QtGui import QPixmap, QColor, QImage
from PySide6.QtCore import Qt, QTimer

from src.ui.ui_generate_and_decode import Ui_MainWindow
from src.qr_encode import generate_qr
from src.qr_decode import decode_qr_from_image

LIMITS = {
    "L (7%)": 2800,
    "M (15%)": 2200,
    "Q (25%)": 1600,
    "H (30%)": 1200,
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fg_color = QColor("#000000")
        self.bg_color = QColor("#ffffff")

        self._connect_signals()
        self.ui.labelDrop.mousePressEvent = self.open_file_dialog
        self.ui.labelDrop.dragEnterEvent = self.drag_enter_event
        self.ui.labelDrop.dropEvent = self.drop_event
        self.update_color_swatches()
        self.ui.insertData.textChanged.connect(self.render_preview)
        self.ui.sliderBoxSize.valueChanged.connect(self.render_preview)
        self.ui.errorCorrectionComboBox.currentIndexChanged.connect(self.render_preview)
        self.ui.BtnCopyResults.clicked.connect(self.copy_results_to_clipboard)
        self.ui.BtnCopyResults.setEnabled(False)
        self.statusBar().showMessage("Ready", 2000)
        self.ui.labelContrastWarning.setVisible(False)

    def _connect_signals(self):
        self.ui.btnPickFg.clicked.connect(self.pick_fg_color)
        self.ui.btnPickBg.clicked.connect(self.pick_bg_color)
        self.ui.btnGenerateSave.clicked.connect(self.save_qr)

    def pick_fg_color(self):
        color = QColorDialog.getColor(self.fg_color, self)
        if color.isValid():
            self.fg_color = color
            self.update_color_swatches()
            self.render_preview()

    def pick_bg_color(self):
        color = QColorDialog.getColor(self.bg_color, self)
        if color.isValid():
            self.bg_color = color
            self.update_color_swatches()
            self.render_preview()

    def update_color_swatches(self):
        self.ui.swatchFg.setStyleSheet(f"background-color: {self.fg_color.name()}")
        self.ui.swatchBg.setStyleSheet(f"background-color: {self.bg_color.name()}")

    def ensure_qr_contrast(self, min_diff: int = 100):
        # auto adjust foreground if contrast is too low - iso says %40 contrast ratio

        fg_light = self.fg_color.lightness()
        bg_light = self.bg_color.lightness()

        if abs(fg_light - bg_light) < min_diff:
            # background is light -> force dark QR
            if bg_light > 128:
                self.fg_color = QColor("#000000")
            # background is dark -> force light QR
            else:
                self.fg_color = QColor("#ffffff")

            self.update_color_swatches()
            return True
        return False

    def show_preview_message(self, message: str):
        self.ui.labelQrPreview.setPixmap(QPixmap())
        self.ui.labelQrPreview.setAlignment(Qt.AlignCenter)
        self.ui.labelQrPreview.setText(message)

    def render_preview(self):
        data = self.ui.insertData.toPlainText().strip()

        if not data:
            self.show_preview_message("Enter data to preview QR code.")
            return

        ec_label = self.ui.errorCorrectionComboBox.currentText()
        limit = LIMITS.get(ec_label, 2200)

        # check limits before generating
        data_size = len(data.encode("utf-8"))
        if data_size > limit:
            self.show_preview_message(
                f"Data too long for selected error correction level "
                f"({data_size} bytes > {limit} bytes)."
            )
            return

        try:
            color_corrected = self.ensure_qr_contrast()

            if color_corrected:
                self.ui.labelContrastWarning.setVisible(True)
                self.statusBar().showMessage(
                    "Low contrast detected. QR color was adjusted for scannability. "
                    "Consider using darker QR on light background.",
                    4000,
                )
            else:
                self.ui.labelContrastWarning.setVisible(False)

            img = generate_qr(
                data=data,
                box_size=self.ui.sliderBoxSize.value(),
                error_correction=ec_label,
                fg_color=self.fg_color.name(),
                bg_color=self.bg_color.name(),
            )

            # preview
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            qimage = QImage.fromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)

            self.ui.labelQrPreview.setPixmap(
                pixmap.scaled(
                    self.ui.labelQrPreview.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
            )

        except Exception as e:
            self.show_preview_message(str(e))

    def save_qr(self):
        data = self.ui.insertData.toPlainText().strip()
        if not data:
            return

        color_corrected = self.ensure_qr_contrast()
        if color_corrected:
            self.statusBar().showMessage(
                "Low contrast detected. QR color was adjusted before saving.", 3000
            )

        img = generate_qr(
            data=data,
            box_size=self.ui.sliderBoxSize.value(),
            error_correction=self.ui.errorCorrectionComboBox.currentText(),
            fg_color=self.fg_color.name(),
            bg_color=self.bg_color.name(),
        )

        save_path, _ = QFileDialog.getSaveFileName(
            self, "Save QR", "", "PNG Files (*.png)"
        )
        if save_path:
            img.save(save_path)

    def open_file_dialog(self, event):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open QR image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if path:
            self.process_decode(path)

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def drop_event(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        path = urls[0].toLocalFile()
        self.process_decode(path)

    def process_decode(self, path: str):
        pixmap = QPixmap(path)
        self.ui.labelPreview.setPixmap(
            pixmap.scaled(
                self.ui.labelPreview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )

        # decode
        try:
            results = decode_qr_from_image(path)

            if not results:
                self.ui.showResultsLabel.setPlainText("No QR code found.")
                self.ui.BtnCopyResults.setEnabled(False)
                return

            self.ui.showResultsLabel.setPlainText("\n\n".join(results))
            self.ui.BtnCopyResults.setEnabled(True)

        except Exception as e:
            self.ui.showResultsLabel.setPlainText(str(e))

    def copy_results_to_clipboard(self):
        results = self.ui.showResultsLabel.toPlainText().strip()
        if not results:
            return

        QApplication.clipboard().setText(results)
        self.ui.BtnCopyResults.setText("Copied!")
        QTimer.singleShot(2000, lambda: self.ui.BtnCopyResults.setText("Copy Results"))
