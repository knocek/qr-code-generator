# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_and_decodevsJUus.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QTabWidget,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(
            'font: 9pt "Segoe UI";\n' "background-color: rgb(30, 30, 30)"
        )
        MainWindow.setDocumentMode(False)
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 800))
        self.centralwidget.setMaximumSize(QSize(1200, 800))
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(1100, 700))
        self.tabWidget.setMaximumSize(QSize(1100, 700))
        self.generate = QWidget()
        self.generate.setObjectName("generate")
        self.generate.setMinimumSize(QSize(1100, 700))
        self.generate.setMaximumSize(QSize(1100, 700))
        self.gridLayoutWidget = QWidget(self.generate)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 1092, 651))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.groupInput = QGroupBox(self.gridLayoutWidget)
        self.groupInput.setObjectName("groupInput")
        self.groupInput.setMinimumSize(QSize(1070, 20))
        self.groupInput.setMaximumSize(QSize(1070, 100))
        self.groupInput.setAcceptDrops(True)
        self.formLayout_5 = QFormLayout(self.groupInput)
        self.formLayout_5.setObjectName("formLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.insertData = QPlainTextEdit(self.groupInput)
        self.insertData.setObjectName("insertData")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertData.sizePolicy().hasHeightForWidth())
        self.insertData.setSizePolicy(sizePolicy)
        self.insertData.setMinimumSize(QSize(1040, 50))
        self.insertData.setMaximumSize(QSize(1040, 100))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.insertData)

        self.formLayout_5.setLayout(0, QFormLayout.ItemRole.LabelRole, self.formLayout)

        self.verticalLayout_5.addWidget(self.groupInput)

        self.groupOptions = QGroupBox(self.gridLayoutWidget)
        self.groupOptions.setObjectName("groupOptions")
        self.groupOptions.setMaximumSize(QSize(1070, 16777215))
        self.groupOptions.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.verticalLayout_8 = QVBoxLayout(self.groupOptions)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.errorCorrectionWidget = QWidget(self.groupOptions)
        self.errorCorrectionWidget.setObjectName("errorCorrectionWidget")
        self.erroCortext = QLabel(self.errorCorrectionWidget)
        self.erroCortext.setObjectName("erroCortext")
        self.erroCortext.setGeometry(QRect(-9, 1, 30, 26))
        self.erroCortext.setMidLineWidth(2)
        self.erroCortext.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.erroCortext.setMargin(5)
        self.erroCortext.setIndent(20)
        self.errorCorrectionComboBox = QComboBox(self.errorCorrectionWidget)
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.setObjectName("errorCorrectionComboBox")
        self.errorCorrectionComboBox.setGeometry(QRect(2, 18, 691, 24))

        self.gridLayout_2.addWidget(self.errorCorrectionWidget, 2, 1, 1, 1)

        self.colorWidget = QWidget(self.groupOptions)
        self.colorWidget.setObjectName("colorWidget")
        self.horizontalLayoutWidget_2 = QWidget(self.colorWidget)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 701, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnPickFg = QToolButton(self.horizontalLayoutWidget_2)
        self.btnPickFg.setObjectName("btnPickFg")
        self.btnPickFg.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_6.addWidget(self.btnPickFg)

        self.swatchFg = QLabel(self.horizontalLayoutWidget_2)
        self.swatchFg.setObjectName("swatchFg")
        self.swatchFg.setMinimumSize(QSize(28, 20))
        self.swatchFg.setMaximumSize(QSize(45, 45))
        self.swatchFg.setFrameShape(QFrame.Shape.Box)
        self.swatchFg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.swatchFg)

        self.horizontalSpacer = QSpacerItem(
            15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btnPickBg = QToolButton(self.horizontalLayoutWidget_2)
        self.btnPickBg.setObjectName("btnPickBg")
        self.btnPickBg.setMinimumSize(QSize(200, 40))
        self.btnPickBg.setMaximumSize(QSize(200, 40))
        self.btnPickBg.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.btnPickBg)

        self.swatchBg = QLabel(self.horizontalLayoutWidget_2)
        self.swatchBg.setObjectName("swatchBg")
        self.swatchBg.setMinimumSize(QSize(28, 20))
        self.swatchBg.setMaximumSize(QSize(45, 45))
        self.swatchBg.setFrameShape(QFrame.Shape.Box)
        self.swatchBg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.swatchBg)

        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 3)
        self.horizontalLayout_6.setStretch(4, 2)

        self.gridLayout_2.addWidget(self.colorWidget, 1, 1, 1, 1)

        self.errorCorrectionLabel = QLabel(self.groupOptions)
        self.errorCorrectionLabel.setObjectName("errorCorrectionLabel")
        self.errorCorrectionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.errorCorrectionLabel, 2, 0, 1, 1)

        self.colorLabel = QLabel(self.groupOptions)
        self.colorLabel.setObjectName("colorLabel")
        self.colorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.colorLabel, 1, 0, 1, 1)

        self.boxSizeWidget = QWidget(self.groupOptions)
        self.boxSizeWidget.setObjectName("boxSizeWidget")
        self.gridLayout_3 = QGridLayout(self.boxSizeWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelBoxSize = QLabel(self.boxSizeWidget)
        self.labelBoxSize.setObjectName("labelBoxSize")

        self.gridLayout_3.addWidget(self.labelBoxSize, 0, 0, 1, 1)

        self.sliderBoxSize = QSlider(self.boxSizeWidget)
        self.sliderBoxSize.setObjectName("sliderBoxSize")
        self.sliderBoxSize.setMinimum(4)
        self.sliderBoxSize.setMaximum(20)
        self.sliderBoxSize.setValue(10)
        self.sliderBoxSize.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sliderBoxSize, 0, 1, 1, 1)

        self.gridLayout_2.addWidget(self.boxSizeWidget, 0, 1, 1, 1)

        self.boxSizeLabel = QLabel(self.groupOptions)
        self.boxSizeLabel.setObjectName("boxSizeLabel")
        self.boxSizeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.boxSizeLabel, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 7)

        self.verticalLayout_8.addLayout(self.gridLayout_2)

        self.verticalLayout_5.addWidget(self.groupOptions)

        self.groupPreview = QGroupBox(self.gridLayoutWidget)
        self.groupPreview.setObjectName("groupPreview")
        self.groupPreview.setMaximumSize(QSize(1070, 16777215))
        self.groupPreview.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.verticalLayoutWidget_3 = QWidget(self.groupPreview)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 1052, 201))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelQrPreview = QLabel(self.verticalLayoutWidget_3)
        self.labelQrPreview.setObjectName("labelQrPreview")
        self.labelQrPreview.setMinimumSize(QSize(1050, 100))
        self.labelQrPreview.setMaximumSize(QSize(1040, 190))
        self.labelQrPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelQrPreview)

        self.labelContrastWarning = QLabel(self.verticalLayoutWidget_3)
        self.labelContrastWarning.setObjectName("labelContrastWarning")
        self.labelContrastWarning.setMaximumSize(QSize(1200, 20))
        self.labelContrastWarning.setStyleSheet("color: #f1c40f;\n" "font-size: 11px;")
        self.labelContrastWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelContrastWarning.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )

        self.verticalLayout_6.addWidget(self.labelContrastWarning)

        self.verticalLayout_5.addWidget(self.groupPreview)

        self.btnGenerateSave = QPushButton(self.gridLayoutWidget)
        self.btnGenerateSave.setObjectName("btnGenerateSave")
        self.btnGenerateSave.setEnabled(True)
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.btnGenerateSave.sizePolicy().hasHeightForWidth()
        )
        self.btnGenerateSave.setSizePolicy(sizePolicy1)
        self.btnGenerateSave.setMinimumSize(QSize(1070, 30))
        self.btnGenerateSave.setMaximumSize(QSize(1070, 30))
        self.btnGenerateSave.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon(QIcon.fromTheme("document-save-as"))
        self.btnGenerateSave.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btnGenerateSave)

        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        icon1 = QIcon(QIcon.fromTheme("list-add"))
        self.tabWidget.addTab(self.generate, icon1, "")
        self.decode = QWidget()
        self.decode.setObjectName("decode")
        self.decode.setMaximumSize(QSize(1100, 700))
        self.frame = QFrame(self.decode)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(-10, 20, 1200, 901))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 40, 931, 561))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.labelPreview = QLabel(self.verticalLayoutWidget)
        self.labelPreview.setObjectName("labelPreview")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.labelPreview.sizePolicy().hasHeightForWidth()
        )
        self.labelPreview.setSizePolicy(sizePolicy2)
        self.labelPreview.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelPreview.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelPreview.setMidLineWidth(2)
        self.labelPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.labelPreview)

        self.labelDrop = QLabel(self.verticalLayoutWidget)
        self.labelDrop.setObjectName("labelDrop")
        sizePolicy2.setHeightForWidth(self.labelDrop.sizePolicy().hasHeightForWidth())
        self.labelDrop.setSizePolicy(sizePolicy2)
        self.labelDrop.setAcceptDrops(True)
        self.labelDrop.setStyleSheet("background-color: rgb(182, 182, 182)")
        self.labelDrop.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDrop.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelDrop.setMidLineWidth(2)
        self.labelDrop.setTextFormat(Qt.TextFormat.AutoText)
        self.labelDrop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.labelDrop)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.labelResults = QLabel(self.verticalLayoutWidget)
        self.labelResults.setObjectName("labelResults")
        self.labelResults.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelResults)

        self.horizontalSpacer_2 = QSpacerItem(
            1000, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout_4.addItem(self.horizontalSpacer_2)

        self.showResultsLabel = QTextEdit(self.verticalLayoutWidget)
        self.showResultsLabel.setObjectName("showResultsLabel")
        self.showResultsLabel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.showResultsLabel.setFrameShape(QFrame.Shape.Box)
        self.showResultsLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.showResultsLabel.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByKeyboard
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )

        self.verticalLayout_4.addWidget(self.showResultsLabel)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout_4.addItem(self.horizontalSpacer_3)

        self.BtnCopyResults = QPushButton(self.verticalLayoutWidget)
        self.BtnCopyResults.setObjectName("BtnCopyResults")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.BtnCopyResults.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.BtnCopyResults)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPageSetup))
        self.tabWidget.addTab(self.decode, icon3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sliderBoxSize.valueChanged.connect(self.labelBoxSize.setNum)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "QR Code Generator & Decoder", None
            )
        )
        self.actionGenerate.setText(
            QCoreApplication.translate("MainWindow", "Generate", None)
        )
        self.groupInput.setTitle(
            QCoreApplication.translate("MainWindow", "Input", None)
        )
        self.insertData.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Enter text / URL / your data here...", None
            )
        )
        self.groupOptions.setTitle(
            QCoreApplication.translate("MainWindow", "Options", None)
        )
        self.erroCortext.setText("")
        self.errorCorrectionComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "L (7%)", None)
        )
        self.errorCorrectionComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", "M (15%)", None)
        )
        self.errorCorrectionComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", "Q (25%)", None)
        )
        self.errorCorrectionComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", "H (30%)", None)
        )

        self.btnPickFg.setText(
            QCoreApplication.translate("MainWindow", "Pick foreground colour", None)
        )
        self.swatchFg.setText("")
        self.btnPickBg.setText(
            QCoreApplication.translate("MainWindow", "Pick background colour", None)
        )
        self.swatchBg.setText("")
        self.errorCorrectionLabel.setText(
            QCoreApplication.translate("MainWindow", "Error correction", None)
        )
        self.colorLabel.setText(
            QCoreApplication.translate(
                "MainWindow", "Set foreground and background colour", None
            )
        )
        self.labelBoxSize.setText(QCoreApplication.translate("MainWindow", "10", None))
        self.boxSizeLabel.setText(
            QCoreApplication.translate("MainWindow", "Box size", None)
        )
        self.groupPreview.setTitle(
            QCoreApplication.translate("MainWindow", "Preview", None)
        )
        self.labelQrPreview.setText(
            QCoreApplication.translate(
                "MainWindow", "Your preview will show here.", None
            )
        )
        self.labelContrastWarning.setText(
            QCoreApplication.translate(
                "MainWindow", "Low contrast \u2013 QR color auto-adjusted", None
            )
        )
        self.btnGenerateSave.setText(
            QCoreApplication.translate("MainWindow", "Generate and Save", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.generate),
            QCoreApplication.translate("MainWindow", "Generate", None),
        )
        self.labelPreview.setText(
            QCoreApplication.translate("MainWindow", "Preview", None)
        )
        self.labelDrop.setText(
            QCoreApplication.translate(
                "MainWindow", "Drop file / Click to add file from disk", None
            )
        )
        self.labelResults.setText(
            QCoreApplication.translate("MainWindow", "Results", None)
        )
        self.showResultsLabel.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Your results will show here.", None
            )
        )
        self.BtnCopyResults.setText(
            QCoreApplication.translate("MainWindow", "Copy results", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.decode),
            QCoreApplication.translate("MainWindow", "Decode", None),
        )

    # retranslateUi
