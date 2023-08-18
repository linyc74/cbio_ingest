import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, \
    QFileDialog, QMessageBox, QGridLayout, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from typing import List, Union
from .model import Model


class Table(QTableWidget):

    model: Model

    def __init__(self, model: Model):
        super().__init__()
        self.model = model
        self.refresh_table()

    def refresh_table(self):
        df = self.model.get_dataframe()

        self.setRowCount(len(df.index))
        self.setColumnCount(len(df.columns))

        self.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # makes the item immutable, i.e. user cannot edit it
                self.setItem(i, j, item)

        self.resizeColumnsToContents()

    def get_selected_rows(self) -> List[int]:
        ret = []
        for item in self.selectedItems():
            ith_row = item.row()
            if ith_row not in ret:
                ret.append(ith_row)
        return ret

    def get_selected_columns(self) -> List[str]:
        ret = []
        for item in self.selectedItems():
            ith_col = item.column()
            column = self.horizontalHeaderItem(ith_col).text()
            if column not in ret:
                ret.append(column)
        return ret


class View(QWidget):

    TITLE = 'cBioIngest'
    ICON_PNG = f'{os.getcwd()}/icon/logo.ico'
    WIDTH, HEIGHT = 1280, 768
    BUTTON_NAME_TO_LABEL = {
        'button_1': 'Button 1',
    }
    BUTTON_NAME_TO_POSITION = {
        'button_1': (0, 0),
    }

    model: Model
    vertical_layout: QVBoxLayout
    table: Table
    button_grid: QGridLayout

    def __init__(self, model: Model):
        super().__init__()
        self.model = model

        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QIcon(self.ICON_PNG))
        self.resize(self.WIDTH, self.HEIGHT)

        self.__init__vertical_layout()
        self.__init__main_table()
        self.__init__buttons()
        self.__init__methods()

    def __init__vertical_layout(self):
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

    def __init__main_table(self):
        self.table = Table(self.model)
        self.vertical_layout.addWidget(self.table)

    def __init__buttons(self):
        self.button_grid = QGridLayout()
        self.vertical_layout.addLayout(self.button_grid)

        for name, label in self.BUTTON_NAME_TO_LABEL.items():
            setattr(self, f'button_{name}', QPushButton(label))
            button = getattr(self, f'button_{name}')
            pos = self.BUTTON_NAME_TO_POSITION[name]
            self.button_grid.addWidget(button, *pos)

    def __init__methods(self):
        self.file_dialog_open_table = FileDialogOpenTable(self)
        self.file_dialog_save_table = FileDialogSaveTable(self)
        self.file_dialog_open_directory = FileDialogOpenDirectory(self)
        self.message_box_info = MessageBoxInfo(self)
        self.message_box_error = MessageBoxError(self)
        self.message_box_yes_no = MessageBoxYesNo(self)
        self.dialog_read1_read2_suffix = DialogRead1Read2Suffix(self)
        self.dialog_bed_file = DialogBedFile(self)

    def refresh_table(self):
        self.table.refresh_table()

    def get_selected_rows(self) -> List[int]:
        return self.table.get_selected_rows()

    def get_selected_columns(self) -> List[str]:
        return self.table.get_selected_columns()


class FileDialog:

    parent: QWidget

    def __init__(self, parent: QWidget):
        self.parent = parent


class FileDialogOpenTable(FileDialog):

    def __call__(self) -> str:
        fpath, ftype = QFileDialog.getOpenFileName(
            parent=self.parent,
            caption='Open',
            filter='All Files (*.*);;CSV files (*.csv);;Excel files (*.xlsx)',
            initialFilter='CSV files (*.csv)',
            options=QFileDialog.DontUseNativeDialog
        )
        return fpath


class FileDialogSaveTable(FileDialog):

    def __call__(self, filename: str = '') -> str:
        fpath, ftype = QFileDialog.getSaveFileName(
            parent=self.parent,
            caption='Save As',
            directory=filename,
            filter='All Files (*.*);;CSV files (*.csv);;Excel files (*.xlsx)',
            initialFilter='CSV files (*.csv)',
            options=QFileDialog.DontUseNativeDialog
        )
        return fpath


class FileDialogOpenDirectory(FileDialog):

    def __call__(self, caption: str) -> str:
        fpath = QFileDialog.getExistingDirectory(
            parent=self.parent,
            caption=caption,
            options=QFileDialog.DontUseNativeDialog
        )
        return fpath


class MessageBox:

    TITLE: str
    ICON: QMessageBox.Icon

    box: QMessageBox

    def __init__(self, parent: QWidget):
        self.box = QMessageBox(parent)
        self.box.setWindowTitle(self.TITLE)
        self.box.setIcon(self.ICON)

    def __call__(self, msg: str):
        self.box.setText(msg)
        self.box.exec_()


class MessageBoxInfo(MessageBox):

    TITLE = 'Info'
    ICON = QMessageBox.Information


class MessageBoxError(MessageBox):

    TITLE = 'Error'
    ICON = QMessageBox.Warning


class MessageBoxYesNo(MessageBox):

    TITLE = ' '
    ICON = QMessageBox.Question

    def __init__(self, parent: QWidget):
        super(MessageBoxYesNo, self).__init__(parent)
        self.box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.box.setDefaultButton(QMessageBox.No)

    def __call__(self, msg: str) -> bool:
        self.box.setText(msg)
        return self.box.exec_() == QMessageBox.Yes


class DialogLineEdits:

    LINE_TITLES: List[str]
    LINE_DEFAULTS: List[str]

    parent: QWidget

    dialog: QDialog
    layout: QFormLayout
    line_edits: List[QLineEdit]
    button_box: QDialogButtonBox

    def __init__(self, parent: QWidget):
        self.parent = parent
        self.__init__dialog()
        self.__init__layout()
        self.__init__line_edits()
        self.__init__button_box()

    def __init__dialog(self):
        self.dialog = QDialog(parent=self.parent)
        self.dialog.setWindowTitle(' ')

    def __init__layout(self):
        self.layout = QFormLayout(parent=self.dialog)

    def __init__line_edits(self):
        self.line_edits = []
        for title, default in zip(self.LINE_TITLES, self.LINE_DEFAULTS):
            line_edit = QLineEdit(default, parent=self.dialog)
            self.line_edits.append(line_edit)
            self.layout.addRow(title, line_edit)

    def __init__button_box(self):
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self.dialog)
        self.button_box.accepted.connect(self.dialog.accept)
        self.button_box.rejected.connect(self.dialog.reject)
        self.layout.addWidget(self.button_box)

    def __call__(self) -> Union[str, tuple]:
        if self.dialog.exec_() == QDialog.Accepted:
            ret = tuple(e.text() for e in self.line_edits)
        else:
            ret = tuple('' for _ in self.LINE_DEFAULTS)

        return ret if len(ret) > 1 else ret[0]


class DialogRead1Read2Suffix(DialogLineEdits):

    LINE_TITLES = [
        'Read 1 Suffix:',
        'Read 2 Suffix:',
    ]
    LINE_DEFAULTS = [
        '_R1.fastq.gz',
        '_R2.fastq.gz',
    ]


class DialogBedFile(DialogLineEdits):

    LINE_TITLES = [
        'BED File:',
    ]
    LINE_DEFAULTS = [
        '*.bed',
    ]