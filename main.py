import os
import sys
import pandas as pd

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QDir, Slot
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog, QTableView
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore import Qt, QDateTime, QAbstractTableModel, QModelIndex

# from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
#     QLabel, QLineEdit, QListView, QPushButton,
#     QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

import student
import staff

UI_FILE = os.path.dirname(__file__) + r"/gui/main.ui"
QSS_FILE = os.path.join(os.path.dirname(__file__), r"gui/theme.qss")

class DataFrameModel(QAbstractTableModel):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self._df = df.copy()

    def rowCount(self, parent=None):
        return len(self._df)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role not in (Qt.DisplayRole, Qt.EditRole):
            return None
        value = self._df.iat[index.row(), index.column()]
        return str(value)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self._df.columns[section])
        else:
            return str(self._df.index[section])

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole or not index.isValid():
            return False
        row, col = index.row(), index.column()
        try:
            # try to preserve dtype
            dtype = self._df.dtypes.iloc[col]
            if pd.api.types.is_numeric_dtype(dtype):
                converted = pd.to_numeric(value)
            else:
                converted = value
            self._df.iat[row, col] = converted
        except Exception:
            self._df.iat[row, col] = value
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
        return True

    def get_dataframe(self):
        return self._df.copy()

class MainWindow(QtWidgets.QWidget):
    def __init__(self, student_reg, staff_reg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.student_reg = student_reg
        self.staff_reg = staff_reg

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

        self.dateTimeEdit: QtWidgets.QDateTimeEdit = self.ui.findChild(QtWidgets.QDateTimeEdit,"dateTimeEdit")
        now = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)

        self.pushButton_now: QtWidgets.QPushButton = self.ui.findChild(QtWidgets.QPushButton, "pushButton_now")
        self.pushButton_now.clicked.connect(self.on_pushButton_now_clicked)

        self.lineEdit_search: QtWidgets.QLineEdit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_search")

        self.pushButton_search: QtWidgets.QPushButton = self.ui.findChild(QtWidgets.QPushButton, "pushButton_search")
        self.pushButton_search.clicked.connect(self.on_pushButton_search_clicked)
        # self.pushButton_search.setEnabled(False)

        self.tableView_search_result: QtWidgets.QTableView = self.ui.findChild(QtWidgets.QTableView, "tableView_search_result")

        self.final_result_text: QtWidgets.QLabel = self.ui.findChild(QtWidgets.QLabel, "final_result_text")

        self.tableView_search_result.clicked.connect(self.on_tableView_search_result_clicked)


        self.apply_qss(QSS_FILE)


    def apply_qss(self, qss_path: str):
        if not os.path.exists(qss_path):
            return
        with open(qss_path, "r", encoding="utf-8") as f:
            qss = f.read()
        self.setStyleSheet(qss)


    @Slot()
    def on_pushButton_search_clicked(self):
        # print('clicked')

        try:
            search_str = self.lineEdit_search.text()
        except:
            print('error in search string')
            search_str = ''
            return

        if len(search_str)<3:
            QMessageBox.warning(self, "Warning", "Search text length \nshoud be greater then 3 !")
            return

        if self.radioButton_student.isChecked():
            self.df_search_result = self.student_reg.search(search_str)

        if self.radioButton_staff.isChecked():
            self.df_search_result = self.staff_reg.search(search_str)

        # print(df_search_result)

        self.tableView_model = DataFrameModel(self.df_search_result)
        self.tableView_search_result.setModel(self.tableView_model)
        self.tableView_search_result.resizeColumnsToContents()


    @Slot()
    def on_pushButton_now_clicked(self):
        now = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)


    def on_tableView_search_result_clicked(self, index: QModelIndex):
        if not index.isValid():
            val = None
        else:
            val = self.tableView_model.data(index, Qt.DisplayRole)

        colname = self.tableView_model.headerData(index.column(), Qt.Horizontal)

        rowidx = index.row()

        print(f"Clicked cell ({rowidx}, {colname}) = {val}")

        print(self.df_search_result.iloc[rowidx])
        s = ", ".join(self.df_search_result.iloc[rowidx].astype(str).tolist())
        self.final_result_text.setText(s)
    # -------------------------------------------------


def main():

    student_reg = student.Students()
    staff_reg = staff.Staffs()

    app = QApplication(sys.argv)
    w = MainWindow(student_reg, staff_reg)
    w.setWindowTitle("Find-Expected-Location-of-Person")
    w.resize(700, 800)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Hello from find-expected-location-of-person!")
    main()


