# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListView, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 701)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.radioButton_student = QRadioButton(self.groupBox)
        self.radioButton_student.setObjectName(u"radioButton_student")

        self.verticalLayout_2.addWidget(self.radioButton_student)

        self.radioButton_staff = QRadioButton(self.groupBox)
        self.radioButton_staff.setObjectName(u"radioButton_staff")

        self.verticalLayout_2.addWidget(self.radioButton_staff)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_search = QLineEdit(self.groupBox)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.pushButton_search = QPushButton(self.groupBox)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout.addWidget(self.pushButton_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listView_search_result = QListView(self.groupBox)
        self.listView_search_result.setObjectName(u"listView_search_result")

        self.verticalLayout_5.addWidget(self.listView_search_result)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.result_text = QLabel(Form)
        self.result_text.setObjectName(u"result_text")
        font = QFont()
        font.setBold(True)
        self.result_text.setFont(font)

        self.horizontalLayout_2.addWidget(self.result_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_6.addWidget(self.graphicsView)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Find-Expected-Location-of-Person", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Search", None))
        self.radioButton_student.setText(QCoreApplication.translate("Form", u"Student", None))
        self.radioButton_staff.setText(QCoreApplication.translate("Form", u"Staff", None))
        self.label.setText(QCoreApplication.translate("Form", u"Search Name/Roll Number : ", None))
        self.pushButton_search.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Result : ", None))
        self.result_text.setText(QCoreApplication.translate("Form", u"result as text", None))
    # retranslateUi

