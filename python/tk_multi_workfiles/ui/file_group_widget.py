# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_group_widget.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_FileGroupWidget(object):
    def setupUi(self, FileGroupWidget):
        FileGroupWidget.setObjectName("FileGroupWidget")
        FileGroupWidget.resize(305, 49)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileGroupWidget.sizePolicy().hasHeightForWidth())
        FileGroupWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(FileGroupWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.expand_check_box = QtGui.QCheckBox(FileGroupWidget)
        self.expand_check_box.setStyleSheet("#expand_check_box::indicator {\n"
"width: 12;\n"
"height: 12;\n"
"}\n"
"\n"
"#expand_check_box {\n"
"font: 14px;\n"
"}\n"
"\n"
"#expand_check_box::indicator::unchecked {\n"
"    image: url(:/tk-multi-workfiles/tree_arrow_collapsed.png);\n"
"\n"
"}\n"
"\n"
"#expand_check_box::indicator::unchecked::hover {\n"
"    image: url(:/tk-multi-workfiles/tree_arrow_collapsed.png);\n"
"}\n"
"\n"
"#expand_check_box::indicator::checked {\n"
"    image: url(:/tk-multi-workfiles/tree_arrow_expanded.png);\n"
"}\n"
"\n"
"/*#grid_radio_btn::indicator::checked::hover {\n"
"    image: url(:/tk-multi-workfiles/grid_view_checked_hover.png);\n"
"}*/")
        self.expand_check_box.setIconSize(QtCore.QSize(16, 16))
        self.expand_check_box.setObjectName("expand_check_box")
        self.horizontalLayout.addWidget(self.expand_check_box)
        self.spinner = QtGui.QLabel(FileGroupWidget)
        self.spinner.setMinimumSize(QtCore.QSize(20, 20))
        self.spinner.setMaximumSize(QtCore.QSize(20, 20))
        self.spinner.setStyleSheet("")
        self.spinner.setText("")
        self.spinner.setObjectName("spinner")
        self.horizontalLayout.addWidget(self.spinner)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtGui.QFrame(FileGroupWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.msg_label = QtGui.QLabel(FileGroupWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy)
        self.msg_label.setStyleSheet("#msg_label {\n"
"font: 11px;\n"
"color: grey;\n"
"}")
        self.msg_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msg_label.setWordWrap(True)
        self.msg_label.setMargin(2)
        self.msg_label.setObjectName("msg_label")
        self.verticalLayout_2.addWidget(self.msg_label)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(FileGroupWidget)
        QtCore.QMetaObject.connectSlotsByName(FileGroupWidget)

    def retranslateUi(self, FileGroupWidget):
        FileGroupWidget.setWindowTitle(QtGui.QApplication.translate("FileGroupWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.expand_check_box.setText(QtGui.QApplication.translate("FileGroupWidget", "Layout - Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.msg_label.setText(QtGui.QApplication.translate("FileGroupWidget", "Searching for files...", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
