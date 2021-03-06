# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 575))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(900, 575))
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_TxParams = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_TxParams.sizePolicy().hasHeightForWidth())
        self.groupBox_TxParams.setSizePolicy(sizePolicy)
        self.groupBox_TxParams.setObjectName("groupBox_TxParams")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_TxParams)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_loadWaveFile = QtWidgets.QRadioButton(self.groupBox_TxParams)
        self.radioButton_loadWaveFile.setChecked(True)
        self.radioButton_loadWaveFile.setObjectName("radioButton_loadWaveFile")
        self.verticalLayout_2.addWidget(self.radioButton_loadWaveFile)
        self.widget_loadWaveFile = QtWidgets.QWidget(self.groupBox_TxParams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_loadWaveFile.sizePolicy().hasHeightForWidth())
        self.widget_loadWaveFile.setSizePolicy(sizePolicy)
        self.widget_loadWaveFile.setObjectName("widget_loadWaveFile")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_loadWaveFile)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_waveBrowse = QtWidgets.QPushButton(self.widget_loadWaveFile)
        self.pushButton_waveBrowse.setObjectName("pushButton_waveBrowse")
        self.gridLayout_2.addWidget(self.pushButton_waveBrowse, 2, 2, 1, 1)
        self.lineEdit_waveFileName = QtWidgets.QLineEdit(self.widget_loadWaveFile)
        self.lineEdit_waveFileName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_waveFileName.sizePolicy().hasHeightForWidth())
        self.lineEdit_waveFileName.setSizePolicy(sizePolicy)
        self.lineEdit_waveFileName.setReadOnly(True)
        self.lineEdit_waveFileName.setObjectName("lineEdit_waveFileName")
        self.gridLayout_2.addWidget(self.lineEdit_waveFileName, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_waveFilepath = QtWidgets.QLabel(self.widget_loadWaveFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_waveFilepath.sizePolicy().hasHeightForWidth())
        self.label_waveFilepath.setSizePolicy(sizePolicy)
        self.label_waveFilepath.setMinimumSize(QtCore.QSize(0, 0))
        self.label_waveFilepath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_waveFilepath.setObjectName("label_waveFilepath")
        self.gridLayout_2.addWidget(self.label_waveFilepath, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_loadWaveFile)
        self.radioButton_selectWaveform = QtWidgets.QRadioButton(self.groupBox_TxParams)
        self.radioButton_selectWaveform.setEnabled(True)
        self.radioButton_selectWaveform.setObjectName("radioButton_selectWaveform")
        self.verticalLayout_2.addWidget(self.radioButton_selectWaveform)
        self.widget_selectWaveform = QtWidgets.QWidget(self.groupBox_TxParams)
        self.widget_selectWaveform.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_selectWaveform.sizePolicy().hasHeightForWidth())
        self.widget_selectWaveform.setSizePolicy(sizePolicy)
        self.widget_selectWaveform.setObjectName("widget_selectWaveform")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_selectWaveform)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_waveform = QtWidgets.QComboBox(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_waveform.sizePolicy().hasHeightForWidth())
        self.comboBox_waveform.setSizePolicy(sizePolicy)
        self.comboBox_waveform.setObjectName("comboBox_waveform")
        self.comboBox_waveform.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_waveform, 0, 1, 1, 1)
        self.label_pulseWidth = QtWidgets.QLabel(self.widget_selectWaveform)
        self.label_pulseWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pulseWidth.setObjectName("label_pulseWidth")
        self.gridLayout_3.addWidget(self.label_pulseWidth, 5, 0, 1, 1)
        self.lineEdit_freq = QtWidgets.QLineEdit(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_freq.sizePolicy().hasHeightForWidth())
        self.lineEdit_freq.setSizePolicy(sizePolicy)
        self.lineEdit_freq.setObjectName("lineEdit_freq")
        self.gridLayout_3.addWidget(self.lineEdit_freq, 4, 1, 1, 1)
        self.label_waveform = QtWidgets.QLabel(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_waveform.sizePolicy().hasHeightForWidth())
        self.label_waveform.setSizePolicy(sizePolicy)
        self.label_waveform.setMinimumSize(QtCore.QSize(155, 0))
        self.label_waveform.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_waveform.setObjectName("label_waveform")
        self.gridLayout_3.addWidget(self.label_waveform, 0, 0, 1, 1)
        self.label_freq = QtWidgets.QLabel(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_freq.sizePolicy().hasHeightForWidth())
        self.label_freq.setSizePolicy(sizePolicy)
        self.label_freq.setMinimumSize(QtCore.QSize(0, 0))
        self.label_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_freq.setObjectName("label_freq")
        self.gridLayout_3.addWidget(self.label_freq, 4, 0, 1, 1)
        self.lineEdit_pulseWidth = QtWidgets.QLineEdit(self.widget_selectWaveform)
        self.lineEdit_pulseWidth.setObjectName("lineEdit_pulseWidth")
        self.gridLayout_3.addWidget(self.lineEdit_pulseWidth, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.lineEdit_numCycles = QtWidgets.QLineEdit(self.widget_selectWaveform)
        self.lineEdit_numCycles.setObjectName("lineEdit_numCycles")
        self.gridLayout_3.addWidget(self.lineEdit_numCycles, 1, 1, 1, 1)
        self.label_numCycles = QtWidgets.QLabel(self.widget_selectWaveform)
        self.label_numCycles.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numCycles.setObjectName("label_numCycles")
        self.gridLayout_3.addWidget(self.label_numCycles, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_selectWaveform)
        self.gridLayout.addWidget(self.groupBox_TxParams, 0, 1, 1, 1)
        self.groupBox_acqOptions = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_acqOptions.sizePolicy().hasHeightForWidth())
        self.groupBox_acqOptions.setSizePolicy(sizePolicy)
        self.groupBox_acqOptions.setObjectName("groupBox_acqOptions")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_acqOptions)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_acqOptions = QtWidgets.QWidget(self.groupBox_acqOptions)
        self.widget_acqOptions.setObjectName("widget_acqOptions")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_acqOptions)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_numSamps = QtWidgets.QLineEdit(self.widget_acqOptions)
        self.lineEdit_numSamps.setObjectName("lineEdit_numSamps")
        self.gridLayout_6.addWidget(self.lineEdit_numSamps, 1, 1, 1, 1)
        self.lineEdit_sampRate = QtWidgets.QLineEdit(self.widget_acqOptions)
        self.lineEdit_sampRate.setObjectName("lineEdit_sampRate")
        self.gridLayout_6.addWidget(self.lineEdit_sampRate, 2, 1, 1, 1)
        self.label_sampRate = QtWidgets.QLabel(self.widget_acqOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sampRate.sizePolicy().hasHeightForWidth())
        self.label_sampRate.setSizePolicy(sizePolicy)
        self.label_sampRate.setMinimumSize(QtCore.QSize(150, 0))
        self.label_sampRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sampRate.setObjectName("label_sampRate")
        self.gridLayout_6.addWidget(self.label_sampRate, 2, 0, 1, 1)
        self.label_numSamps = QtWidgets.QLabel(self.widget_acqOptions)
        self.label_numSamps.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numSamps.setObjectName("label_numSamps")
        self.gridLayout_6.addWidget(self.label_numSamps, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_acqOptions)
        self.gridLayout.addWidget(self.groupBox_acqOptions, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.horizontalLayout_begin = QtWidgets.QHBoxLayout()
        self.horizontalLayout_begin.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_begin.setSpacing(6)
        self.horizontalLayout_begin.setObjectName("horizontalLayout_begin")
        self.pushButton_runTest = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_runTest.setObjectName("pushButton_runTest")
        self.horizontalLayout_begin.addWidget(self.pushButton_runTest)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_begin.addItem(spacerItem4)
        self.pushButton_begin = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_begin.setObjectName("pushButton_begin")
        self.horizontalLayout_begin.addWidget(self.pushButton_begin)
        self.gridLayout.addLayout(self.horizontalLayout_begin, 4, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mapping = QtWidgets.QWidget()
        self.tab_mapping.setAutoFillBackground(True)
        self.tab_mapping.setObjectName("tab_mapping")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_mapping)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tableWidget_transMapping = QtWidgets.QTableWidget(self.tab_mapping)
        self.tableWidget_transMapping.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_transMapping.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget_transMapping.setAcceptDrops(False)
        self.tableWidget_transMapping.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_transMapping.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget_transMapping.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_transMapping.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_transMapping.setRowCount(60)
        self.tableWidget_transMapping.setColumnCount(2)
        self.tableWidget_transMapping.setObjectName("tableWidget_transMapping")
        self.tableWidget_transMapping.horizontalHeader().setVisible(True)
        self.tableWidget_transMapping.horizontalHeader().setHighlightSections(False)
        self.tableWidget_transMapping.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_transMapping.verticalHeader().setVisible(False)
        self.gridLayout_9.addWidget(self.tableWidget_transMapping, 1, 0, 1, 3)
        self.widget_loadTransFile_2 = QtWidgets.QWidget(self.tab_mapping)
        self.widget_loadTransFile_2.setObjectName("widget_loadTransFile_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_loadTransFile_2)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_mappingFilePath = QtWidgets.QLabel(self.widget_loadTransFile_2)
        self.label_mappingFilePath.setObjectName("label_mappingFilePath")
        self.gridLayout_5.addWidget(self.label_mappingFilePath, 0, 1, 1, 1)
        self.pushButton_mappingBrowse = QtWidgets.QPushButton(self.widget_loadTransFile_2)
        self.pushButton_mappingBrowse.setObjectName("pushButton_mappingBrowse")
        self.gridLayout_5.addWidget(self.pushButton_mappingBrowse, 1, 2, 1, 1)
        self.lineEdit_mappingFileName = QtWidgets.QLineEdit(self.widget_loadTransFile_2)
        self.lineEdit_mappingFileName.setReadOnly(True)
        self.lineEdit_mappingFileName.setObjectName("lineEdit_mappingFileName")
        self.gridLayout_5.addWidget(self.lineEdit_mappingFileName, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.widget_loadTransFile_2, 0, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 2, 1, 1, 1)
        self.pushButton_saveMapping = QtWidgets.QPushButton(self.tab_mapping)
        self.pushButton_saveMapping.setObjectName("pushButton_saveMapping")
        self.gridLayout_9.addWidget(self.pushButton_saveMapping, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab_mapping, "")
        self.tab_switch = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_switch.sizePolicy().hasHeightForWidth())
        self.tab_switch.setSizePolicy(sizePolicy)
        self.tab_switch.setAutoFillBackground(True)
        self.tab_switch.setObjectName("tab_switch")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_switch)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 2, 3, 1, 1)
        self.widget_loadTransFile = QtWidgets.QWidget(self.tab_switch)
        self.widget_loadTransFile.setObjectName("widget_loadTransFile")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_loadTransFile)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_transFilePath = QtWidgets.QLabel(self.widget_loadTransFile)
        self.label_transFilePath.setObjectName("label_transFilePath")
        self.gridLayout_4.addWidget(self.label_transFilePath, 0, 1, 1, 1)
        self.pushButton_transBrowse = QtWidgets.QPushButton(self.widget_loadTransFile)
        self.pushButton_transBrowse.setObjectName("pushButton_transBrowse")
        self.gridLayout_4.addWidget(self.pushButton_transBrowse, 1, 2, 1, 1)
        self.lineEdit_transFileName = QtWidgets.QLineEdit(self.widget_loadTransFile)
        self.lineEdit_transFileName.setReadOnly(True)
        self.lineEdit_transFileName.setObjectName("lineEdit_transFileName")
        self.gridLayout_4.addWidget(self.lineEdit_transFileName, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.widget_loadTransFile, 0, 0, 1, 5)
        self.tableWidget_transConfig = QtWidgets.QTableWidget(self.tab_switch)
        self.tableWidget_transConfig.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_transConfig.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget_transConfig.setAcceptDrops(False)
        self.tableWidget_transConfig.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_transConfig.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget_transConfig.setProperty("showDropIndicator", False)
        self.tableWidget_transConfig.setDragEnabled(False)
        self.tableWidget_transConfig.setDragDropOverwriteMode(False)
        self.tableWidget_transConfig.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_transConfig.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_transConfig.setAlternatingRowColors(False)
        self.tableWidget_transConfig.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_transConfig.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_transConfig.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_transConfig.setObjectName("tableWidget_transConfig")
        self.tableWidget_transConfig.setColumnCount(0)
        self.tableWidget_transConfig.setRowCount(0)
        self.tableWidget_transConfig.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_transConfig.verticalHeader().setStretchLastSection(False)
        self.gridLayout_8.addWidget(self.tableWidget_transConfig, 1, 0, 1, 5)
        self.pushButton_saveTrans = QtWidgets.QPushButton(self.tab_switch)
        self.pushButton_saveTrans.setObjectName("pushButton_saveTrans")
        self.gridLayout_8.addWidget(self.pushButton_saveTrans, 2, 4, 1, 1)
        self.pushButton_addRow = QtWidgets.QPushButton(self.tab_switch)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.gridLayout_8.addWidget(self.pushButton_addRow, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_switch, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 4, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 17))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_mappingFileName, self.pushButton_mappingBrowse)
        MainWindow.setTabOrder(self.pushButton_mappingBrowse, self.tableWidget_transMapping)
        MainWindow.setTabOrder(self.tableWidget_transMapping, self.pushButton_saveMapping)
        MainWindow.setTabOrder(self.pushButton_saveMapping, self.lineEdit_transFileName)
        MainWindow.setTabOrder(self.lineEdit_transFileName, self.pushButton_transBrowse)
        MainWindow.setTabOrder(self.pushButton_transBrowse, self.tableWidget_transConfig)
        MainWindow.setTabOrder(self.tableWidget_transConfig, self.pushButton_addRow)
        MainWindow.setTabOrder(self.pushButton_addRow, self.pushButton_saveTrans)
        MainWindow.setTabOrder(self.pushButton_saveTrans, self.radioButton_loadWaveFile)
        MainWindow.setTabOrder(self.radioButton_loadWaveFile, self.lineEdit_waveFileName)
        MainWindow.setTabOrder(self.lineEdit_waveFileName, self.pushButton_waveBrowse)
        MainWindow.setTabOrder(self.pushButton_waveBrowse, self.radioButton_selectWaveform)
        MainWindow.setTabOrder(self.radioButton_selectWaveform, self.comboBox_waveform)
        MainWindow.setTabOrder(self.comboBox_waveform, self.lineEdit_numCycles)
        MainWindow.setTabOrder(self.lineEdit_numCycles, self.lineEdit_freq)
        MainWindow.setTabOrder(self.lineEdit_freq, self.lineEdit_pulseWidth)
        MainWindow.setTabOrder(self.lineEdit_pulseWidth, self.lineEdit_numSamps)
        MainWindow.setTabOrder(self.lineEdit_numSamps, self.lineEdit_sampRate)
        MainWindow.setTabOrder(self.lineEdit_sampRate, self.pushButton_runTest)
        MainWindow.setTabOrder(self.pushButton_runTest, self.pushButton_begin)
        MainWindow.setTabOrder(self.pushButton_begin, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ultrasound Breast Imaging"))
        self.groupBox_TxParams.setTitle(_translate("MainWindow", "Transmission Parameters"))
        self.radioButton_loadWaveFile.setText(_translate("MainWindow", "Load Waveform"))
        self.widget_loadWaveFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>Samples are clocked in at 125 MHz</p></body></html>"))
        self.pushButton_waveBrowse.setText(_translate("MainWindow", "Browse..."))
        self.label_waveFilepath.setText(_translate("MainWindow", "File Path:"))
        self.radioButton_selectWaveform.setText(_translate("MainWindow", "Select Waveform"))
        self.comboBox_waveform.setItemText(0, _translate("MainWindow", "Sinusoid"))
        self.label_pulseWidth.setText(_translate("MainWindow", "Pulse Width (μs):"))
        self.label_waveform.setText(_translate("MainWindow", "Waveform Type:"))
        self.label_freq.setText(_translate("MainWindow", "Frequency (MHz):"))
        self.label_numCycles.setText(_translate("MainWindow", "Number of Cycles:"))
        self.groupBox_acqOptions.setTitle(_translate("MainWindow", "Acquisition Options"))
        self.label_sampRate.setText(_translate("MainWindow", "Sampling Rate (MHz):"))
        self.label_numSamps.setText(_translate("MainWindow", "Number of Samples:"))
        self.pushButton_runTest.setText(_translate("MainWindow", "Run Test"))
        self.pushButton_begin.setText(_translate("MainWindow", "Begin"))
        self.tableWidget_transMapping.setSortingEnabled(True)
        self.label_mappingFilePath.setText(_translate("MainWindow", "File Path:"))
        self.pushButton_mappingBrowse.setText(_translate("MainWindow", "Browse..."))
        self.pushButton_saveMapping.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mapping), _translate("MainWindow", "Transducer Mapping"))
        self.label_transFilePath.setText(_translate("MainWindow", "File Path:"))
        self.pushButton_transBrowse.setText(_translate("MainWindow", "Browse..."))
        self.tableWidget_transConfig.setSortingEnabled(False)
        self.pushButton_saveTrans.setText(_translate("MainWindow", "Save"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_switch), _translate("MainWindow", "Transducer Configuration"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

