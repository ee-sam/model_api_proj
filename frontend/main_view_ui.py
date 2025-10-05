# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 607)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_Input = QGridLayout()
        self.gridLayout_Input.setObjectName(u"gridLayout_Input")
        self.gridLayout_Input.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.label_Input = QLabel(self.centralwidget)
        self.label_Input.setObjectName(u"label_Input")

        self.gridLayout_Input.addWidget(self.label_Input, 0, 0, 1, 1)

        self.textEdit_Input = QTextEdit(self.centralwidget)
        self.textEdit_Input.setObjectName(u"textEdit_Input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_Input.sizePolicy().hasHeightForWidth())
        self.textEdit_Input.setSizePolicy(sizePolicy)

        self.gridLayout_Input.addWidget(self.textEdit_Input, 1, 0, 1, 1)

        self.pushButton_Summarize = QPushButton(self.centralwidget)
        self.pushButton_Summarize.setObjectName(u"pushButton_Summarize")

        self.gridLayout_Input.addWidget(self.pushButton_Summarize, 0, 1, 2, 1, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addLayout(self.gridLayout_Input)

        self.label_Progress = QLabel(self.centralwidget)
        self.label_Progress.setObjectName(u"label_Progress")

        self.verticalLayout.addWidget(self.label_Progress)

        self.gridLayout_Output = QGridLayout()
        self.gridLayout_Output.setObjectName(u"gridLayout_Output")
        self.label_Output = QLabel(self.centralwidget)
        self.label_Output.setObjectName(u"label_Output")

        self.gridLayout_Output.addWidget(self.label_Output, 0, 0, 1, 1)

        self.textEdit_Output = QTextEdit(self.centralwidget)
        self.textEdit_Output.setObjectName(u"textEdit_Output")
        sizePolicy.setHeightForWidth(self.textEdit_Output.sizePolicy().hasHeightForWidth())
        self.textEdit_Output.setSizePolicy(sizePolicy)

        self.gridLayout_Output.addWidget(self.textEdit_Output, 1, 0, 1, 1)

        self.pushButton_Save = QPushButton(self.centralwidget)
        self.pushButton_Save.setObjectName(u"pushButton_Save")

        self.gridLayout_Output.addWidget(self.pushButton_Save, 0, 1, 2, 1, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addLayout(self.gridLayout_Output)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main View", None))
        self.label_Input.setText(QCoreApplication.translate("MainWindow", u"Input Paragraph:", None))
        self.pushButton_Summarize.setText(QCoreApplication.translate("MainWindow", u"Summarize", None))
        self.label_Progress.setText("")
        self.label_Output.setText(QCoreApplication.translate("MainWindow", u"Output Paragraph:", None))
        self.pushButton_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

