# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np

from PandasModel import PandasModel

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(176, 0))
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(278, 16777215))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.verticalFrame_2)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.itemSelectionChanged.connect(self.on_change)
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addWidget(self.verticalFrame_2, 0, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableView = QtWidgets.QTableView(self.verticalFrame)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.gridLayout.addWidget(self.verticalFrame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave_as.triggered.connect(self.fileSave)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grind"))
        self.label.setText(_translate("MainWindow", "Select Columns to preserve:"))
        self.label_2.setText(_translate("MainWindow", "Output Format"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Import..."))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))

    def on_change(self):
        self.stable = []
        for item in self.listWidget.selectedItems():
            self.stable.append(item.text())
        fra = {}
        delm = "/"
        neg = "neg"
        for col in self.asd.columns.drop(self.stable):
            nstable = self.stable.copy()
            nstable.append(col)
            df = self.asd.loc[:, nstable[:]]
            nstable = self.stable.copy()
            nstable.append('Value')
            df.columns = nstable
            df.name = col
            if col == neg:
                fra["".join(col)] = df
                continue
            col = col.split(delm)
            for i in range(len(col)):
                if col[i] in df.columns.tolist():
                    break
                df.insert(loc = len(self.stable) + 1 + i, column = col[i], value='+')
            fra["".join(col)] = df
        
        # Concatenate all dataframes in fra dictionary
        df=fra[list(fra.keys())[0]]
        for i in range(1, len(list(fra.keys()))):
            df = df.append(fra[list(fra.keys())[i]])    
            
        # Replace NaN with '-'
        df = df.replace(np.nan, '-')
        
        # Rearrange column names
        col = df.columns.tolist()
        col.remove('Value')
        for i in reversed(range(len(self.stable))):
            col.remove(self.stable[i])
            col.insert(0, self.stable[i])
        col.append('Value')
        self.df = df[col].reset_index(drop=True)
        model=PandasModel(self.df)
        self.tableView.setModel(model)

    def fileOpen(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        MainWindow.setWindowTitle(" - ".join(["Grrrrind",fileName]))
        self.asd = pd.read_csv(fileName, delimiter=',')
        self.listWidget.addItems(self.asd.columns)

    def fileSave(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        # Write csv
        self.df.to_csv(fileName, index=False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

