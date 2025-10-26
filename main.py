import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QDir, Slot
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide6.QtUiTools import QUiLoader 

# from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
#     QLabel, QLineEdit, QListView, QPushButton,
#     QRadioButton, QSizePolicy, QVBoxLayout, QWidget)




UI_FILE = os.path.dirname(__file__) + r"/gui/main.ui"
QSS_FILE = os.path.join(os.path.dirname(__file__), r"gui/theme.qss")


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load .ui
        loader = QUiLoader()
        ui_file = QtCore.QFile(UI_FILE)
        if not ui_file.open(QtCore.QFile.ReadOnly):
            raise RuntimeError(f"Failed to open {UI_FILE}")
        self.ui = loader.load(ui_file, parentWidget=None)
        ui_file.close()
        if self.ui is None:
            raise RuntimeError("Failed to load UI")

        # Reparent loaded UI widgets into this widget
        self.ui.setParent(self)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.ui)

        # Access widgets created in the .ui

        self.radioButton_student: QtWidgets.QRadioButton = self.ui.findChild(QtWidgets.QRadioButton, "radioButton_student")
        self.radioButton_student.setChecked(True)

        self.radioButton_staff: QtWidgets.QRadioButton = self.ui.findChild(QtWidgets.QRadioButton, "radioButton_staff")

        self.lineEdit_search: QtWidgets.QLineEdit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_search")

        self.pushButton_search: QtWidgets.QPushButton = self.ui.findChild(QtWidgets.QPushButton, "pushButton_search")
        self.pushButton_search.clicked.connect(self.on_pushButton_search_clicked)
        # self.pushButton_search.setEnabled(False)

        self.listView_search_result: QtWidgets.QListView = self.ui.findChild(QtWidgets.QListView, "listView_search_result")

        # self.lineEdit_rm_right: QtWidgets.QLineEdit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_rm_right")
        # self.lineEdit_rm_right.setValidator(QIntValidator(1, 50, self))
        # self.lineEdit_rm_right.setText("8")

        # self.dpi_combo: QtWidgets.QComboBox = self.ui.findChild(QtWidgets.QComboBox, "dpi_combo")
        # self.dpi_combo.setEditable(True)
        # self.dpi_combo.addItems(["72", "96", "100", "150", "200", "300"])
        # self.dpi_combo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        # self.dpi_combo.lineEdit().setValidator(QtGui.QIntValidator(72, 1200, self))
        
        self.apply_qss(QSS_FILE)


    def apply_qss(self, qss_path: str):
        if not os.path.exists(qss_path):
            return
        with open(qss_path, "r", encoding="utf-8") as f:
            qss = f.read()
        self.setStyleSheet(qss)


    @Slot()
    def on_pushButton_search_clicked(self):

        print('clicked')

        try:
            search_list = [x for x in self.lineEdit_search.text().split(" ") if x]
        except:
            print('error in search string')

        if not (len(search_list)):
            QMessageBox.warning(self, "Warning", "No search text.")
            return

        print(search_list)


    #     try:
    #         out_path = self.process_psd(self.label_file_to_process.text() , 
    #                                     dpi = dpi,
    #                                     rm_left_mm = rm_left,
    #                                     rm_right_mm = rm_right,
    #                                     rm_top_mm = rm_top, 
    #                                     rm_bottom_mm = rm_bottom,
    #                                     scale = scale, 
    #                                     gutter = gutter,
    #                                     g_at = g_at)
            
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Processing failed: {e}")
    #         return

    #     self.load_output_pdf(str(out_path))
    #     self.tabWidget.setCurrentIndex(1)

    # -------------------------------------------------


def main():

    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("Find-Expected-Location-of-Person")
    w.resize(700, 800)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Hello from find-expected-location-of-person!")
    main()


