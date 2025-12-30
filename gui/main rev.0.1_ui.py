# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main rev.0.1.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGraphicsView,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 552)
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
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radioButton_student = QRadioButton(self.frame)
        self.radioButton_student.setObjectName(u"radioButton_student")
        font = QFont()
        font.setPointSize(10)
        self.radioButton_student.setFont(font)

        self.verticalLayout_8.addWidget(self.radioButton_student)

        self.radioButton_staff = QRadioButton(self.frame)
        self.radioButton_staff.setObjectName(u"radioButton_staff")
        self.radioButton_staff.setFont(font)

        self.verticalLayout_8.addWidget(self.radioButton_staff)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setFont(font)

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)

        self.pushButton_now = QPushButton(self.groupBox)
        self.pushButton_now.setObjectName(u"pushButton_now")
        self.pushButton_now.setMinimumSize(QSize(0, 0))
        self.pushButton_now.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_now.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_now)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_search = QLineEdit(self.groupBox)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_search)

        self.pushButton_search = QPushButton(self.groupBox)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_search)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.tableView_search_result = QTableView(self.groupBox)
        self.tableView_search_result.setObjectName(u"tableView_search_result")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        self.tableView_search_result.setFont(font1)

        self.verticalLayout_5.addWidget(self.tableView_search_result)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.final_result_text = QLabel(Form)
        self.final_result_text.setObjectName(u"final_result_text")
        self.final_result_text.setFont(font2)

        self.horizontalLayout_2.addWidget(self.final_result_text)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


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
        self.label_2.setText(QCoreApplication.translate("Form", u"Date Time :", None))
        self.pushButton_now.setText(QCoreApplication.translate("Form", u"Now", None))
        self.label.setText(QCoreApplication.translate("Form", u"Search Name/Roll Number : ", None))
        self.pushButton_search.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Result : ", None))
        self.final_result_text.setText(QCoreApplication.translate("Form", u"result as text", None))
    # retranslateUi

