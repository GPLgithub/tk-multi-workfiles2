# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_save_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_FileSaveForm(object):
    def setupUi(self, FileSaveForm):
        FileSaveForm.setObjectName("FileSaveForm")
        FileSaveForm.resize(532, 466)
        self.verticalLayout = QtGui.QVBoxLayout(FileSaveForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(-1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.expand_checkbox = QtGui.QCheckBox(FileSaveForm)
        self.expand_checkbox.setText("")
        self.expand_checkbox.setObjectName("expand_checkbox")
        self.horizontalLayout_3.addWidget(self.expand_checkbox)
        self.nav_stacked_widget = QtGui.QStackedWidget(FileSaveForm)
        self.nav_stacked_widget.setLineWidth(1)
        self.nav_stacked_widget.setObjectName("nav_stacked_widget")
        self.location_page = QtGui.QWidget()
        self.location_page.setObjectName("location_page")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.location_page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.location_page)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.nav_stacked_widget.addWidget(self.location_page)
        self.history_nav_page = QtGui.QWidget()
        self.history_nav_page.setObjectName("history_nav_page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.history_nav_page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.history_btns = NavigationWidget(self.history_nav_page)
        self.history_btns.setMinimumSize(QtCore.QSize(60, 30))
        self.history_btns.setStyleSheet("#history_btns {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.history_btns.setObjectName("history_btns")
        self.horizontalLayout.addWidget(self.history_btns)
        self.nav_stacked_widget.addWidget(self.history_nav_page)
        self.horizontalLayout_3.addWidget(self.nav_stacked_widget)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.breadcrumbs = BreadcrumbWidget(FileSaveForm)
        self.breadcrumbs.setStyleSheet("#breadcrumbs {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.breadcrumbs.setObjectName("breadcrumbs")
        self.gridLayout_2.addWidget(self.breadcrumbs, 0, 1, 1, 1)
        self.gridLayout_2.setColumnMinimumWidth(0, 100)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.browser = BrowserForm(FileSaveForm)
        self.browser.setStyleSheet("#browser {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.browser.setObjectName("browser")
        self.verticalLayout_3.addWidget(self.browser)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtGui.QFrame(FileSaveForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(12, 4, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(-1)
        self.gridLayout.setObjectName("gridLayout")
        self.file_type_menu = QtGui.QComboBox(FileSaveForm)
        self.file_type_menu.setObjectName("file_type_menu")
        self.gridLayout.addWidget(self.file_type_menu, 1, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(FileSaveForm)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 3, 1, 1)
        self.name_edit = QtGui.QLineEdit(FileSaveForm)
        self.name_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name_edit.setFrame(True)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.file_type_label = QtGui.QLabel(FileSaveForm)
        self.file_type_label.setMinimumSize(QtCore.QSize(0, 0))
        self.file_type_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.file_type_label.setIndent(4)
        self.file_type_label.setObjectName("file_type_label")
        self.gridLayout.addWidget(self.file_type_label, 1, 0, 1, 1)
        self.name_label = QtGui.QLabel(FileSaveForm)
        self.name_label.setMinimumSize(QtCore.QSize(0, 0))
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.name_label.setIndent(4)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.version_label = QtGui.QLabel(FileSaveForm)
        self.version_label.setMinimumSize(QtCore.QSize(0, 0))
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setIndent(4)
        self.version_label.setObjectName("version_label")
        self.gridLayout.addWidget(self.version_label, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(-1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.path_preview_edit_2 = QtGui.QTextEdit(FileSaveForm)
        self.path_preview_edit_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_preview_edit_2.sizePolicy().hasHeightForWidth())
        self.path_preview_edit_2.setSizePolicy(sizePolicy)
        self.path_preview_edit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.path_preview_edit_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.path_preview_edit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.path_preview_edit_2.setStyleSheet("QTextEdit {\n"
"background-color: rgb(0,0,0,0);\n"
"border-style: none;\n"
"}")
        self.path_preview_edit_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.path_preview_edit_2.setFrameShadow(QtGui.QFrame.Plain)
        self.path_preview_edit_2.setLineWidth(0)
        self.path_preview_edit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.path_preview_edit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_preview_edit_2.setReadOnly(True)
        self.path_preview_edit_2.setAcceptRichText(True)
        self.path_preview_edit_2.setObjectName("path_preview_edit_2")
        self.gridLayout_3.addWidget(self.path_preview_edit_2, 1, 1, 1, 1)
        self.preview_label_2 = QtGui.QLabel(FileSaveForm)
        self.preview_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.preview_label_2.setIndent(4)
        self.preview_label_2.setObjectName("preview_label_2")
        self.gridLayout_3.addWidget(self.preview_label_2, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(FileSaveForm)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_7.setMargin(4)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.filename_preview_label_2 = QtGui.QLabel(FileSaveForm)
        self.filename_preview_label_2.setIndent(4)
        self.filename_preview_label_2.setObjectName("filename_preview_label_2")
        self.gridLayout_3.addWidget(self.filename_preview_label_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnMinimumWidth(0, 100)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.break_line = QtGui.QFrame(FileSaveForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cancel_btn = QtGui.QPushButton(FileSaveForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.save_btn = QtGui.QPushButton(FileSaveForm)
        self.save_btn.setDefault(True)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FileSaveForm)
        self.nav_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FileSaveForm)

    def retranslateUi(self, FileSaveForm):
        FileSaveForm.setWindowTitle(QtGui.QApplication.translate("FileSaveForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Location:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_type_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">File Type:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Name:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Version #:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.path_preview_edit_2.setHtml(QtGui.QApplication.translate("FileSaveForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/foo/bar/...</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">line 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">line 3</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.preview_label_2.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Preview:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FileSaveForm", "<html><head/><body><p><span style=\" font-weight:600;\">Work Area:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.filename_preview_label_2.setText(QtGui.QApplication.translate("FileSaveForm", "name.v001.ma", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("FileSaveForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("FileSaveForm", "Save", None, QtGui.QApplication.UnicodeUTF8))

from ..navigation_widget import NavigationWidget
from ..breadcrumb_widget import BreadcrumbWidget
from ..browser_form import BrowserForm
from . import resources_rc
