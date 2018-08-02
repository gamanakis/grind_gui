#!/usr/bin/env python3
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
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave_as.triggered.connect(self.fileSave)
        self.actionAbout.triggered.connect(self.helpAbout)
        self.actionLicense.triggered.connect(self.helpLicense)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grind"))
        self.label.setText(_translate("MainWindow", "Select Columns to preserve:"))
        self.label_2.setText(_translate("MainWindow", "Output Format:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Import..."))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionLicense.setText(_translate("MainWindow", "License..."))

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
        MainWindow.setWindowTitle(" - ".join(["Grind",fileName]))
        self.asd = pd.read_csv(fileName, delimiter=',')
        self.listWidget.addItems(self.asd.columns)

    def fileSave(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        # Write csv
        self.df.to_csv(fileName, index=False)

    def helpAbout(self):
        message = """
This program converts exported table data from FlowJo to a format 
suitable for use with SPICE (niaid.github.io/spice)
Copyright (C) 2018 Georgios Amanakis (gamanakis@gmail.com)

Export the Combination Gates from FlowJo in a ".csv" file
with the following header format (see Book1.csv):
    Subject | Marker-1 | Marker-2 | Marker-1/Marker-2 | neg

Multiple markers should be delimited with "/".
The column where none of the markers is expressed should be
labeled "neg".

To import this file select "File->Import...".
In the program window, select in the left list the columns
which should be preserved in the transformation. Usually
these are the "Subjects" and any column to be used as
overlay in SPICE.

The transformation appears in the right table. Check it, 
and save with "File->Save as...".
"""
        QMessageBox.about(self, "About", message)

    def helpLicense(self):
        message = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
"""
        QMessageBox.about(self, "License", message)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

