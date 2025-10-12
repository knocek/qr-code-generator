# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_and_decodevqggiy.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(30, 30, 30)")
        MainWindow.setDocumentMode(False)
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 800))
        self.centralwidget.setMaximumSize(QSize(1200, 800))
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1100, 700))
        self.tabWidget.setMaximumSize(QSize(1100, 700))
        self.generate = QWidget()
        self.generate.setObjectName(u"generate")
        self.generate.setMinimumSize(QSize(1100, 700))
        self.generate.setMaximumSize(QSize(1100, 700))
        self.gridLayoutWidget = QWidget(self.generate)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 1092, 651))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.groupInput = QGroupBox(self.gridLayoutWidget)
        self.groupInput.setObjectName(u"groupInput")
        self.groupInput.setMinimumSize(QSize(1070, 20))
        self.groupInput.setMaximumSize(QSize(1070, 100))
        self.groupInput.setAcceptDrops(True)
        self.formLayout_5 = QFormLayout(self.groupInput)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.editData = QPlainTextEdit(self.groupInput)
        self.editData.setObjectName(u"editData")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editData.sizePolicy().hasHeightForWidth())
        self.editData.setSizePolicy(sizePolicy)
        self.editData.setMinimumSize(QSize(1040, 50))
        self.editData.setMaximumSize(QSize(1040, 100))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.editData)


        self.formLayout_5.setLayout(0, QFormLayout.ItemRole.LabelRole, self.formLayout)


        self.verticalLayout_5.addWidget(self.groupInput)

        self.groupOptions = QGroupBox(self.gridLayoutWidget)
        self.groupOptions.setObjectName(u"groupOptions")
        self.groupOptions.setMaximumSize(QSize(1070, 16777215))
        self.groupOptions.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupOptions)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.errorCorrectionWidget = QWidget(self.groupOptions)
        self.errorCorrectionWidget.setObjectName(u"errorCorrectionWidget")
        self.horizontalLayoutWidget_3 = QWidget(self.errorCorrectionWidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(-10, 0, 721, 61))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.erroCortext = QLabel(self.horizontalLayoutWidget_3)
        self.erroCortext.setObjectName(u"erroCortext")
        self.erroCortext.setMidLineWidth(2)
        self.erroCortext.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.erroCortext)

        self.errorCorrectionComboBox = QComboBox(self.horizontalLayoutWidget_3)
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.addItem("")
        self.errorCorrectionComboBox.setObjectName(u"errorCorrectionComboBox")

        self.horizontalLayout_7.addWidget(self.errorCorrectionComboBox)

        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 6)

        self.gridLayout_2.addWidget(self.errorCorrectionWidget, 2, 1, 1, 1)

        self.colorWidget = QWidget(self.groupOptions)
        self.colorWidget.setObjectName(u"colorWidget")
        self.horizontalLayoutWidget_2 = QWidget(self.colorWidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 701, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnPickFg = QToolButton(self.horizontalLayoutWidget_2)
        self.btnPickFg.setObjectName(u"btnPickFg")

        self.horizontalLayout_6.addWidget(self.btnPickFg)

        self.SWATCHfG = QLabel(self.horizontalLayoutWidget_2)
        self.SWATCHfG.setObjectName(u"SWATCHfG")
        self.SWATCHfG.setMinimumSize(QSize(28, 20))
        self.SWATCHfG.setFrameShape(QFrame.Shape.Box)
        self.SWATCHfG.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.SWATCHfG)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btnPickBg = QToolButton(self.horizontalLayoutWidget_2)
        self.btnPickBg.setObjectName(u"btnPickBg")

        self.horizontalLayout_6.addWidget(self.btnPickBg)

        self.swatchHFG = QLabel(self.horizontalLayoutWidget_2)
        self.swatchHFG.setObjectName(u"swatchHFG")
        self.swatchHFG.setMinimumSize(QSize(28, 20))
        self.swatchHFG.setFrameShape(QFrame.Shape.Box)
        self.swatchHFG.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.swatchHFG)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 3)
        self.horizontalLayout_6.setStretch(4, 2)

        self.gridLayout_2.addWidget(self.colorWidget, 1, 1, 1, 1)

        self.errorCorrectionLabel = QLabel(self.groupOptions)
        self.errorCorrectionLabel.setObjectName(u"errorCorrectionLabel")

        self.gridLayout_2.addWidget(self.errorCorrectionLabel, 2, 0, 1, 1)

        self.colorLabel = QLabel(self.groupOptions)
        self.colorLabel.setObjectName(u"colorLabel")

        self.gridLayout_2.addWidget(self.colorLabel, 1, 0, 1, 1)

        self.boxSizeWidget = QWidget(self.groupOptions)
        self.boxSizeWidget.setObjectName(u"boxSizeWidget")
        self.gridLayout_3 = QGridLayout(self.boxSizeWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelBoxSize = QLabel(self.boxSizeWidget)
        self.labelBoxSize.setObjectName(u"labelBoxSize")

        self.gridLayout_3.addWidget(self.labelBoxSize, 0, 0, 1, 1)

        self.sliderBoxSize = QSlider(self.boxSizeWidget)
        self.sliderBoxSize.setObjectName(u"sliderBoxSize")
        self.sliderBoxSize.setMinimum(4)
        self.sliderBoxSize.setMaximum(20)
        self.sliderBoxSize.setValue(10)
        self.sliderBoxSize.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.sliderBoxSize, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.boxSizeWidget, 0, 1, 1, 1)

        self.boxSizeLabel = QLabel(self.groupOptions)
        self.boxSizeLabel.setObjectName(u"boxSizeLabel")

        self.gridLayout_2.addWidget(self.boxSizeLabel, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 7)

        self.verticalLayout_8.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.groupOptions)

        self.groupPreview = QGroupBox(self.gridLayoutWidget)
        self.groupPreview.setObjectName(u"groupPreview")
        self.groupPreview.setMaximumSize(QSize(1070, 16777215))
        self.groupPreview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayoutWidget_3 = QWidget(self.groupPreview)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 1052, 201))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelQrPreview = QLabel(self.verticalLayoutWidget_3)
        self.labelQrPreview.setObjectName(u"labelQrPreview")
        self.labelQrPreview.setMinimumSize(QSize(1050, 100))
        self.labelQrPreview.setMaximumSize(QSize(1040, 190))
        self.labelQrPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelQrPreview)


        self.verticalLayout_5.addWidget(self.groupPreview)

        self.btnGenerateSave = QPushButton(self.gridLayoutWidget)
        self.btnGenerateSave.setObjectName(u"btnGenerateSave")
        self.btnGenerateSave.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnGenerateSave.sizePolicy().hasHeightForWidth())
        self.btnGenerateSave.setSizePolicy(sizePolicy1)
        self.btnGenerateSave.setMinimumSize(QSize(1070, 30))
        self.btnGenerateSave.setMaximumSize(QSize(1070, 30))
        self.btnGenerateSave.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_5.addWidget(self.btnGenerateSave)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.tabWidget.addTab(self.generate, icon, "")
        self.decode = QWidget()
        self.decode.setObjectName(u"decode")
        self.decode.setMaximumSize(QSize(1100, 700))
        self.frame = QFrame(self.decode)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 20, 1200, 901))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 40, 931, 561))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.labelPreview = QLabel(self.verticalLayoutWidget)
        self.labelPreview.setObjectName(u"labelPreview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelPreview.sizePolicy().hasHeightForWidth())
        self.labelPreview.setSizePolicy(sizePolicy2)
        self.labelPreview.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelPreview.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelPreview.setMidLineWidth(2)
        self.labelPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.labelPreview)

        self.labelDrop = QLabel(self.verticalLayoutWidget)
        self.labelDrop.setObjectName(u"labelDrop")
        sizePolicy2.setHeightForWidth(self.labelDrop.sizePolicy().hasHeightForWidth())
        self.labelDrop.setSizePolicy(sizePolicy2)
        self.labelDrop.setAcceptDrops(True)
        self.labelDrop.setStyleSheet(u"backgroud-color: rgb(182, 182, 182)")
        self.labelDrop.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDrop.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelDrop.setMidLineWidth(2)
        self.labelDrop.setTextFormat(Qt.TextFormat.AutoText)
        self.labelDrop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.labelDrop)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.labelResults = QLabel(self.verticalLayoutWidget)
        self.labelResults.setObjectName(u"labelResults")
        self.labelResults.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelResults)

        self.showResultsLabel = QLabel(self.verticalLayoutWidget)
        self.showResultsLabel.setObjectName(u"showResultsLabel")
        sizePolicy2.setHeightForWidth(self.showResultsLabel.sizePolicy().hasHeightForWidth())
        self.showResultsLabel.setSizePolicy(sizePolicy2)
        self.showResultsLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.showResultsLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.showResultsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.showResultsLabel)

        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherFog))
        self.tabWidget.addTab(self.decode, icon1, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sliderBoxSize.valueChanged.connect(self.labelBoxSize.setNum)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QR Code Generator & Decoder", None))
        self.actionGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.groupInput.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.editData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text / URL / any data...", None))
        self.groupOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.erroCortext.setText(QCoreApplication.translate("MainWindow", u"set error correction", None))
        self.errorCorrectionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"L (7%)", None))
        self.errorCorrectionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"M (15%)", None))
        self.errorCorrectionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Q (25%)", None))
        self.errorCorrectionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"H (30%)", None))

        self.btnPickFg.setText(QCoreApplication.translate("MainWindow", u"FG", None))
        self.SWATCHfG.setText(QCoreApplication.translate("MainWindow", u"watch foreground", None))
        self.btnPickBg.setText(QCoreApplication.translate("MainWindow", u"BG", None))
        self.swatchHFG.setText(QCoreApplication.translate("MainWindow", u"watch background", None))
        self.errorCorrectionLabel.setText(QCoreApplication.translate("MainWindow", u"errorCorrection", None))
        self.colorLabel.setText(QCoreApplication.translate("MainWindow", u"color", None))
        self.labelBoxSize.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.boxSizeLabel.setText(QCoreApplication.translate("MainWindow", u"boxSize", None))
        self.groupPreview.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.labelQrPreview.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.btnGenerateSave.setText(QCoreApplication.translate("MainWindow", u"Generate & Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generate), QCoreApplication.translate("MainWindow", u"Generate", None))
        self.labelPreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.labelDrop.setText(QCoreApplication.translate("MainWindow", u"Drop file", None))
        self.labelResults.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.showResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Your results will show here.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decode), QCoreApplication.translate("MainWindow", u"Decode", None))
    # retranslateUi

