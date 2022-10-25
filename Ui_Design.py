# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestGUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1610, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1026, 792))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(260, 200, 63, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.displayLabel = QtWidgets.QLabel(self.groupBox)
        self.displayLabel.setGeometry(QtCore.QRect(10, 20, 995, 733))
        self.displayLabel.setText("")
        self.displayLabel.setObjectName("displayLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1040, 17, 261, 551))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboDevices = QtWidgets.QComboBox(self.groupBox_2)
        self.comboDevices.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.comboDevices.setObjectName("comboDevices")
        self.btnEnum = QtWidgets.QPushButton(self.groupBox_2)
        self.btnEnum.setGeometry(QtCore.QRect(20, 70, 231, 31))
        self.btnEnum.setObjectName("btnEnum")
        self.btnOpen = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOpen.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.btnOpen.setObjectName("btnOpen")
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setGeometry(QtCore.QRect(150, 110, 101, 31))
        self.btnClose.setObjectName("btnClose")
        self.radioContinueMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioContinueMode.setGeometry(QtCore.QRect(20, 150, 110, 24))
        self.radioContinueMode.setObjectName("radioContinueMode")
        self.radioTriggerMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioTriggerMode.setGeometry(QtCore.QRect(160, 150, 110, 24))
        self.radioTriggerMode.setObjectName("radioTriggerMode")
        self.bnStart = QtWidgets.QPushButton(self.groupBox_2)
        self.bnStart.setGeometry(QtCore.QRect(20, 220, 103, 29))
        self.bnStart.setObjectName("bnStart")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.label_2.setObjectName("label_2")
        self.editTimeTrigger = QtWidgets.QTextEdit(self.groupBox_2)
        self.editTimeTrigger.setGeometry(QtCore.QRect(150, 180, 101, 31))
        self.editTimeTrigger.setObjectName("editTimeTrigger")
        self.bnStop = QtWidgets.QPushButton(self.groupBox_2)
        self.bnStop.setGeometry(QtCore.QRect(150, 220, 101, 29))
        self.bnStop.setObjectName("bnStop")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 360, 261, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnGetParam = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGetParam.setGeometry(QtCore.QRect(20, 150, 102, 29))
        self.btnGetParam.setObjectName("btnGetParam")
        self.btnSetParam = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSetParam.setGeometry(QtCore.QRect(149, 150, 102, 29))
        self.btnSetParam.setObjectName("btnSetParam")
        self.edtExposureTime = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtExposureTime.setGeometry(QtCore.QRect(150, 30, 101, 31))
        self.edtExposureTime.setObjectName("edtExposureTime")
        self.edtGain = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtGain.setGeometry(QtCore.QRect(150, 70, 101, 31))
        self.edtGain.setObjectName("edtGain")
        self.edtFrameRate = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtFrameRate.setGeometry(QtCore.QRect(150, 110, 101, 31))
        self.edtFrameRate.setObjectName("edtFrameRate")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1300, 7, 251, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 345, 251, 191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btnRunInference = QtWidgets.QPushButton(self.groupBox_5)
        self.btnRunInference.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.btnRunInference.setObjectName("btnRunInference")
        self.btnLoadImage = QtWidgets.QPushButton(self.groupBox_5)
        self.btnLoadImage.setGeometry(QtCore.QRect(130, 60, 101, 31))
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(20, 110, 63, 20))
        self.label_21.setObjectName("label_21")
        self.editInferenceTimeImage = QtWidgets.QTextEdit(self.groupBox_5)
        self.editInferenceTimeImage.setGeometry(QtCore.QRect(100, 110, 131, 31))
        self.editInferenceTimeImage.setObjectName("editInferenceTimeImage")
        self.Combo_model = QtWidgets.QGroupBox(self.tab)
        self.Combo_model.setGeometry(QtCore.QRect(0, -16, 251, 351))
        self.Combo_model.setTitle("")
        self.Combo_model.setObjectName("Combo_model")
        self.label_13 = QtWidgets.QLabel(self.Combo_model)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 63, 20))
        self.label_13.setObjectName("label_13")
        self.comboModels = QtWidgets.QComboBox(self.Combo_model)
        self.comboModels.setGeometry(QtCore.QRect(80, 30, 151, 31))
        self.comboModels.setObjectName("comboModels")
        self.comboModels.addItem("")
        self.comboModels.addItem("")
        self.comboModels.addItem("")
        self.btnLoadCheckpoint = QtWidgets.QPushButton(self.Combo_model)
        self.btnLoadCheckpoint.setGeometry(QtCore.QRect(11, 72, 221, 31))
        self.btnLoadCheckpoint.setObjectName("btnLoadCheckpoint")
        self.label_18 = QtWidgets.QLabel(self.Combo_model)
        self.label_18.setGeometry(QtCore.QRect(11, 126, 63, 20))
        self.label_18.setObjectName("label_18")
        self.editInferenceTime = QtWidgets.QTextEdit(self.Combo_model)
        self.editInferenceTime.setGeometry(QtCore.QRect(100, 120, 131, 31))
        self.editInferenceTime.setObjectName("editInferenceTime")
        self.label_19 = QtWidgets.QLabel(self.Combo_model)
        self.label_19.setGeometry(QtCore.QRect(12, 176, 71, 21))
        self.label_19.setObjectName("label_19")
        self.editScoreThreshold = QtWidgets.QTextEdit(self.Combo_model)
        self.editScoreThreshold.setGeometry(QtCore.QRect(100, 170, 131, 31))
        self.editScoreThreshold.setObjectName("editScoreThreshold")
        self.btnRunInferenceVideo = QtWidgets.QPushButton(self.Combo_model)
        self.btnRunInferenceVideo.setGeometry(QtCore.QRect(10, 221, 93, 29))
        self.btnRunInferenceVideo.setObjectName("btnRunInferenceVideo")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnLoadCalib = QtWidgets.QPushButton(self.tab_2)
        self.btnLoadCalib.setGeometry(QtCore.QRect(128, 56, 101, 31))
        self.btnLoadCalib.setObjectName("btnLoadCalib")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(8, 26, 81, 20))
        self.label_20.setObjectName("label_20")
        self.editLoadedCalib = QtWidgets.QTextEdit(self.tab_2)
        self.editLoadedCalib.setGeometry(QtCore.QRect(98, 16, 131, 31))
        self.editLoadedCalib.setObjectName("editLoadedCalib")
        self.btnRunCalib = QtWidgets.QPushButton(self.tab_2)
        self.btnRunCalib.setGeometry(QtCore.QRect(8, 56, 91, 31))
        self.btnRunCalib.setObjectName("btnRunCalib")
        self.editChessboardLength = QtWidgets.QTextEdit(self.tab_2)
        self.editChessboardLength.setGeometry(QtCore.QRect(148, 93, 80, 31))
        self.editChessboardLength.setObjectName("editChessboardLength")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(14, 103, 150, 20))
        self.label_22.setObjectName("label_22")
        self.editChessboardWidth = QtWidgets.QTextEdit(self.tab_2)
        self.editChessboardWidth.setGeometry(QtCore.QRect(148, 134, 80, 31))
        self.editChessboardWidth.setObjectName("editChessboardWidth")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(14, 144, 110, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(14, 185, 81, 20))
        self.label_24.setObjectName("label_24")
        self.editImageLength = QtWidgets.QTextEdit(self.tab_2)
        self.editImageLength.setGeometry(QtCore.QRect(148, 175, 80, 31))
        self.editImageLength.setObjectName("editImageLength")
        self.editImageWidth = QtWidgets.QTextEdit(self.tab_2)
        self.editImageWidth.setGeometry(QtCore.QRect(148, 216, 80, 31))
        self.editImageWidth.setObjectName("editImageWidth")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(14, 226, 81, 20))
        self.label_25.setObjectName("label_25")
        self.editSquareSize = QtWidgets.QTextEdit(self.tab_2)
        self.editSquareSize.setGeometry(QtCore.QRect(148, 253, 80, 31))
        self.editSquareSize.setObjectName("editSquareSize")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(14, 263, 135, 20))
        self.label_26.setObjectName("label_26")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(-1, 293, 243, 239))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnStartCamCalibTest = QtWidgets.QPushButton(self.groupBox_4)
        self.btnStartCamCalibTest.setGeometry(QtCore.QRect(147, 26, 82, 31))
        self.btnStartCamCalibTest.setObjectName("btnStartCamCalibTest")
        self.editPixCoordX = QtWidgets.QTextEdit(self.groupBox_4)
        self.editPixCoordX.setGeometry(QtCore.QRect(148, 68, 80, 31))
        self.editPixCoordX.setObjectName("editPixCoordX")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(14, 78, 150, 20))
        self.label_36.setObjectName("label_36")
        self.editPixCoordY = QtWidgets.QTextEdit(self.groupBox_4)
        self.editPixCoordY.setGeometry(QtCore.QRect(148, 100, 80, 31))
        self.editPixCoordY.setObjectName("editPixCoordY")
        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setGeometry(QtCore.QRect(14, 110, 150, 20))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_4)
        self.label_38.setGeometry(QtCore.QRect(14, 142, 150, 20))
        self.label_38.setObjectName("label_38")
        self.editWorldCoordX = QtWidgets.QTextEdit(self.groupBox_4)
        self.editWorldCoordX.setGeometry(QtCore.QRect(148, 132, 80, 31))
        self.editWorldCoordX.setObjectName("editWorldCoordX")
        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setGeometry(QtCore.QRect(14, 174, 150, 20))
        self.label_39.setObjectName("label_39")
        self.editPixelCoordY = QtWidgets.QTextEdit(self.groupBox_4)
        self.editPixelCoordY.setGeometry(QtCore.QRect(148, 164, 80, 31))
        self.editPixelCoordY.setObjectName("editPixelCoordY")
        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setGeometry(QtCore.QRect(14, 207, 150, 20))
        self.label_40.setObjectName("label_40")
        self.editWorldLength = QtWidgets.QTextEdit(self.groupBox_4)
        self.editWorldLength.setGeometry(QtCore.QRect(148, 197, 80, 31))
        self.editWorldLength.setObjectName("editWorldLength")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1610, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btnEnum.clicked.connect(self.displayLabel.clear)
        self.btnOpen.clicked.connect(self.displayLabel.clear)
        self.btnClose.clicked.connect(self.displayLabel.clear)
        self.bnStart.clicked.connect(self.displayLabel.clear)
        self.bnStop.clicked.connect(self.displayLabel.clear)
        self.btnGetParam.clicked.connect(self.displayLabel.clear)
        self.btnSetParam.clicked.connect(self.displayLabel.clear)
        self.radioContinueMode.clicked['bool'].connect(self.displayLabel.clear)
        self.radioTriggerMode.clicked.connect(self.displayLabel.clear)
        self.btnLoadCheckpoint.clicked.connect(self.displayLabel.clear)
        self.btnRunInferenceVideo.clicked.connect(self.displayLabel.clear)
        self.btnRunInference.clicked.connect(self.displayLabel.clear)
        self.btnLoadImage.clicked.connect(self.displayLabel.clear)
        self.btnLoadCalib.clicked.connect(self.displayLabel.clear)
        self.btnRunCalib.clicked.connect(self.displayLabel.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.overwriteLogic()

    def overwriteLogic(self):
        # Will be overwritten in child class
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "DISPLAY"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Camera setting"))
        self.btnEnum.setText(_translate("MainWindow", "Enum"))
        self.btnOpen.setText(_translate("MainWindow", "Open"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.radioContinueMode.setText(_translate("MainWindow", "Continue"))
        self.radioTriggerMode.setText(_translate("MainWindow", "Trigger"))
        self.bnStart.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Time trigger(s):"))
        self.bnStop.setText(_translate("MainWindow", "Stop"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parameters"))
        self.label_3.setText(_translate("MainWindow", "ExposureTime:"))
        self.label_4.setText(_translate("MainWindow", "Gain:"))
        self.label_5.setText(_translate("MainWindow", "FrameRate:"))
        self.btnGetParam.setText(_translate("MainWindow", "GetParam"))
        self.btnSetParam.setText(_translate("MainWindow", "SetParam"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Single Image Inference"))
        self.btnRunInference.setText(_translate("MainWindow", "Run"))
        self.btnLoadImage.setText(_translate("MainWindow", "Load"))
        self.label_21.setText(_translate("MainWindow", "Time:(s): "))
        self.label_13.setText(_translate("MainWindow", "Model:"))
        self.comboModels.setItemText(0, _translate("MainWindow", "Solov2"))
        self.comboModels.setItemText(1, _translate("MainWindow", "Faster_RCNN"))
        self.comboModels.setItemText(2, _translate("MainWindow", "YOLOX-s"))
        self.btnLoadCheckpoint.setText(_translate("MainWindow", "Load"))
        self.label_18.setText(_translate("MainWindow", "Time:(s): "))
        self.label_19.setText(_translate("MainWindow", "Threshold"))
        self.btnRunInferenceVideo.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Computer Vision"))
        self.btnLoadCalib.setText(_translate("MainWindow", "Load"))
        self.label_20.setText(_translate("MainWindow", "Calib File:"))
        self.btnRunCalib.setText(_translate("MainWindow", "Run"))
        self.editChessboardLength.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "Chessboard Length"))
        self.editChessboardWidth.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "Chessboard Width"))
        self.label_24.setText(_translate("MainWindow", "Image Length"))
        self.editImageLength.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2592</p></body></html>"))
        self.editImageWidth.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1944</p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Image Width"))
        self.editSquareSize.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23.7</p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "Square Size (mm)"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Testing Area"))
        self.btnStartCamCalibTest.setText(_translate("MainWindow", "Start"))
        self.editPixCoordX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "Pixel Coordinate X"))
        self.editPixCoordY.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "Pixel Coordinate Y"))
        self.label_38.setText(_translate("MainWindow", "World Coordinate X"))
        self.editWorldCoordX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "Wolrd Coordinate Y"))
        self.editPixelCoordY.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "World Length"))
        self.editWorldLength.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "CameraCalib"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
