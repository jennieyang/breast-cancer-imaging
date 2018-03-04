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
        MainWindow.resize(1080, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 600))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(1080, 600))
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
        self.label_waveform = QtWidgets.QLabel(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_waveform.sizePolicy().hasHeightForWidth())
        self.label_waveform.setSizePolicy(sizePolicy)
        self.label_waveform.setMinimumSize(QtCore.QSize(0, 0))
        self.label_waveform.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_waveform.setObjectName("label_waveform")
        self.gridLayout_3.addWidget(self.label_waveform, 1, 1, 1, 1)
        self.comboBox_waveform = QtWidgets.QComboBox(self.widget_selectWaveform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_waveform.sizePolicy().hasHeightForWidth())
        self.comboBox_waveform.setSizePolicy(sizePolicy)
        self.comboBox_waveform.setObjectName("comboBox_waveform")
        self.comboBox_waveform.addItem("")
        self.comboBox_waveform.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_waveform, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_selectWaveform)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.groupBox_TxParams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amplitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_amplitude.setSizePolicy(sizePolicy)
        self.lineEdit_amplitude.setObjectName("lineEdit_amplitude")
        self.gridLayout_7.addWidget(self.lineEdit_amplitude, 0, 1, 1, 1)
        self.label_freqUnit = QtWidgets.QLabel(self.groupBox_TxParams)
        self.label_freqUnit.setObjectName("label_freqUnit")
        self.gridLayout_7.addWidget(self.label_freqUnit, 1, 2, 1, 1)
        self.lineEdit_freq = QtWidgets.QLineEdit(self.groupBox_TxParams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_freq.sizePolicy().hasHeightForWidth())
        self.lineEdit_freq.setSizePolicy(sizePolicy)
        self.lineEdit_freq.setObjectName("lineEdit_freq")
        self.gridLayout_7.addWidget(self.lineEdit_freq, 1, 1, 1, 1)
        self.label_amplitude = QtWidgets.QLabel(self.groupBox_TxParams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_amplitude.sizePolicy().hasHeightForWidth())
        self.label_amplitude.setSizePolicy(sizePolicy)
        self.label_amplitude.setMinimumSize(QtCore.QSize(0, 0))
        self.label_amplitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_amplitude.setObjectName("label_amplitude")
        self.gridLayout_7.addWidget(self.label_amplitude, 0, 0, 1, 1)
        self.label_freq = QtWidgets.QLabel(self.groupBox_TxParams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_freq.sizePolicy().hasHeightForWidth())
        self.label_freq.setSizePolicy(sizePolicy)
        self.label_freq.setMinimumSize(QtCore.QSize(0, 0))
        self.label_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_freq.setObjectName("label_freq")
        self.gridLayout_7.addWidget(self.label_freq, 1, 0, 1, 1)
        self.label_ampUnit = QtWidgets.QLabel(self.groupBox_TxParams)
        self.label_ampUnit.setObjectName("label_ampUnit")
        self.gridLayout_7.addWidget(self.label_ampUnit, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
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
        self.label_sampRateUnit = QtWidgets.QLabel(self.widget_acqOptions)
        self.label_sampRateUnit.setObjectName("label_sampRateUnit")
        self.gridLayout_6.addWidget(self.label_sampRateUnit, 2, 2, 1, 1)
        self.label_numSamps = QtWidgets.QLabel(self.widget_acqOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_numSamps.sizePolicy().hasHeightForWidth())
        self.label_numSamps.setSizePolicy(sizePolicy)
        self.label_numSamps.setMinimumSize(QtCore.QSize(150, 0))
        self.label_numSamps.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numSamps.setObjectName("label_numSamps")
        self.gridLayout_6.addWidget(self.label_numSamps, 1, 0, 1, 1)
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
        self.label_numSampsUnit = QtWidgets.QLabel(self.widget_acqOptions)
        self.label_numSampsUnit.setObjectName("label_numSampsUnit")
        self.gridLayout_6.addWidget(self.label_numSampsUnit, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_acqOptions)
        self.gridLayout.addWidget(self.groupBox_acqOptions, 1, 1, 1, 1)
        self.horizontalLayout_begin = QtWidgets.QHBoxLayout()
        self.horizontalLayout_begin.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_begin.setSpacing(6)
        self.horizontalLayout_begin.setObjectName("horizontalLayout_begin")
        self.pushButton_runTest = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_runTest.setObjectName("pushButton_runTest")
        self.horizontalLayout_begin.addWidget(self.pushButton_runTest)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_begin.addItem(spacerItem3)
        self.pushButton_begin = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_begin.setObjectName("pushButton_begin")
        self.horizontalLayout_begin.addWidget(self.pushButton_begin)
        self.gridLayout.addLayout(self.horizontalLayout_begin, 2, 0, 1, 2)
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
        self.tableWidget_transMapping.setProperty("showDropIndicator", False)
        self.tableWidget_transMapping.setDragEnabled(False)
        self.tableWidget_transMapping.setDragDropOverwriteMode(False)
        self.tableWidget_transMapping.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_transMapping.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_transMapping.setAlternatingRowColors(False)
        self.tableWidget_transMapping.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_transMapping.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_transMapping.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_transMapping.setRowCount(60)
        self.tableWidget_transMapping.setColumnCount(2)
        self.tableWidget_transMapping.setObjectName("tableWidget_transMapping")
        self.tableWidget_transMapping.horizontalHeader().setVisible(True)
        self.tableWidget_transMapping.horizontalHeader().setHighlightSections(False)
        self.tableWidget_transMapping.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_transMapping.verticalHeader().setVisible(False)
        self.tableWidget_transMapping.verticalHeader().setHighlightSections(False)
        self.tableWidget_transMapping.verticalHeader().setStretchLastSection(False)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 2, 1, 1, 1)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 2, 3, 1, 1)
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
        self.tableWidget_transConfig.setProperty("showDropIndicator", False)
        self.tableWidget_transConfig.setDragEnabled(False)
        self.tableWidget_transConfig.setDragDropOverwriteMode(False)
        self.tableWidget_transConfig.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_transConfig.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_transConfig.setAlternatingRowColors(False)
        self.tableWidget_transConfig.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
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
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1080, 17))
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
        MainWindow.setTabOrder(self.radioButton_loadWaveFile, self.radioButton_selectWaveform)
        MainWindow.setTabOrder(self.radioButton_selectWaveform, self.lineEdit_waveFileName)
        MainWindow.setTabOrder(self.lineEdit_waveFileName, self.pushButton_waveBrowse)
        MainWindow.setTabOrder(self.pushButton_waveBrowse, self.comboBox_waveform)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ultrasound Breast Imaging"))
        self.groupBox_TxParams.setTitle(_translate("MainWindow", "Transmission Parameters"))
        self.radioButton_loadWaveFile.setText(_translate("MainWindow", "Load Waveform"))
        self.pushButton_waveBrowse.setText(_translate("MainWindow", "Browse..."))
        self.label_waveFilepath.setText(_translate("MainWindow", "File Path:"))
        self.radioButton_selectWaveform.setText(_translate("MainWindow", "Select Waveform"))
        self.label_waveform.setText(_translate("MainWindow", "Waveform:"))
        self.comboBox_waveform.setItemText(0, _translate("MainWindow", "Sinusoid"))
        self.comboBox_waveform.setItemText(1, _translate("MainWindow", "Square"))
        self.label_freqUnit.setText(_translate("MainWindow", "Hz"))
        self.label_amplitude.setText(_translate("MainWindow", "Amplitude:"))
        self.label_freq.setText(_translate("MainWindow", "Frequency:"))
        self.label_ampUnit.setText(_translate("MainWindow", "V"))
        self.groupBox_acqOptions.setTitle(_translate("MainWindow", "Acquisition Options"))
        self.label_sampRateUnit.setText(_translate("MainWindow", "MHz"))
        self.label_numSamps.setText(_translate("MainWindow", "Number of Samples:"))
        self.label_sampRate.setText(_translate("MainWindow", "Sampling Rate:"))
        self.label_numSampsUnit.setText(_translate("MainWindow", "Samples"))
        self.pushButton_runTest.setText(_translate("MainWindow", "Run Test"))
        self.pushButton_begin.setText(_translate("MainWindow", "Begin"))
        self.tableWidget_transMapping.setSortingEnabled(False)
        self.label_mappingFilePath.setText(_translate("MainWindow", "File Path:"))
        self.pushButton_mappingBrowse.setText(_translate("MainWindow", "Browse..."))
        self.pushButton_saveMapping.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mapping), _translate("MainWindow", "Transducer Mapping"))
        self.label_transFilePath.setText(_translate("MainWindow", "File Path:"))
        self.pushButton_transBrowse.setText(_translate("MainWindow", "Browse..."))
        self.tableWidget_transConfig.setSortingEnabled(False)
        self.pushButton_saveTrans.setText(_translate("MainWindow", "Save"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_switch), _translate("MainWindow", "Switch Configuration"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

